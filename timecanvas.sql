-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 192.168.198.186    Database: timecanvas
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `id` int NOT NULL AUTO_INCREMENT,
  `album_name` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `album_description` text COLLATE utf8mb3_unicode_ci,
  `album_date` datetime NOT NULL,
  `album_type` int DEFAULT NULL,
  `album_owner` varchar(15) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `album_name` (`album_name`),
  KEY `album_owner` (`album_owner`),
  KEY `ix_album_id` (`id`),
  KEY `album_type` (`album_type`),
  CONSTRAINT `album_ibfk_1` FOREIGN KEY (`album_owner`) REFERENCES `user` (`baidu_uk`),
  CONSTRAINT `album_ibfk_2` FOREIGN KEY (`album_type`) REFERENCES `album_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES (1,'小学','我的小学同学','2024-03-09 00:00:00',1,'2867615989'),(2,'高中','我的高中同学','2024-03-09 10:27:55',1,'2867615989'),(3,'初中','我初中同学','2024-03-09 10:28:14',1,'2867615989'),(4,'大学','我的大学同学','2024-03-09 10:28:27',1,'2867615989'),(5,'篮球比赛','高中举行的篮球比赛','2024-03-09 10:29:51',2,'2867615989'),(6,'高中运动会','高中参加的运动会比赛','2024-03-09 10:32:03',2,'2867615989'),(7,'校园歌手','大学参加的校园歌手，很开心','2024-03-09 10:32:39',2,'2867615989'),(9,'爬山','和朋友们一起爬山','2024-04-07 22:16:00',3,'2867615989'),(10,'骑行','和朋友们一起骑行','2024-04-07 22:16:51',3,'2867615989');
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_type`
--

DROP TABLE IF EXISTS `album_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `albumtype_name` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `albumtype_description` text COLLATE utf8mb3_unicode_ci,
  `albumtype_data` datetime NOT NULL,
  `albumtype_owner` varchar(15) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `albumtype_owner` (`albumtype_owner`),
  KEY `ix_album_type_id` (`id`),
  CONSTRAINT `album_type_ibfk_1` FOREIGN KEY (`albumtype_owner`) REFERENCES `user` (`baidu_uk`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_type`
--

