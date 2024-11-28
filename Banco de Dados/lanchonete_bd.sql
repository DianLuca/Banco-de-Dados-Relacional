-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 17/11/2024 às 19:12
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `lanchonete_bd`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `atendimento`
--

CREATE TABLE `atendimento` (
  `Id` int(11) NOT NULL,
  `Id_Funcionario` int(11) NOT NULL,
  `Id_Cliente` int(11) NOT NULL,
  `Id_Pedido` int(11) NOT NULL,
  `Data_Atendimento` timestamp NOT NULL DEFAULT current_timestamp(),
  `Status` enum('Pendente','Concluído') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `atendimento`
--

INSERT INTO `atendimento` (`Id`, `Id_Funcionario`, `Id_Cliente`, `Id_Pedido`, `Data_Atendimento`, `Status`) VALUES
(7, 1, 1, 1, '2024-11-17 14:46:58', 'Pendente'),
(8, 1, 1, 2, '2024-11-17 14:46:58', 'Pendente'),
(9, 2, 2, 3, '2024-11-17 14:46:58', 'Concluído'),
(10, 5, 3, 4, '2024-11-17 14:46:58', 'Pendente'),
(11, 6, 4, 5, '2024-11-17 14:46:58', 'Concluído'),
(12, 3, 5, 6, '2024-11-17 14:46:58', 'Pendente'),
(13, 4, 6, 7, '2024-11-17 14:46:58', 'Concluído');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `Id_Cliente` int(11) NOT NULL,
  `Nome_Cliente` varchar(100) NOT NULL,
  `Email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`Id_Cliente`, `Nome_Cliente`, `Email`) VALUES
(1, 'Dian Luca', 'Di@email.com'),
(2, 'Leonardo', 'l@email.com'),
(3, 'Beatriz', 'Be@email.com'),
(4, 'Bruno', 'b@email.com'),
(5, 'Colyana', 'c@email.com'),
(6, 'Sebastião', 's@email.com'),
(7, 'Isis', 'i@email.com'),
(8, 'Agata', 'Ag@email.com'),
(9, 'Danilo', 'd@email.com'),
(10, 'Moises', 'm@email.com'),
(11, 'Gilber', 'g@email.com'),
(12, 'Vinicius', 'v@email.com'),
(13, 'Augusto', 'a@email.com'),
(14, 'Brendon', 'br@email.com'),
(15, 'Arthur', 'ar@email.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `Id_Funcionario` int(11) NOT NULL,
  `Nome_Funcionario` varchar(100) NOT NULL,
  `Cargo` varchar(100) NOT NULL DEFAULT 'Atendente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `funcionario`
--

INSERT INTO `funcionario` (`Id_Funcionario`, `Nome_Funcionario`, `Cargo`) VALUES
(1, 'João', 'Atendente'),
(2, 'José', 'Atendente'),
(3, 'Maria', 'Atendente'),
(4, 'Hermanoteu', 'Gerente'),
(5, 'Micalateia', 'Atendente'),
(6, 'Isaac', 'Atendente');

-- --------------------------------------------------------

--
-- Estrutura para tabela `itens_pedido`
--

CREATE TABLE `itens_pedido` (
  `Id` int(11) NOT NULL,
  `Id_Pedido` int(11) NOT NULL,
  `Id_Produto` int(11) NOT NULL,
  `Quantidade` int(11) NOT NULL,
  `Valor_Total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `itens_pedido`
--

INSERT INTO `itens_pedido` (`Id`, `Id_Pedido`, `Id_Produto`, `Quantidade`, `Valor_Total`) VALUES
(1, 1, 1, 3, 26.70),
(2, 1, 8, 2, 10.00),
(3, 2, 3, 1, 5.99),
(4, 3, 2, 1, 15.75),
(5, 4, 6, 2, 44.00),
(7, 6, 2, 1, 15.75),
(8, 6, 6, 1, 22.00),
(9, 7, 1, 2, 17.80),
(10, 5, 5, 10, 45.00);

--
-- Acionadores `itens_pedido`
--
DELIMITER $$
CREATE TRIGGER `CalcularValorTotal` BEFORE INSERT ON `itens_pedido` FOR EACH ROW BEGIN 
	DECLARE preco DECIMAL(10, 2);
    
    SELECT Preco_Unitario INTO preco
    FROM produto
    WHERE Id_Produto = NEW.Id_Produto;
    
    SET preco = preco * NEW.Quantidade;
    
    SET NEW.Valor_Total = preco;
    
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Verifica_Estoque` BEFORE INSERT ON `itens_pedido` FOR EACH ROW BEGIN
	DECLARE nova_quantidade INT;
    DECLARE status ENUM('Pendente', 'Finalizado', 'Cancelado', 'Em Preparo');
    
    SELECT Status INTO status
    FROM pedido
    WHERE Id_Pedido = NEW.Id_Pedido;
    
    SELECT Quantidade_Estoque INTO nova_quantidade
    FROM produto
    WHERE Id_Produto = NEW.Id_Produto;
    
    IF status = 'Cancelado' THEN
    	SET NEW.Quantidade = 0;
    ELSE
        
    SET nova_quantidade = nova_quantidade - NEW.Quantidade;
    END IF;
    
    UPDATE produto
    SET Quantidade_Estoque = nova_quantidade
    WHERE Id_Produto = NEW.Id_Produto;
    
    IF nova_quantidade < NEW.Quantidade THEN
    	SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Não há produto(s) o suficiente para concluir o pedido.';
        END IF;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedido`
--

CREATE TABLE `pedido` (
  `Id_Pedido` int(11) NOT NULL,
  `Id_Cliente` int(11) DEFAULT NULL,
  `Status` enum('Pendente','Em Preparo','Finalizado','Cancelado') DEFAULT NULL,
  `Data_Pedido` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `pedido`
--

INSERT INTO `pedido` (`Id_Pedido`, `Id_Cliente`, `Status`, `Data_Pedido`) VALUES
(1, 1, 'Pendente', '2024-11-16 19:05:11'),
(2, 1, 'Pendente', '2024-11-16 19:05:11'),
(3, 2, 'Finalizado', '2024-11-16 19:05:11'),
(4, 3, 'Em Preparo', '2024-11-16 19:05:11'),
(5, 4, 'Cancelado', '2024-11-16 19:05:11'),
(6, 5, 'Pendente', '2024-11-16 19:05:11'),
(7, 6, 'Finalizado', '2024-11-16 19:05:11');

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

CREATE TABLE `produto` (
  `Id_Produto` int(11) NOT NULL,
  `Nome_Produto` varchar(255) NOT NULL,
  `Quantidade_Estoque` int(11) DEFAULT NULL,
  `Preco_Unitario` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `produto`
--

INSERT INTO `produto` (`Id_Produto`, `Nome_Produto`, `Quantidade_Estoque`, `Preco_Unitario`) VALUES
(1, 'Misto Quente', 45, 8.90),
(2, 'Hamburguer', 118, 15.75),
(3, 'Coca-Cola 350ml', 249, 5.99),
(4, 'Guaraná 600ml', 10, 7.50),
(5, 'Suco de Laranja ', 30, 4.50),
(6, 'X-Bacon', 72, 22.00),
(7, 'Fanta Uva 350ml', 150, 6.25),
(8, 'Suco de Abacaxi', 58, 5.00);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `atendimento`
--
ALTER TABLE `atendimento`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Id_Cliente` (`Id_Cliente`),
  ADD KEY `Id_Funcionario` (`Id_Funcionario`),
  ADD KEY `Id_Pedido` (`Id_Pedido`);

--
-- Índices de tabela `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`Id_Cliente`,`Nome_Cliente`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`Id_Funcionario`,`Nome_Funcionario`);

--
-- Índices de tabela `itens_pedido`
--
ALTER TABLE `itens_pedido`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Id_Pedido` (`Id_Pedido`),
  ADD KEY `Id_Produto` (`Id_Produto`);

--
-- Índices de tabela `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`Id_Pedido`),
  ADD KEY `Id_Cliente` (`Id_Cliente`);

--
-- Índices de tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`Id_Produto`,`Nome_Produto`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `atendimento`
--
ALTER TABLE `atendimento`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `cliente`
--
ALTER TABLE `cliente`
  MODIFY `Id_Cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `Id_Funcionario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `itens_pedido`
--
ALTER TABLE `itens_pedido`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `pedido`
--
ALTER TABLE `pedido`
  MODIFY `Id_Pedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `Id_Produto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `atendimento`
--
ALTER TABLE `atendimento`
  ADD CONSTRAINT `atendimento_ibfk_1` FOREIGN KEY (`Id_Cliente`) REFERENCES `cliente` (`Id_Cliente`),
  ADD CONSTRAINT `atendimento_ibfk_2` FOREIGN KEY (`Id_Funcionario`) REFERENCES `funcionario` (`Id_Funcionario`),
  ADD CONSTRAINT `atendimento_ibfk_3` FOREIGN KEY (`Id_Pedido`) REFERENCES `pedido` (`Id_Pedido`);

--
-- Restrições para tabelas `itens_pedido`
--
ALTER TABLE `itens_pedido`
  ADD CONSTRAINT `itens_pedido_ibfk_1` FOREIGN KEY (`Id_Pedido`) REFERENCES `pedido` (`Id_Pedido`),
  ADD CONSTRAINT `itens_pedido_ibfk_2` FOREIGN KEY (`Id_Produto`) REFERENCES `produto` (`Id_Produto`);

--
-- Restrições para tabelas `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`Id_Cliente`) REFERENCES `cliente` (`Id_Cliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
