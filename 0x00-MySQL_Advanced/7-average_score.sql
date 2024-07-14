-- average score

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE mean FLOAT;

  -- Calcul de la moyenne des scores
  SELECT AVG(score) INTO mean
  FROM corrections
  WHERE corrections.user_id = user_id;

  -- Mise à jour de la moyenne des scores dans la table users
  UPDATE users
  SET average_score = mean
  WHERE users.id = user_id;

END;

//

DELIMITER ;
