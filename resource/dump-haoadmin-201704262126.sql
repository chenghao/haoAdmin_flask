-- MySQL dump 10.13  Distrib 5.7.18, for linux-glibc2.5 (x86_64)
--
-- Host: localhost    Database: haoadmin
-- ------------------------------------------------------
-- Server version	5.7.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `h_menu`
--

DROP TABLE IF EXISTS `h_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `h_menu` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `icon` varchar(50) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `menu_name` varchar(20) NOT NULL,
  `menu_url` varchar(100) DEFAULT NULL,
  `parent_menu` int(11) DEFAULT NULL,
  `sort` int(11) NOT NULL,
  `org_ids` longtext,
  `role_ids` longtext,
  PRIMARY KEY (`pid`),
  KEY `h_menu_parent_menu` (`parent_menu`),
  CONSTRAINT `h_menu_ibfk_1` FOREIGN KEY (`parent_menu`) REFERENCES `h_menu` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `h_menu`
--

LOCK TABLES `h_menu` WRITE;
/*!40000 ALTER TABLE `h_menu` DISABLE KEYS */;
INSERT INTO `h_menu` VALUES (1,'2017-04-23 16:06:09',NULL,1,'系统管理',NULL,NULL,1,',1,',',1,'),(2,'2017-04-23 16:07:29','fa fa-check-square-o',2,'菜单管理','menu/index',1,2,',1,',',1,'),(3,'2017-04-23 16:08:02','fa fa-check-square-o',2,'角色管理','role/index',1,3,',1,',',1,'),(4,'2017-04-23 16:08:56','fa fa-check-square-o',2,'用户管理','user/index',1,4,',1,',',1,'),(5,'2017-04-23 16:09:25','fa fa-check-square-o',2,'字典管理','type/index',1,5,',1,',',1,');
/*!40000 ALTER TABLE `h_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `h_org`
--

DROP TABLE IF EXISTS `h_org`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `h_org` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `parent_org` int(11) DEFAULT NULL,
  PRIMARY KEY (`pid`),
  KEY `h_org_parent_org` (`parent_org`),
  CONSTRAINT `h_org_ibfk_1` FOREIGN KEY (`parent_org`) REFERENCES `h_org` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `h_org`
--

LOCK TABLES `h_org` WRITE;
/*!40000 ALTER TABLE `h_org` DISABLE KEYS */;
INSERT INTO `h_org` VALUES (1,'2017-04-23 16:03:02','haoAdmin机构',NULL,NULL);
/*!40000 ALTER TABLE `h_org` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `h_role`
--

DROP TABLE IF EXISTS `h_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `h_role` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `role_name` varchar(20) NOT NULL,
  `role_code` varchar(20) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `h_role`
--

LOCK TABLES `h_role` WRITE;
/*!40000 ALTER TABLE `h_role` DISABLE KEYS */;
INSERT INTO `h_role` VALUES (1,'2017-04-23 16:03:22','管理员','admin');
/*!40000 ALTER TABLE `h_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `h_type`
--

DROP TABLE IF EXISTS `h_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `h_type` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `group_id` int(11) NOT NULL,
  `type_name` varchar(20) NOT NULL,
  `type_value` varchar(20) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `h_type`
--

LOCK TABLES `h_type` WRITE;
/*!40000 ALTER TABLE `h_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `h_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `h_typegroup`
--

DROP TABLE IF EXISTS `h_typegroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `h_typegroup` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `group_name` varchar(20) NOT NULL,
  `group_value` varchar(20) NOT NULL,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `h_typegroup_group_value` (`group_value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `h_typegroup`
--

LOCK TABLES `h_typegroup` WRITE;
/*!40000 ALTER TABLE `h_typegroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `h_typegroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `h_user`
--

DROP TABLE IF EXISTS `h_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `h_user` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `login_name` varchar(20) NOT NULL,
  `login_pwd` varchar(64) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `org_ids` longtext,
  `role_ids` longtext,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `h_user_login_name` (`login_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `h_user`
--

LOCK TABLES `h_user` WRITE;
/*!40000 ALTER TABLE `h_user` DISABLE KEYS */;
INSERT INTO `h_user` VALUES (1,'2017-04-22 15:40:45','chenghao','MDk0MjAz96','豪哥',NULL,NULL,',1,',',1,');
/*!40000 ALTER TABLE `h_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'haoadmin'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-26 21:26:17
