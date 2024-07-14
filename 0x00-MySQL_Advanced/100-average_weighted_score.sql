-- average score

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
  DECLARE mean FLOAT;
  DECLARE total INT;
  DECLARE total_weight INT;
  
  -- Calcul de la moyenne des scores
  SELECT SUM(corrections.score * projects.weight), SUM(weight)
  INTO total, total_weight
  FROM corrections INNER JOIN projects ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;

  IF total_weight > 0 THEN
    SET mean = total / total_weight;
  ELSE
    SET mean = 0;
  END IF;
  
  UPDATE users
  SET average_score = mean
  WHERE users.id = user_id;

END;

//

DELIMITER ;
