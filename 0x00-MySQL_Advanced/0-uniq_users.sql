--unique attributes importance
CREATE IF NOT EXISTS TABLE users(
  id INTEGER AUTO_INCREMENT PRIMARY_KEY NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
);