-- index first letter

CREATE INDEX idx_name_first_score on names(name(1));
