-- MySQL dump 10.13  Distrib 5.7.23, for osx10.14 (x86_64)
--
-- Host: localhost    Database: cs542
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `_yoyo_log`
--

DROP TABLE IF EXISTS `_yoyo_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `_yoyo_log` (
  `id` varchar(36) NOT NULL,
  `migration_hash` varchar(64) DEFAULT NULL,
  `migration_id` varchar(255) DEFAULT NULL,
  `operation` varchar(10) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `hostname` varchar(255) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `created_at_utc` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `_yoyo_log`
--

LOCK TABLES `_yoyo_log` WRITE;
/*!40000 ALTER TABLE `_yoyo_log` DISABLE KEYS */;
INSERT INTO `_yoyo_log` VALUES ('ce32eb9a-fe61-11e9-add2-acde48001122','81e62d691d3c572b67ceaccfe1c8e993a664c93fde3178c697660abaafed2786','20190913_01_rb2OO-create-users','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce35b80c-fe61-11e9-add2-acde48001122','ba8e6a94debacc0b0edb1e44d911424f4912cbcfe3e4065d92f9753773963cb2','20190913_02_LViZ5-create-events','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce380846-fe61-11e9-add2-acde48001122','82fd6bbdf5028e74ba828a3f3874ec4097081ef717a1e9e9f9cf386c0e984f0e','20190916_01_77FxU-drop-user-salt','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce39d55e-fe61-11e9-add2-acde48001122','7482587cc92cadab3fa0e9aef17c19090a44f7907da769a539f83d9af0126de0','20190916_01_KsWxH-create-UserRoles','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce3bbe00-fe61-11e9-add2-acde48001122','cfc70e42d1332ba5160fb81e726939aea4e9d6ecd494c964af039d487a2cdb52','20190914_01_FONOP-create-route','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce3db41c-fe61-11e9-add2-acde48001122','569ac3020a74b5f4ea6d5b02d5d62fe4ebe47a8fc92ea185cdefbade45c6ea37','20190916_02_RbiMa-create-timeEntry','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce41c1ec-fe61-11e9-add2-acde48001122','b9e12eeaf120ca20ff4d5a3ce9f4686184bec7bfb2f15206b7772e3acd151a3b','20190916_02_CImKu-login-sessions','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce438db0-fe61-11e9-add2-acde48001122','f1ac7d0ea81fd707b915c64fb7ea9886a176bc04e9b3b38c9bf352afe5b91844','20190914_02_gA5Xf-create-tournamentparticipants','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce44a5b0-fe61-11e9-add2-acde48001122','7de44c0cf49b01a9914625d6fa674acda705fa46b26ff92c2d70ce601ae8b520','20190917_01_Jttbg-auto-session-expiry-event','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce45f5b4-fe61-11e9-add2-acde48001122','6b298f242d13359cdcdb684d5eef8ecd679b1c792d0b6f03bdc3d8dc21c6fb18','20190927_01_ouV2L-create-userdata-view','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce472a6a-fe61-11e9-add2-acde48001122','0c86c5c4f32ee5b5fd0d86f392c6508592190dcae7232ab14b009e2e884fab0f','20190927_02_RPNwN-create-userdatawithrole-view','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce4c93ce-fe61-11e9-add2-acde48001122','b865c58fbb83cfa892d02b0b112955e105424f0150832235e181c4d5b97a90f1','20191013_01_z7Cn9-cascade-userroles-delete','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce4dd964-fe61-11e9-add2-acde48001122','ef13d3793f03d0e1f7ce8bb3713b2b625ce16a4c24becc46d4ae29e6cea5e44c','20191014_01_GoMDS-trigger-password-change-logout','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce50af2c-fe61-11e9-add2-acde48001122','5279c311262a0841d5020158c9f1ec31802891b0c71b29a4aa522901542aff0a','20191021_01_yPkaO-make-end-in-timeentry-nullable','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce558e5c-fe61-11e9-add2-acde48001122','268da690a4a90e3391985ed5494b8e34e2f93efcdca1342636157b826ac761d7','20191022_01_d2si0-add-opener-to-event','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04'),('ce56cfec-fe61-11e9-add2-acde48001122','7426b4aadb771c5680e817ca14e6dd8b3a870f05ee7050a5e202206f3bf91fc4','20191022_01_d2VAv-make-triggers-in-timeentry-table','apply','ryanjohnson','swegdock.dyn.wpi.edu',NULL,'2019-11-03 22:46:04');
/*!40000 ALTER TABLE `_yoyo_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `_yoyo_migration`
--

