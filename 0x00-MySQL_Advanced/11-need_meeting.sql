-- view

CREATE VIEW need_meeting AS
SELECT name 
FROM students
WHERE score < 80
    AND (last_meeting is NULL OR 
	last_meeting < DATE_ADD(CURDATE(), INTERVAL -1 MONTH));
