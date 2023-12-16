CREATE TABLE `empresa` (
	`id_empresa` int NOT NULL AUTO_INCREMENT,
	`cod` decimal(5,0),
	PRIMARY KEY (`id_empresa`)
); CREATE TABLE `folha_ponto` (
	`id_folha` int NOT NULL AUTO_INCREMENT,
	`id_user` int,
	`data_fp` datetime,
	`falta` tinyint(1),
	`hora` time,
	`atraso` varchar(255),
	`hr_extra` varchar(255),
	`hr_efetiva` varchar(255),
	`folga` tinyint(1),
	PRIMARY KEY (`id_folha`)
); CREATE TABLE `notificacoes` (
	`id_notification` int NOT NULL AUTO_INCREMENT,
	`icon` decimal(30,0),
	`title` varchar(255),
	`message` varchar(255),
	PRIMARY KEY (`id_notification`)
); CREATE TABLE `pedidos_ff` (
	`id_pedidosff` int NOT NULL AUTO_INCREMENT,
	`id_user` int,
	`tipo_pedido` tinyint(1),
	PRIMARY KEY (`id_pedidosff`)
); CREATE TABLE `pontos_dia` (
	`id_ptdia` int NOT NULL AUTO_INCREMENT,
	`id_user` int,
	`entrada` time,
	`almoco` time,
	`retorno` time,
	`saida` time,
	PRIMARY KEY (`id_ptdia`)
); CREATE TABLE `relatorios` (
	`id_relatorio` int NOT NULL AUTO_INCREMENT,
	`id_user` int,
	`id_folha` int,
	`id_salario` int,
	`id_advertencia` int,
	PRIMARY KEY (`id_relatorio`)
); CREATE TABLE `usuarios` (
	`id_usuarios` int NOT NULL AUTO_INCREMENT,
	`nome` varchar(255),
	`cargo` varchar(255),
	`email` varchar(255),
	`cpf` varchar(255),
	`celular` varchar(255),
	`senha` varchar(255),
	`adm` tinyint(1),
	PRIMARY KEY (`id_usuarios`)
)