DROP TABLE IF EXISTS `_yoyo_migration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `_yoyo_migration` (
  `migration_hash` varchar(64) NOT NULL,
  `migration_id` varchar(255) DEFAULT NULL,
  `applied_at_utc` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`migration_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `_yoyo_migration`
--

LOCK TABLES `_yoyo_migration` WRITE;
/*!40000 ALTER TABLE `_yoyo_migration` DISABLE KEYS */;
INSERT INTO `_yoyo_migration` VALUES ('0c86c5c4f32ee5b5fd0d86f392c6508592190dcae7232ab14b009e2e884fab0f','20190927_02_RPNwN-create-userdatawithrole-view','2019-11-03 22:46:04'),('268da690a4a90e3391985ed5494b8e34e2f93efcdca1342636157b826ac761d7','20191022_01_d2si0-add-opener-to-event','2019-11-03 22:46:04'),('5279c311262a0841d5020158c9f1ec31802891b0c71b29a4aa522901542aff0a','20191021_01_yPkaO-make-end-in-timeentry-nullable','2019-11-03 22:46:04'),('569ac3020a74b5f4ea6d5b02d5d62fe4ebe47a8fc92ea185cdefbade45c6ea37','20190916_02_RbiMa-create-timeEntry','2019-11-03 22:46:04'),('6b298f242d13359cdcdb684d5eef8ecd679b1c792d0b6f03bdc3d8dc21c6fb18','20190927_01_ouV2L-create-userdata-view','2019-11-03 22:46:04'),('7426b4aadb771c5680e817ca14e6dd8b3a870f05ee7050a5e202206f3bf91fc4','20191022_01_d2VAv-make-triggers-in-timeentry-table','2019-11-03 22:46:04'),('7482587cc92cadab3fa0e9aef17c19090a44f7907da769a539f83d9af0126de0','20190916_01_KsWxH-create-UserRoles','2019-11-03 22:46:04'),('7de44c0cf49b01a9914625d6fa674acda705fa46b26ff92c2d70ce601ae8b520','20190917_01_Jttbg-auto-session-expiry-event','2019-11-03 22:46:04'),('81e62d691d3c572b67ceaccfe1c8e993a664c93fde3178c697660abaafed2786','20190913_01_rb2OO-create-users','2019-11-03 22:46:04'),('82fd6bbdf5028e74ba828a3f3874ec4097081ef717a1e9e9f9cf386c0e984f0e','20190916_01_77FxU-drop-user-salt','2019-11-03 22:46:04'),('b865c58fbb83cfa892d02b0b112955e105424f0150832235e181c4d5b97a90f1','20191013_01_z7Cn9-cascade-userroles-delete','2019-11-03 22:46:04'),('b9e12eeaf120ca20ff4d5a3ce9f4686184bec7bfb2f15206b7772e3acd151a3b','20190916_02_CImKu-login-sessions','2019-11-03 22:46:04'),('ba8e6a94debacc0b0edb1e44d911424f4912cbcfe3e4065d92f9753773963cb2','20190913_02_LViZ5-create-events','2019-11-03 22:46:04'),('cfc70e42d1332ba5160fb81e726939aea4e9d6ecd494c964af039d487a2cdb52','20190914_01_FONOP-create-route','2019-11-03 22:46:04'),('ef13d3793f03d0e1f7ce8bb3713b2b625ce16a4c24becc46d4ae29e6cea5e44c','20191014_01_GoMDS-trigger-password-change-logout','2019-11-03 22:46:04'),('f1ac7d0ea81fd707b915c64fb7ea9886a176bc04e9b3b38c9bf352afe5b91844','20190914_02_gA5Xf-create-tournamentparticipants','2019-11-03 22:46:04');
/*!40000 ALTER TABLE `_yoyo_migration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `_yoyo_version`
--

DROP TABLE IF EXISTS `_yoyo_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `_yoyo_version` (
  `version` int(11) NOT NULL,
  `installed_at_utc` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `_yoyo_version`
--

LOCK TABLES `_yoyo_version` WRITE;
/*!40000 ALTER TABLE `_yoyo_version` DISABLE KEYS */;
INSERT INTO `_yoyo_version` VALUES (2,'2019-11-03 22:46:04');
/*!40000 ALTER TABLE `_yoyo_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event` (
  `eventid` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `max_participants` tinyint(3) unsigned DEFAULT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  `actual_start` timestamp NULL DEFAULT NULL,
  `actual_end` timestamp NULL DEFAULT NULL,
  `name` varchar(40) NOT NULL,
  `description` text,
  `cost` tinyint(3) unsigned DEFAULT NULL,
  `paid_members_only` tinyint(1) NOT NULL DEFAULT '1',
  `tournament_result_unit` varchar(10) DEFAULT NULL,
  `tournament_result_ordering` tinyint(1) DEFAULT NULL,
  `opener` smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY (`eventid`),
  KEY `opener_id` (`opener`),
  CONSTRAINT `opener_id` FOREIGN KEY (`opener`) REFERENCES `user` (`userid`) ON DELETE CASCADE,
  CONSTRAINT `event_chk_1` CHECK (((`start` < `end`) and (`actual_start` <= `actual_end`)))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (4,40,'2019-11-07 18:00:00','2019-11-07 22:00:00',NULL,NULL,'Open Cave','',0,1,NULL,NULL,5),(5,40,'2019-11-08 18:00:00','2019-11-08 22:00:00',NULL,NULL,'Free Friday','',0,0,NULL,NULL,4),(6,20,'2019-11-06 08:00:00','2019-11-06 16:00:00',NULL,NULL,'Open Cave','Free',0,1,NULL,NULL,8),(7,25,'2019-11-06 18:00:00','2019-11-06 21:00:00',NULL,NULL,'Open Cave','',0,1,NULL,NULL,5),(8,40,'2019-11-11 18:00:00','2019-11-11 22:00:00',NULL,NULL,'Open Cave','',0,1,NULL,NULL,5),(9,40,'2019-11-12 18:00:00','2019-11-12 22:00:00',NULL,NULL,'Open Cave','',0,1,NULL,NULL,9),(10,20,'2019-11-06 14:20:00','2019-11-06 16:40:00',NULL,NULL,'Speed Competition','This is our monthly competition for all our members.',50,1,'seconds',1,9),(11,50,'2019-11-05 08:00:00','2019-11-05 21:00:00','2019-11-05 16:05:18','2019-11-05 16:05:25','Open Cave','',0,1,NULL,NULL,11),(12,20,'2019-11-05 10:45:00','2019-11-05 12:30:00','2019-11-05 15:48:51','2019-11-05 16:05:18','Difficulty Competition','This is our monthly competition for all our members.',50,1,'points',0,5);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LoginSession`
--

DROP TABLE IF EXISTS `LoginSession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LoginSession` (
  `userid` smallint(5) unsigned NOT NULL,
  `start_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `token` varchar(60) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE KEY `token` (`token`),
  KEY `userid_ind` (`userid`),
  CONSTRAINT `loginsession_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LoginSession`
--

LOCK TABLES `LoginSession` WRITE;
/*!40000 ALTER TABLE `LoginSession` DISABLE KEYS */;
INSERT INTO `LoginSession` VALUES (8,'2019-11-05 16:12:31','e485e37cc7ae8ccde07fbe006518784a1c9006830ad35f31dcc5fc485fb9'),(12,'2019-11-05 15:24:15','7bfecdc9a80851e2c51e23bb5672353e51ef70f4e6ba9048d3d356acef7a'),(13,'2019-11-05 15:58:46','68d9e220409f42c49a6deb19898033fc61439e23ac33b9e62e79837879fc'),(14,'2019-11-05 15:24:24','ac805464fa2846920de936328e12054a07d2ffb2a8ce80f1581a0386daec');
/*!40000 ALTER TABLE `LoginSession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Route`
--

DROP TABLE IF EXISTS `Route`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Route` (
  `routeid` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `set_by` smallint(5) unsigned NOT NULL,
  `difficulty` tinyint(3) unsigned NOT NULL,
  `picture` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`routeid`),
  KEY `set_by` (`set_by`),
  CONSTRAINT `route_ibfk_1` FOREIGN KEY (`set_by`) REFERENCES `user` (`userid`),
  CONSTRAINT `route_chk_1` CHECK (((17 >= `difficulty`) >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Route`
--

LOCK TABLES `Route` WRITE;
/*!40000 ALTER TABLE `Route` DISABLE KEYS */;
INSERT INTO `Route` VALUES (3,2,7,'IMG_5376.jpeg'),(4,5,5,'IMG_5379.jpeg'),(5,13,4,'IMG_5375.jpeg');
/*!40000 ALTER TABLE `Route` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timeentry`
--

DROP TABLE IF EXISTS `timeentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timeentry` (
  `eventid` smallint(5) unsigned NOT NULL,
  `userid` smallint(5) unsigned NOT NULL,
  `start` timestamp NOT NULL,
  `end` timestamp NULL DEFAULT NULL,
  `total_time` decimal(5,2) GENERATED ALWAYS AS ((timestampdiff(SECOND,`start`,`end`) / 3600)) STORED,
  PRIMARY KEY (`eventid`,`userid`),
  KEY `userid` (`userid`),
  CONSTRAINT `timeentry_ibfk_1` FOREIGN KEY (`eventid`) REFERENCES `event` (`eventid`),
  CONSTRAINT `timeentry_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timeentry`
--

LOCK TABLES `timeentry` WRITE;
/*!40000 ALTER TABLE `timeentry` DISABLE KEYS */;
INSERT INTO `timeentry` (`eventid`, `userid`, `start`, `end`) VALUES (11,1,'2019-11-05 15:47:39','2019-11-05 16:05:25'),(11,2,'2019-11-05 15:47:56','2019-11-05 16:05:25'),(11,6,'2019-11-05 15:48:08','2019-11-05 16:05:25'),(11,7,'2019-11-05 15:48:39','2019-11-05 16:05:25'),(11,9,'2019-11-05 15:48:16','2019-11-05 16:05:25'),(11,11,'2019-11-05 15:59:20','2019-11-05 16:05:25'),(11,13,'2019-11-05 15:52:56','2019-11-05 16:05:25'),(12,6,'2019-11-05 15:47:42','2019-11-05 16:05:25'),(12,8,'2019-11-05 15:47:47','2019-11-05 16:05:18'),(12,9,'2019-11-05 15:47:53','2019-11-05 16:05:25'),(12,10,'2019-11-05 15:48:00','2019-11-05 16:05:18');
/*!40000 ALTER TABLE `timeentry` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`cs542`@`localhost`*/ /*!50003 TRIGGER `trig_timeentry` BEFORE INSERT ON `timeentry` FOR EACH ROW BEGIN 
	declare boo INT;
    declare boo1 INT;
    declare boo2 INT;
    declare boo3 INT;
    declare boo4 INT;
    SELECT paid into boo FROM User U WHERE userid = new.userid;
	SELECT paid_members_only into boo1 FROM event where eventid = new.eventid;  
    SELECT waiver into boo2 FROM user where userid = new.userid;
	SELECT max_participants into boo3 FROM event WHERE eventid = new.eventid;
    SELECT count(*) into boo4 FROM timeentry where eventid = new.eventid AND end is null;
    IF boo4 >= boo3 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because the event has reached the maximum number of participants';
    END IF;

    IF boo = 0 and boo1 = 0 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because waiver has not been signed';
    END IF;
    IF boo = 0 and boo1 = 1 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because membership has not been paid and waiver has not been signed';		    
    END IF;
    IF boo = 1 and boo1 = 0 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because waiver has not been signed';
    END IF;
    IF boo = 1 and boo1 = 1 and boo2 =0 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because waiver has not been signed';
    END IF;
    IF boo = 0 and boo1 = 1 and boo2 =1 THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Cannot checkin, because membership has not been paid';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `TournamentParticipants`
--

DROP TABLE IF EXISTS `TournamentParticipants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TournamentParticipants` (
  `eventid` smallint(5) unsigned NOT NULL,
  `userid` smallint(5) unsigned NOT NULL,
  `score` double DEFAULT NULL,
  PRIMARY KEY (`eventid`,`userid`),
  KEY `userid` (`userid`),
  CONSTRAINT `tournamentparticipants_ibfk_1` FOREIGN KEY (`eventid`) REFERENCES `event` (`eventid`),
  CONSTRAINT `tournamentparticipants_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TournamentParticipants`
--

LOCK TABLES `TournamentParticipants` WRITE;
/*!40000 ALTER TABLE `TournamentParticipants` DISABLE KEYS */;
INSERT INTO `TournamentParticipants` VALUES (12,6,7),(12,8,5),(12,9,5),(12,10,4);
/*!40000 ALTER TABLE `TournamentParticipants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `userid` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `student_id` varchar(128) DEFAULT NULL,
  `student_name` varchar(30) NOT NULL,
  `join_date` date NOT NULL,
  `paid` tinyint(1) NOT NULL DEFAULT '0',
  `waiver` tinyint(1) NOT NULL DEFAULT '0',
  `cpr_certified` tinyint(1) NOT NULL DEFAULT '0',
  `password_hash` varchar(60) NOT NULL,
  `pe_credit` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`userid`),
  UNIQUE KEY `student_id` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'0c4a111e786523432df12b8e6735a8d29f2da93dab0d9b04c17db5c32c18f61353594e15865a92024ad46e8dcf486a8056c3067b372ea621983d57eee9953ccc','Cameron Mason','2019-09-27',1,1,0,'$2b$12$eJqw1u5rQegvkDrLVPLEEeFucMdv/qEDfVOWPg.GtMGXVO38Ng7bW',1),(2,'eb4ee16eb982f6dd94c79dc3c391cce84fba54dbc51547f98adef2d680b9a6f1f9f5ffa42272177e5399de498f3f9d3bc9fc08287c4b86813afd5068ef3b9f34','Aidan Roberts','2019-09-27',1,1,0,'$2b$12$DhQ6rVy65f.RuGsaQCgEoOaIv0VxjxAHo.qMTpHXgIvg65Zz0nRi6',1),(3,'efcee89e2a1f29efdcfb24520ef21904d97678714b5616e78f55004e6dfd80307de30381fc5e6169f8f3f0d955c2dc281b20247669cfa00b354327bbb3abdecd','Bradley Perry','2019-09-27',1,1,0,'$2b$12$5ZRYoGvupAQy7gszQEK3qeg5C7eVlkimhJPzJGyh.SCHeSlsFIfoa',1),(4,'5615033fce8161129ee3b56260734b42b1d71c8428e452dfdca3a914f65f8cb9563020d54c472bfca682eac7d747b32f1438f6fb864fc1347824fcb4d27b03ea','Mason Butler','2019-09-27',1,1,0,'$2b$12$cfbnvY39bXcNljASqS.yxuJoEyNhntUckW8mDgraqoySHljZNQT2C',1),(5,'65743292cd9c8f56013d9a0d868adc5768c0b60f0f9079d819a3859ee5962f95fb6e113e4beac030c67ae4405b7b37956f6940512523e568b4e88b86eace2d37','Jayden Sun','2019-09-27',1,1,0,'$2b$12$AoFv5YNfCJDo0J.Uq04i5OmnAZcWSG3k9VuUpNUDOeTtdr079eLyW',1),(6,'7f448384bfbce34619ef2186841df9071d190763a5d4ac61d871d9180cb7e2541ab021ee7afa8626472af573d47ce6cc63d3e508937de446cb2123c80b86c101','Heidi Ball','2019-09-27',0,1,0,'$2b$12$MDEbwaFgXqFUM4nrnnrUcebtJwc3Jgml1iAlZu6iGZ6DDHWqlQNgS',1),(7,'c072002400695b4433afa9adc5be6e985ef1673b41bc6a646f5b7e8bcbc6cf96da266a5b8b47324b54c955027f3f1c86d1e16694c27ca7f512aa75801abd605f','Morgan Matthews','2019-09-27',1,0,0,'$2b$12$QBNG4z1ZRklvxK7oFcV/XOQVq7/8BRk6KpfWsdy/u2RXsdVgPqEbe',0),(8,'2dc8efe75ce7bac9999807451cafc521fb384721c3ea5f7e1a2f2e1c53413a25b5e96edced2935ab698f670c6d9608e6e121950b827d95fc9aefe24fdf120eae','Isabel Hall','2019-09-27',1,1,0,'$2b$12$X89adXhckeMO6/G5uN.qvua5o9eTmyr6juq4JXTgRqy7BS8MB0.cG',0),(9,'b4f9816b89929123f31b4d6c160c9cdfa44c0c5ab1ce09a4640adf19ee8148da339673c1d29c92337fdb35db8d4137af79c8659f449e2601d4ae766fb350fd42','Elsie Wilkinson','2019-09-27',1,1,0,'$2b$12$LQIpyEihtI7NFp.zACnv1.JXVV8woQn1lcm3IRdE6TaBcFObKyBla',0),(10,'082c0f067c196c9006ac0f9bee423b78434822dd1aaa695267409db8b26e9c5490d9062fc7defe08bd0185d2978067c0984985799a5d3bdf3b8a93687aab48a0','Bethany Ross','2019-09-27',1,1,0,'$2b$12$GfE/NtKaHNzBn4sICgeFKux8Aq2.T3cOEA98Qx1TnQk50cO9hWVdu',0),(11,'f1ecb37cc45de7b5e816917b042f258e37bd81e95a4352723c172d20095418d82e3c05838912b8801f4f0d215969c0188509868f26735eddc5293880ef0a4c06','Ryan','2019-11-05',1,1,0,'$2b$12$TsVeauCNpq29FD6SAcfXU.yfXoI/47OZqLhLOWbToTFzxZj1iJvHq',0),(12,'4635d697eb36874d335a79538948c6eb057f291d3ab736b5554a15916445a2023451b767943e78de1dea3ea17244f28416ed185bb1b261d62d7cbc0ce96740f6','Yu Zhai','2019-11-05',1,1,0,'$2b$12$xUEDGiYywpfLBwfcUSI5z./xtxQeEc/sCmidC4SGdlAtJsRh.0PIG',0),(13,'a28fe5d42d93c05ae710168af729d3a3eeffca6aab3594745169ccdbe86fe0c72ead4e877f5f86e7473a34a2229f9320cb6307ebd5239d0c3c9c1091c25bec7c','Bill','2019-11-05',1,1,0,'$2b$12$1fbAXzzRnzLBCNG.61argeFdEREQNfP7d/MeO57jgHS2hc.jTqy/C',1),(14,'fdb463ad0ccfd8acabf170b1ec8787318c75f1564e16b0418e89fecf9f27c4b5df978c335584bb51c2a813992dcfcc3336324c02c21d5928748483cf576c5d86','manyang','2019-11-05',1,1,0,'$2b$12$yskm6WUKTvUKuBPQ4iZwYeQtz5vbHNRe3y9OY.eoiUrxb4h50grX2',0);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`cs542`@`localhost`*/ /*!50003 TRIGGER `logout_upon_password_change` AFTER UPDATE ON `user` FOR EACH ROW BEGIN
	IF NOT (NEW.password_hash <=> OLD.password_hash) THEN
		DELETE FROM LoginSession WHERE userid=NEW.userid;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary table structure for view `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!50001 DROP VIEW IF EXISTS `userdata`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `userdata` AS SELECT 
 1 AS `userid`,
 1 AS `student_name`,
 1 AS `join_date`,
 1 AS `paid`,
 1 AS `waiver`,
 1 AS `cpr_certified`,
 1 AS `pe_credit`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `userdatawithrole`
--

DROP TABLE IF EXISTS `userdatawithrole`;
/*!50001 DROP VIEW IF EXISTS `userdatawithrole`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `userdatawithrole` AS SELECT 
 1 AS `userid`,
 1 AS `student_name`,
 1 AS `join_date`,
 1 AS `paid`,
 1 AS `waiver`,
 1 AS `cpr_certified`,
 1 AS `pe_credit`,
 1 AS `roles`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `UserRoles`
--

DROP TABLE IF EXISTS `UserRoles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserRoles` (
  `userid` smallint(5) unsigned NOT NULL,
  `role` varchar(6) NOT NULL,
  KEY `UserRoles_fk_userid` (`userid`),
  CONSTRAINT `UserRoles_fk_userid` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`) ON DELETE CASCADE,
  CONSTRAINT `userroles_chk_1` CHECK ((`role` in (_utf8mb4'admin',_utf8mb4'setter',_utf8mb4'opener')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserRoles`
--

LOCK TABLES `UserRoles` WRITE;
/*!40000 ALTER TABLE `UserRoles` DISABLE KEYS */;
INSERT INTO `UserRoles` VALUES (11,'admin'),(12,'admin'),(13,'admin'),(14,'admin'),(1,'admin'),(2,'setter'),(13,'setter'),(4,'opener'),(5,'opener'),(9,'opener'),(5,'setter'),(11,'opener'),(13,'opener'),(8,'opener');
/*!40000 ALTER TABLE `UserRoles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yoyo_lock`
--

DROP TABLE IF EXISTS `yoyo_lock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yoyo_lock` (
  `locked` int(11) NOT NULL DEFAULT '1',
  `ctime` timestamp NULL DEFAULT NULL,
  `pid` int(11) NOT NULL,
  PRIMARY KEY (`locked`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yoyo_lock`
--

LOCK TABLES `yoyo_lock` WRITE;
/*!40000 ALTER TABLE `yoyo_lock` DISABLE KEYS */;
/*!40000 ALTER TABLE `yoyo_lock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `userdata`
--

/*!50001 DROP VIEW IF EXISTS `userdata`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`cs542`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `userdata` AS select `user`.`userid` AS `userid`,`user`.`student_name` AS `student_name`,`user`.`join_date` AS `join_date`,`user`.`paid` AS `paid`,`user`.`waiver` AS `waiver`,`user`.`cpr_certified` AS `cpr_certified`,`user`.`pe_credit` AS `pe_credit` from `user` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `userdatawithrole`
--

/*!50001 DROP VIEW IF EXISTS `userdatawithrole`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`cs542`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `userdatawithrole` AS select `u`.`userid` AS `userid`,`u`.`student_name` AS `student_name`,`u`.`join_date` AS `join_date`,`u`.`paid` AS `paid`,`u`.`waiver` AS `waiver`,`u`.`cpr_certified` AS `cpr_certified`,`u`.`pe_credit` AS `pe_credit`,ifnull(group_concat(`R`.`role` separator ', '),'') AS `roles` from (`userdata` `U` left join `userroles` `R` on((`u`.`userid` = `R`.`userid`))) group by `u`.`userid` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-05 11:24:01
