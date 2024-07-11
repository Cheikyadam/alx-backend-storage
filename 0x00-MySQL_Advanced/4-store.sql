-- trigger

DELIMITER //

CREATE TRIGGER after_insert_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - 1;
END;

//

DELIMITER ;
