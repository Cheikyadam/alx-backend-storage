-- stored procedure

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN users_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE v_count INT;
    DECLARE p_id INT;

    -- Vérifie l'existence du projet
    SELECT COUNT(*) INTO v_count
    FROM projects
    WHERE name = project_name;

    -- Si le projet n'existe pas, l'insère
    IF v_count = 0 THEN
        INSERT INTO projects(name)
        VALUES(project_name);
    END IF;

    -- Récupère l'ID du projet
    SELECT id INTO p_id
    FROM projects
    WHERE name = project_name;

    -- Insère la correction
    INSERT INTO corrections(user_id, project_id, score)
    VALUES(users_id, p_id, score);
END;

//

DELIMITER ;
