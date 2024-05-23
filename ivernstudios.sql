CREATE DATABASE ivernstudios;
USE ivernstudios;

CREATE TABLE company (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    position VARCHAR(100)
);

INSERT INTO company (name, age, position) VALUES 
('Ivern Buala', 'Founder', 21),
('Lawrence Apalla', 'Co-Founder', 20),
('Joshua Matriano', 'Co-Founder', 18),
('Gian Carlo Sambayan', 'Co-Founder', 20),
('Allyson Keihl Valdez', 'Co-Founder', 20),
('Yoshimichi Maruo', '3D Artist', 24),
('Johannes Suh', 'Graphic Designer', 24),
('Mark Conrad', 'Motion Designer', 21),
('Caryl Atienza', 'Graphic Designer', 18),
('Brian Cafranca', 'Graphic Designer', 19),

('HK Sauza', '3D Artist', 20),
('Mikael Denzo', '3D Artist', 20),
('Yeshua Nazareno', 'Apparel Designer', 17),
('Yves Steven', 'Graphic Designer', 19),
('Justine Ayag', 'Graphic Designer', 21),
('Bien Austin', 'Graphic Designer', 19),
('Dyric Espinosa', 'Graphic Designer', 17),
('Jed Felisilda', 'Graphic Designer', 20),
('Kervin Dela Cruz', 'Graphic Designer', 20),
('Adrianne Blu Sanchez', 'Video Editor', 21);