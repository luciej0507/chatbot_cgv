-- Adminer 5.3.0 MySQL 9.3.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `echange`;
CREATE TABLE `echange` (
  `id` int NOT NULL AUTO_INCREMENT,
  `conversation` varchar(100) NOT NULL,
  `prompt` varchar(100) NOT NULL,
  `reponse` varchar(100) NOT NULL,
  `statut` int NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `statut` (`statut`),
  CONSTRAINT `echange_ibfk_1` FOREIGN KEY (`statut`) REFERENCES `status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `status`;
CREATE TABLE `status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `libelle` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