LOCK TABLES `album_type` WRITE;
/*!40000 ALTER TABLE `album_type` DISABLE KEYS */;
INSERT INTO `album_type` VALUES (1,'同学录','与同学相关的记录','2024-03-08 00:00:00','2867615989'),(2,'趣事录','一些有趣的活动','2024-03-08 00:00:00','2867615989'),(3,'旅游志','旅游的相册','2024-03-08 00:00:00','2867615989');
/*!40000 ALTER TABLE `album_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('dc8d228c33e7');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classmates`
--

DROP TABLE IF EXISTS `classmates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classmates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `nickname` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `birthday` datetime DEFAULT NULL,
  `hometown` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `hobby` varchar(200) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `qq_number` varchar(20) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `wx_number` varchar(20) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `phone_number` varchar(20) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `constellation` varchar(5) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `dream` varchar(200) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `graduation_message` text COLLATE utf8mb3_unicode_ci,
  `classmates_album_name` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `classmates_avatar_name` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `baidu_uk` varchar(15) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `baidu_uk` (`baidu_uk`),
  KEY `ix_classmates_id` (`id`),
  CONSTRAINT `classmates_ibfk_1` FOREIGN KEY (`baidu_uk`) REFERENCES `user` (`baidu_uk`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classmates`
--

LOCK TABLES `classmates` WRITE;
/*!40000 ALTER TABLE `classmates` DISABLE KEYS */;
INSERT INTO `classmates` VALUES (1,'小明','小聪明','2000-12-13 00:00:00','四川省/成都市/青羊区/ ','阅读，旅行，摄影，绘画，音乐，运动，烹饪，园艺，编程，写作','123456789','12136547896','12136547896','123456789@qq.com','金牛座','我的梦想是成为一名旅行作家，用脚步丈量世界，用文字记录旅途中的点点滴滴。我希望在世界各地留下自己的足迹，感受不同地域的风土人情，体验各种文化的碰撞与融合。我梦想着能够用我的笔触，将那些美丽的风景、动人的故事、深刻的感悟分享给更多的人，让更多的人通过我的文字，感受到这个世界的广阔与美好','在这个阳光明媚的夏日，我们即将告别这所充满回忆的校园，各奔前程。毕业的钟声已经敲响，我们即将踏上新的旅程，但请不要忘记，这里永远是我们共同的家。\n\n离别总是带着一丝不舍，我们曾经一起度过的日日夜夜，那些在图书馆里埋头苦读、在操场上挥洒汗水、在教室里激烈讨论的日子，都将成为我们心中最宝贵的记忆。我们曾一起笑过、哭过、奋斗过，这份深厚的友情和同窗之情，将伴随我们一生。\n\n虽然我们即将各奔东西，但请相信，无论走到哪里，我们的心始终相连。在未来的道路上，或许会有挑战和困难，但请记住，你们拥有无限的力量和潜力，只要保持坚定的信念和不懈的努力，就没有什么是不可能的。\n\n愿你们在未来的旅程中，勇敢地追逐梦想，不断探索和学习，成为自己想成为的人。愿你们的生活充满阳光，事业蒸蒸日上，爱情甜蜜美满，家庭幸福和睦。\n\n请记住，无论何时何地，只要你们需要，我们永远是你们最坚实的后盾，最温暖的依靠。让我们带着这份不舍和祝福，勇敢地迈向未来，去创造属于我们自己的精彩人生。\n','高中','test.png','2867615989'),(2,'小红','红苹果','2000-10-11 00:00:00','四川省/成都市/青羊区/ ','打羽毛球','124536987','15236547854','15236547854','1245369872@qq.com','水瓶座','成为一个歌手','离别是生命中不可避免的旋律，它让友情和记忆更加珍贵。在这一刻，我想对你说：“青山不改，绿水长流。”愿我们的友谊如同这永恒的自然，不论身在何方，都坚韧不拔。前行的路上，让我们携带着对方的祝福与鼓励，勇敢地追寻各自的梦想。再见不是结束，而是另一种形式的相遇。期待在未来的某个日子，我们能带着各自的故事，再次相聚。\n','高中','string.png','2867615989'),(3,'小蓝','蓝莓','1999-08-14 00:00:00','四川省/成都市/锦江区/ ','画画','123456789','13579246810','13579246810','1234567890@qq.com','狮子座','成为一个画家','离别是生命中不可避免的旋律，它让友情和记忆更加珍贵。在这一刻，我想对你说：“青山不改，绿水长流。”愿我们的友谊如同这永恒的自然，不论身在何方，都坚韧不拔。前行的路上，让我们携带着对方的祝福与鼓励，勇敢地追寻各自的梦想。再见不是结束，而是另一种形式的相遇。期待在未来的某个日子，我们能带着各自的故事，再次相聚。\n','高中','string1.png','2867615989'),(4,'小李','草莓','2001-05-19 00:00:00','上海市/市辖区/黄浦区/ ','读书','987654321','2468135790','15474859632','9876543210@qq.com','金牛座','成为一个作家','祝你一切顺利','高中','string2.png','2867615989'),(6,'张三','小张','1998-12-03 00:00:00','上海','打球，编程，阅读','177845963','15145786589','15145786589','177845963@qq.com','金牛座','一名优秀的军人','.最近烦恼的是小小的告别总是让人觉得寂寞，所以打算将那些短暂的相遇和告别的片段一点点的累计起来好好珍惜。 -- 绿川幸 《夏目友人帐》','string','string','2867615989'),(7,'李四','小李','1999-05-12 00:00:00','北京','跑步，摄影，旅游','123456789','12345678900','12345678900','123456789@qq.com','双子座','成为一名专业的摄影师','每一次的离别都是为了更好的重逢。','回忆相册','班级头像','2867615989'),(8,'王五','大王','1997-08-15 00:00:00','广州','游泳，绘画，听音乐','987654321','98765432100','98765432100','987654321@qq.com','狮子座','成为一名著名的画家','愿我们的友谊像星空一样永恒。','青春纪念册','集体照','2867615989'),(9,'赵六','小赵','2000-11-05 00:00:00','深圳','登山，写作，烹饪','111111111','11111111100','11111111100','111111111@qq.com','天蝎座','成为一名畅销书作家','离别不是结束，而是另一种开始。','青春不散场','毕业合影','2867615989'),(10,'钱七','老钱','1996-03-22 00:00:00','杭州','骑行，摄影，园艺','222222222','22222222200','22222222200','222222222@qq.com','白羊座','成为一名环保志愿者','感谢这段时光，让我们共同成长。','青春留影','校园风光','2867615989'),(11,'孙八','小孙','1995-07-09 00:00:00','成都','跳舞，唱歌，看电影','333333333','33333333300','33333333300','333333333@qq.com','射手座','成为一名舞台剧演员','让我们带着梦想，勇敢前行。','青春舞台','剧照集','2867615989'),(12,'周九','周周','1994-10-30 00:00:00','重庆','篮球，编程，旅游','444444444','44444444100','44444444100','444444444@qq.com','天秤座','成为一名软件工程师','感谢这段旅程，让我们相遇相知。','青春纪念','班级合影','2867615989'),(13,'吴十','小吴','1993-02-18 00:00:00','武汉','足球，设计，阅读','555555555','55555555100','55555555100','555555555@qq.com','水瓶座','成为一名平面设计师','青春不老，我们不散。','青春相册','校园生活','2867615989'),(14,'郑十一','小郑','1992-08-07 00:00:00','南京','羽毛球，写作，听音乐','666666666','66666666600','66666666600','666666666@qq.com','处女座','成为一名作家','愿我们的友情如同这些美好的回忆一样，永不褪色。','青春留念','校园风光','2867615989'),(15,'王十二','大王','1991-04-14 00:00:00','西安','跑步，摄影，旅行','777777777','77777777100','77777777100','777777777@qq.com','双鱼座','成为一名旅行家','每一次的离别都是为了更好的相遇。','青春旅行','旅行照片','2867615989'),(16,'冯十三','小冯','1990-11-21 00:00:00','天津','游泳，编程，看电影','888888888','88888888800','88888888800','888888888@qq.com','摩羯座','成为一名电影导演','感谢这段时光，让我们共同成长。','青春电影','电影海报','2867615989'),(17,'陈十四','小陈','1989-09-01 00:00:00','苏州','登山，写作，烹饪','999999999','99999999100','99999999100','999999999@qq.com','巨蟹座','成为一名厨师','离别不是结束，而是另一种开始。','青春美食','美食照片','2867615989'),(18,'张三','肥料','2000-12-05 00:00:00','四川省/成都市/成华区/ ','打球','1748596845','12347854587','12347854587','1748596845@qq.com','金牛座','NBA球星','希望你能考上心仪的大学','高中','string','2867615989'),(19,'张三丰','肥料','2000-12-05 00:00:00','上海市/市辖区/黄浦区/ ','打球','1748596845','12347854587','12347854587','1748596845@qq.com','金牛座','NBA球星','希望你能考上心仪的大学','高中','string','2867615989'),(20,'张三广','肥料','2000-12-05 00:00:00','北京市/市辖区/东城区/ ','打球','1748596845','12347854587','12347854587','1748596845@qq.com','金牛座','NBA球星','希望你能考上心仪的大学','高中','string','2867615989'),(21,'张三里','肥料','2000-12-05 00:00:00','四川省/成都市/锦江区/ ','打球','1748596845','12347854587','12347854587','1748596845@qq.com','金牛座','NBA球星','希望你能考上心仪的大学','高中','string','2867615989'),(22,'张三外','肥料','2000-12-05 00:00:00','四川省/成都市/成华区/ ','打球','1748596845','12347854587','12347854587','1748596845@qq.com','金牛座','NBA球星','希望你能考上心仪的大学','高中','string','2867615989'),(23,'张三穷','肥料','2000-12-05 00:00:00','四川省/成都市/青羊区/ ','打球','1748596845','12347854587','12347854587','1748596845@qq.com','金牛座','NBA球星','希望你能考上心仪的大学','高中','string','2867615989'),(25,'李小四','小四','2000-06-10 00:00:00','四川省/自贡市/自流井区/ ','吃法','987654321','15236547854','15236547854','1245369872@qq.com','金牛座','作家','在这离别的时刻，让我们以诗的形式，表达那份不舍与希望。\n\n风起时，叶随风舞，\n相逢何处，知多少？\n别离的泪，滴在心口，\n化作前行路上的光。\n\n愿每一次挥手，不是终点，\n而是另一段旅程的起点。\n愿你的每一步，都坚定而从容，\n无论天涯，还是咫尺，心始终相连。\n\n记住，每一段离别，都是为了更好的重逢。\n愿你携带着我们的记忆，勇敢地迎接新的挑战，\n直到那一天，我们再次相聚，分享成长的故事。\n\n再见，不是结束，是另一种开始。\n愿你的未来，如星辰般璀璨，如诗篇般温暖。\n','高中','高中','2867615989');
/*!40000 ALTER TABLE `classmates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interesting_event`
--

DROP TABLE IF EXISTS `interesting_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interesting_event` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `event_date` datetime NOT NULL,
  `event_description` text COLLATE utf8mb3_unicode_ci,
  `event_participant` text COLLATE utf8mb3_unicode_ci,
  `event_album_image` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `event_album_name` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `baidu_uk` varchar(15) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `baidu_uk` (`baidu_uk`),
  KEY `ix_interesting_event_id` (`id`),
  CONSTRAINT `interesting_event_ibfk_1` FOREIGN KEY (`baidu_uk`) REFERENCES `user` (`baidu_uk`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interesting_event`
--

LOCK TABLES `interesting_event` WRITE;
/*!40000 ALTER TABLE `interesting_event` DISABLE KEYS */;
INSERT INTO `interesting_event` VALUES (1,'第一届3v3比赛','2024-04-08 00:00:00','','我，小方，小王，小珊，小海','string','篮球比赛','2867615989'),(3,'拔河','2024-04-08 00:00:00','','张伟, 李娜, 王浩, 赵敏, 刘强, 陈静, 杨帆, 吴迪, 孙悦, 周杰, 徐磊, 马云, 朱莉','string','高中运动会','2867615989'),(4,'400米接力','2024-04-08 00:00:00','','张伟, 李娜, 王浩, 赵敏, 刘强, 陈静, 杨帆, 吴迪, 孙悦, 周杰, 徐磊, 马云, 朱莉','string','高中运动会','2867615989'),(5,'1000米跑','2024-04-08 00:00:00','','张伟, 李娜, 王浩, 赵敏, 刘强, 陈静, 杨帆, 吴迪, 孙悦, 周杰, 徐磊, 马云, 朱莉','string','高中运动会','2867615989'),(8,'高中校园篮球友谊赛','2018-10-18 00:00:00','在激动人心的篮球赛场上，每一次跳投、每一次冲刺、每一次精准传球都凝聚着汗水与梦想。球员们的拼搏和团队精神，激励我们无论在何处都要全力以赴，追逐胜利的光芒。\n','张三，李四，王五，赵六，钱七，孙八，周九，吴十，郑十一，王十二，冯十三，陈十四，楚十五，林十六，韩十七，李白','篮球比赛','篮球比赛','2867615989'),(9,'第二届篮球3v3','2017-02-01 00:00:00','有趣的篮球比赛\n','张三，李四，王五，赵六，钱七，孙八，周九，吴十，郑十一，王十二，冯十三，陈十四，楚十五，林十六，韩十七，李白','篮球比赛','篮球比赛','2867615989'),(11,'第三届篮球3v3','2024-04-17 00:00:00','有趣的篮球比赛\n','张三，李四，王五，赵六，钱七，孙八，周九，吴十，郑十一，王十二，冯十三，陈十四，楚十五，林十六，韩十七，李白','篮球比赛','篮球比赛','2867615989'),(12,'大学新生杯','2024-04-03 00:00:00','快乐的新生杯篮球比赛\n','张三，李四，王五，赵六，钱七，孙八，周九，吴十，郑十一，王十二，冯十三，陈十四，楚十五，林十六，韩十七，李白','篮球比赛','篮球比赛','2867615989'),(13,'班级拔河','2024-04-10 00:00:00','拿了第一名的班级拔河比赛\n','张三，李四，王五，赵六，钱七，孙八，周九，吴十，郑十一，王十二，冯十三，陈十四，楚十五，林十六，韩十七，李白','高中运动会','高中运动会','2867615989');
/*!40000 ALTER TABLE `interesting_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travel`
--

DROP TABLE IF EXISTS `travel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `travel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `travel_album_name` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `travel_theme` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `travel_date` datetime NOT NULL,
  `travel_description` text COLLATE utf8mb3_unicode_ci,
  `travel_participant` text COLLATE utf8mb3_unicode_ci,
  `travel_place` varchar(30) COLLATE utf8mb3_unicode_ci NOT NULL,
  `travel_album_image` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `baidu_uk` varchar(15) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `travel_province` varchar(30) COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `baidu_uk` (`baidu_uk`),
  KEY `ix_travel_id` (`id`),
  CONSTRAINT `travel_ibfk_1` FOREIGN KEY (`baidu_uk`) REFERENCES `user` (`baidu_uk`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travel`
--

LOCK TABLES `travel` WRITE;
/*!40000 ALTER TABLE `travel` DISABLE KEYS */;
INSERT INTO `travel` VALUES (1,'爬山','西岭雪山','2024-04-07 00:00:00','快乐的西岭雪山的一天','代大嘴，张三丰，小朋友','西岭',NULL,'2867615989','四川省'),(3,'爬山','川西竹海','2024-04-07 00:00:00','快乐川西竹海的一天','小奕，小陈，小蔡，小王，我','邛崃市竹海',NULL,'2867615989','四川省'),(4,'测试','string','2024-04-08 00:00:00','string','string','string',NULL,'2867615989','string');
/*!40000 ALTER TABLE `travel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `baidu_name` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `avatar_url` varchar(200) COLLATE utf8mb3_unicode_ci NOT NULL,
  `access_token` varchar(500) COLLATE utf8mb3_unicode_ci NOT NULL,
  `baidu_uk` varchar(15) COLLATE utf8mb3_unicode_ci NOT NULL,
  `baidu_vip_type` int NOT NULL,
  `nickname` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `refresh_token` varchar(500) COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`baidu_uk`),
  UNIQUE KEY `ix_user_baidu_name` (`baidu_name`),
  KEY `ix_user_id` (`id`),
  KEY `ix_user_baidu_uk` (`baidu_uk`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'未来hhh可期','https://dss0.bdstatic.com/7Ls0a8Sm1A5BphGlnYG/sys/portrait/item/netdisk.1.d0f67b7f.WQ9jbIe0ZLIt1r5b1t2r0g.jpg','tYKo7k0yX/+DHweKu7ZLyQIYfneTXAYsPplhEWlgcYkeZgB54IKZw4Zpbo64fK24SKwOUwknx09PcRydAzXCD4GINQLFTdXYGBYlg1vzrQVcQ4dOmxkQtB9YpJUg3JQk','2867615989',0,'','mhZ1O8qwjYc2DR/+kOUqUCToDz3iI8DGXZ7MYVEhcyfnyIX31oW9n2wFU+hHIJZMYZkMUUokBk/OxXzRW8M8M81kbrOPytBAM7FVdqXRRHdmmYB5gFiUMGJ+gInP2qLJ');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video`
--

DROP TABLE IF EXISTS `video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `video_name` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `video_date` datetime NOT NULL,
  `video_size` varchar(20) COLLATE utf8mb3_unicode_ci NOT NULL,
  `video_owner` varchar(15) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `video_album` int DEFAULT NULL,
  `video_nickname` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `video_specifc_event` int NOT NULL,
  `video_album_type` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `video_name` (`video_name`),
  KEY `video_owner` (`video_owner`),
  KEY `video_album` (`video_album`),
  KEY `ix_video_id` (`id`),
  KEY `video_album_type` (`video_album_type`),
  CONSTRAINT `video_ibfk_1` FOREIGN KEY (`video_owner`) REFERENCES `user` (`baidu_uk`),
  CONSTRAINT `video_ibfk_3` FOREIGN KEY (`video_album`) REFERENCES `album` (`id`),
  CONSTRAINT `video_ibfk_4` FOREIGN KEY (`video_album_type`) REFERENCES `album_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video`
--

LOCK TABLES `video` WRITE;
/*!40000 ALTER TABLE `video` DISABLE KEYS */;
INSERT INTO `video` VALUES (6,'20240417104024503059_2867615989_sea.mp4','2024-04-17 10:40:25','7.08 MB','2867615989',2,'sea.mp4',1,1),(9,'20240601140550357839_2867615989_student1.mp4','2024-06-01 14:05:51','42.27 MB','2867615989',2,'student1.mp4',1,1),(10,'20240601140550521355_2867615989_student2.mp4','2024-06-01 14:05:51','43.14 MB','2867615989',2,'student2.mp4',1,1);
/*!40000 ALTER TABLE `video` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-07 12:43:08
