CREATE DATABASE ticket_dev;
USE ticket_dev;

CREATE TABLE ticket_request (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT NOT NULL,
    sender_id INT NOT NULL,
    fk_agent_valide INT,
    ticket_id INT,
    status ENUM('acceptee', 'suspens'),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table des messages (fil de discussion)
CREATE TABLE ticket_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT NOT NULL,      -- Clé vers ticket Dolibarr
    sender_id INT NOT NULL,      -- Clé vers utilisateur ou contact Dolibarr
    sender_role ENUM('agent', 'client') NOT NULL,
    message TEXT NOT NULL,
    attachment_path VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table des évaluations après résolution
CREATE TABLE ticket_evaluations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT NOT NULL,      -- Clé vers ticket Dolibarr
    client_id INT NOT NULL,      -- Clé vers client Dolibarr
    rating TINYINT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Historique des statuts de ticket
CREATE TABLE ticket_status_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT NOT NULL,      -- Clé vers ticket Dolibarr
    old_status ENUM('ouvert', 'en cours', 'résolu', 'fermé'),
    new_status ENUM('ouvert', 'en cours', 'résolu', 'fermé'),
    changed_by INT,              -- ID de l'utilisateur Dolibarr
    changed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tarifs par type de ticket
CREATE TABLE tarif_ticket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    montant DOUBLE,
    ticket_type_id INT, -- ty id makany an dolibarr koa
    changed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


