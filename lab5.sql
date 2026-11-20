USE `mydb`;

-- =====================================================================
-- 1. ДОДАТКОВА ТАБЛИЦЯ (1:M ДО actors) + ТРИГЕРИ ЦІЛІСНОСТІ ЗАМІСТЬ FK
-- =====================================================================
DROP TABLE IF EXISTS `mydb`.`actor_awards`;
CREATE TABLE `mydb`.`actor_awards` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `award_name` VARCHAR(100) NOT NULL,
  `award_year` INT NOT NULL,
  `actor_id` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- Тестові дані для нової таблиці (прив'язані до існуючих акторів 1, 2, 6)
INSERT INTO `mydb`.`actor_awards` (`award_name`, `award_year`, `actor_id`) VALUES
('MTV Movie Award', 2000, 1),
('Oscar Best Supporting Actor', 2011, 2),
('Oscar Best Actor', 2016, 6);

DELIMITER //

-- Тригер 1.1: перевірка існування actor_id при вставці в actor_awards
DROP TRIGGER IF EXISTS `trg_actor_awards_before_insert` //
CREATE TRIGGER `trg_actor_awards_before_insert`
BEFORE INSERT ON `actor_awards`
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM `actors` WHERE `id` = NEW.actor_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Помилка цілісності: актора з таким actor_id не існує в таблиці actors';
    END IF;
END //

-- Тригер 1.2: перевірка існування actor_id при оновленні actor_awards
DROP TRIGGER IF EXISTS `trg_actor_awards_before_update` //
CREATE TRIGGER `trg_actor_awards_before_update`
BEFORE UPDATE ON `actor_awards`
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM `actors` WHERE `id` = NEW.actor_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Помилка цілісності: актора з таким actor_id не існує в таблиці actors';
    END IF;
END //

-- Тригер 1.3: заборона видалення актора, якщо у нього є нагороди в actor_awards
DROP TRIGGER IF EXISTS `trg_actors_before_delete_awards` //
CREATE TRIGGER `trg_actors_before_delete_awards`
BEFORE DELETE ON `actors`
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM `actor_awards` WHERE `actor_id` = OLD.id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Помилка цілісності: не можна видалити актора, оскільки він має записи в actor_awards';
    END IF;
END //

-- Тригер 1.4: заборона зміни id актора, якщо на нього посилається actor_awards
DROP TRIGGER IF EXISTS `trg_actors_before_update_awards` //
CREATE TRIGGER `trg_actors_before_update_awards`
BEFORE UPDATE ON `actors`
FOR EACH ROW
BEGIN
    IF OLD.id <> NEW.id AND EXISTS (SELECT 1 FROM `actor_awards` WHERE `actor_id` = OLD.id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Помилка цілісності: не можна змінити id актора, бо на нього посилається actor_awards';
    END IF;
END //

-- =====================================================================
-- 2. ЗБЕРЕЖЕНІ ПРОЦЕДУРИ ТА КОРИСТУВАЦЬКА ФУНКЦІЯ
-- =====================================================================

-- 2.1. Параметризована вставка нових значень у таблицю actors
DROP PROCEDURE IF EXISTS `sp_insert_actor` //
CREATE PROCEDURE `sp_insert_actor`(
    IN p_name VARCHAR(45),
    IN p_birthday DATE
)
BEGIN
    INSERT INTO `actors` (`name`, `birthday`) VALUES (p_name, p_birthday);
    SELECT LAST_INSERT_ID() AS inserted_id, p_name AS name, p_birthday AS birthday;
END //

-- 2.2. Реалізація зв'язку M:M (вставка в content_actors за іменем актора і назвою контенту)
DROP PROCEDURE IF EXISTS `sp_link_actor_content` //
CREATE PROCEDURE `sp_link_actor_content`(
    IN p_actor_name VARCHAR(45),
    IN p_content_title VARCHAR(45),
    IN p_role_name VARCHAR(45)
)
BEGIN
    DECLARE v_actor_id INT;
    DECLARE v_content_id INT;

    SELECT `id` INTO v_actor_id FROM `actors` WHERE `name` = p_actor_name LIMIT 1;
    SELECT `id` INTO v_content_id FROM `content` WHERE `title` = p_content_title LIMIT 1;

    IF v_actor_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Актора з таким іменем не знайдено';
    END IF;

    IF v_content_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Контент з такою назвою не знайдено';
    END IF;

    INSERT INTO `content_actors` (`actors_id`, `content_id`, `role_name`)
    VALUES (v_actor_id, v_content_id, p_role_name);

    SELECT v_actor_id AS actors_id, v_content_id AS content_id, p_role_name AS role_name;
END //

-- 2.3. Пакетна вставка 10 стрічок у форматі Noname+№ у таблицю subscription
DROP PROCEDURE IF EXISTS `sp_insert_10_noname_subscriptions` //
CREATE PROCEDURE `sp_insert_10_noname_subscriptions`(
    IN p_start_num INT
)
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 10 DO
        INSERT INTO `subscription` (`name`, `description`)
        VALUES (CONCAT('Noname', p_start_num + i), CONCAT('Auto-generated #', p_start_num + i));
        SET i = i + 1;
    END WHILE;

    SELECT CONCAT('Додано 10 записів: від Noname', p_start_num, ' до Noname', p_start_num + 9) AS message;
END //

-- 2.4. Користувацька функція (середній рейтинг відгуків AVG) + процедура, яка її викликає
DROP FUNCTION IF EXISTS `fn_avg_review_rating` //
CREATE FUNCTION `fn_avg_review_rating`()
RETURNS DECIMAL(5, 2)
READS SQL DATA
BEGIN
    DECLARE v_avg DECIMAL(5, 2);
    SELECT AVG(`rating`) INTO v_avg FROM `user_review`;
    RETURN IFNULL(v_avg, 0.00);
END //

DROP PROCEDURE IF EXISTS `sp_get_avg_review_rating` //
CREATE PROCEDURE `sp_get_avg_review_rating`()
BEGIN
    SELECT `fn_avg_review_rating`() AS average_rating;
END //

-- 2.5. Процедура з курсором: динамічне створення 2 таблиць зі штампом часу
-- та випадкове пострічкове копіювання даних з таблиці actors
DROP PROCEDURE IF EXISTS `sp_split_actors_cursor` //
CREATE PROCEDURE `sp_split_actors_cursor`()
BEGIN
    DECLARE v_done INT DEFAULT 0;
    DECLARE v_id INT;
    DECLARE v_name VARCHAR(45);
    DECLARE v_birthday DATE;
    DECLARE v_ts VARCHAR(20);
    DECLARE v_table1 VARCHAR(64);
    DECLARE v_table2 VARCHAR(64);

    DECLARE actor_cursor CURSOR FOR
        SELECT `id`, `name`, `birthday` FROM `actors`;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = 1;

    SET v_ts = DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s');
    SET v_table1 = CONCAT('actors_copy1_', v_ts);
    SET v_table2 = CONCAT('actors_copy2_', v_ts);

    SET @sql_create1 = CONCAT('CREATE TABLE `', v_table1, '` LIKE `actors`');
    PREPARE stmt1 FROM @sql_create1;
    EXECUTE stmt1;
    DEALLOCATE PREPARE stmt1;

    SET @sql_create2 = CONCAT('CREATE TABLE `', v_table2, '` LIKE `actors`');
    PREPARE stmt2 FROM @sql_create2;
    EXECUTE stmt2;
    DEALLOCATE PREPARE stmt2;

    OPEN actor_cursor;

    read_loop: LOOP
        FETCH actor_cursor INTO v_id, v_name, v_birthday;
        IF v_done = 1 THEN
            LEAVE read_loop;
        END IF;

        SET @p_id = v_id;
        SET @p_name = v_name;
        SET @p_birthday = v_birthday;

        IF RAND() < 0.5 THEN
            SET @sql_ins = CONCAT('INSERT INTO `', v_table1, '` (`id`, `name`, `birthday`) VALUES (?, ?, ?)');
        ELSE
            SET @sql_ins = CONCAT('INSERT INTO `', v_table2, '` (`id`, `name`, `birthday`) VALUES (?, ?, ?)');
        END IF;

        PREPARE stmt_ins FROM @sql_ins;
        EXECUTE stmt_ins USING @p_id, @p_name, @p_birthday;
        DEALLOCATE PREPARE stmt_ins;
    END LOOP;

    CLOSE actor_cursor;

    SELECT v_table1 AS created_table_1, v_table2 AS created_table_2;
END //

-- =====================================================================
-- 3. ТРИ ДОВІЛЬНІ ТРИГЕРИ ДЛЯ ТАБЛИЦЬ БД
-- =====================================================================

-- 3.1. Заборонити видалення стрічок з таблиці age_ratings
DROP TRIGGER IF EXISTS `trg_forbid_delete_age_ratings` //
CREATE TRIGGER `trg_forbid_delete_age_ratings`
BEFORE DELETE ON `age_ratings`
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Видалення записів з таблиці age_ratings заборонено тригером';
END //

-- 3.2. Таблиця-журнал логів зі штампом часу при видаленні даних з user_review
DELIMITER ;
DROP TABLE IF EXISTS `mydb`.`user_review_delete_log`;
CREATE TABLE `mydb`.`user_review_delete_log` (
  `log_id` INT NOT NULL AUTO_INCREMENT,
  `deleted_review_id` INT NOT NULL,
  `rating` INT NOT NULL,
  `user_id` INT NOT NULL,
  `content_id` INT NOT NULL,
  `deleted_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`log_id`)
) ENGINE = InnoDB;

DELIMITER //
DROP TRIGGER IF EXISTS `trg_log_delete_user_review` //
CREATE TRIGGER `trg_log_delete_user_review`
AFTER DELETE ON `user_review`
FOR EACH ROW
BEGIN
    INSERT INTO `user_review_delete_log` (`deleted_review_id`, `rating`, `user_id`, `content_id`)
    VALUES (OLD.id, OLD.rating, OLD.user_id, OLD.content_id);
END //

-- 3.3. Значення стовпця name у таблиці subscription не може закінчуватись двома нулями ('00')
DROP TRIGGER IF EXISTS `trg_subscription_no_double_zero_ins` //
CREATE TRIGGER `trg_subscription_no_double_zero_ins`
BEFORE INSERT ON `subscription`
FOR EACH ROW
BEGIN
    IF RIGHT(NEW.name, 2) = '00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Назва підписки не може закінчуватись двома нулями (00)';
    END IF;
END //

DROP TRIGGER IF EXISTS `trg_subscription_no_double_zero_upd` //
CREATE TRIGGER `trg_subscription_no_double_zero_upd`
BEFORE UPDATE ON `subscription`
FOR EACH ROW
BEGIN
    IF RIGHT(NEW.name, 2) = '00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Назва підписки не може закінчуватись двома нулями (00)';
    END IF;
END //

DELIMITER ;