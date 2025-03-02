-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.7.40 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 导出 tianqi 的数据库结构
DROP DATABASE IF EXISTS `tianqi`;
CREATE DATABASE IF NOT EXISTS `tianqi` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `tianqi`;

-- 导出  表 tianqi.lishiweathers 结构
DROP TABLE IF EXISTS `lishiweathers`;
CREATE TABLE IF NOT EXISTS `lishiweathers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `城市` varchar(255) DEFAULT NULL,
  `日期` date DEFAULT NULL,
  `最高温度` float DEFAULT NULL,
  `最低温度` float DEFAULT NULL,
  `天气` varchar(255) DEFAULT NULL,
  `风向` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129112 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。

-- 导出  表 tianqi.users 结构
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。

-- 导出  表 tianqi.weatherdata 结构
DROP TABLE IF EXISTS `weatherdata`;
CREATE TABLE IF NOT EXISTS `weatherdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `城市` varchar(255) DEFAULT NULL,
  `时间` varchar(255) DEFAULT NULL,
  `温度` float DEFAULT NULL,
  `体感温度` float DEFAULT NULL,
  `天气情况` varchar(255) DEFAULT NULL,
  `风力等级` varchar(255) DEFAULT NULL,
  `湿度` float DEFAULT NULL,
  `能见度` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1043 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。

-- 导出  表 tianqi.weatherdata7 结构
DROP TABLE IF EXISTS `weatherdata7`;
CREATE TABLE IF NOT EXISTS `weatherdata7` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `城市` varchar(255) DEFAULT NULL,
  `观测时间` date DEFAULT NULL,
  `最高温度` float DEFAULT NULL,
  `最低温度` float DEFAULT NULL,
  `白天天气状况` varchar(255) DEFAULT NULL,
  `晚间天气状况` varchar(255) DEFAULT NULL,
  `白天风力` varchar(255) DEFAULT NULL,
  `夜间风力` varchar(255) DEFAULT NULL,
  `降水量` varchar(255) DEFAULT NULL,
  `紫外线` float DEFAULT NULL,
  `湿度` float DEFAULT NULL,
  `能见度` float DEFAULT NULL,
  `云量` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2500 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
