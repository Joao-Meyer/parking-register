CREATE DATABASE `estacionamento` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE 'estacionamento';

CREATE TABLE `vagas` (
  `posicao` varchar(100) NOT NULL,
  `ocupada` tinyint(1) NOT NULL,
  `nome` varchar(250) DEFAULT NULL,
  `ondeesta` varchar(250) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;