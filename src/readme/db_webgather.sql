/*
Navicat MySQL Data Transfer

Source Server         : mysql-localhost
Source Server Version : 50162
Source Host           : localhost:3306
Source Database       : db_webgather

Target Server Type    : MYSQL
Target Server Version : 50162
File Encoding         : 65001

Date: 2014-09-15 19:02:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for wg_job
-- ----------------------------
DROP TABLE IF EXISTS `wg_job`;
CREATE TABLE `wg_job` (
  `job_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(256) DEFAULT NULL,
  `job_flag` varchar(256) DEFAULT NULL,
  `get_rules` text,
  `searchwords` varchar(256) DEFAULT NULL,
  `searchbase` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of wg_job
-- ----------------------------
INSERT INTO `wg_job` VALUES ('5', 'ç§‘å­¦æ¾é¼ ä¼š-åŽŸåˆ›', '2', '(lp0\r\n(dp1\r\nS\'loopUrl\'\r\np2\r\n(lp3\r\nS\'${nextPageUrl1}\'\r\np4\r\nasS\'encoding\'\r\np5\r\nS\'UTF-8\'\r\np6\r\nsS\'url\'\r\np7\r\n(lp8\r\nS\'http://songshuhui.net/archives/tag/%E5%8E%9F%E5%88%9B\'\r\np9\r\nasS\'regexps\'\r\np10\r\n(lp11\r\n(dp12\r\nS\'unique\'\r\np13\r\nS\'1\'\r\np14\r\nsS\'exp\'\r\np15\r\n(lp16\r\nS\'<a class=\"nextpostslink\" href=\"([^\"]*)\"[^>]*>[^<]*</a>\'\r\np17\r\nasS\'str\'\r\np18\r\nS\'nextPageUrl\'\r\np19\r\nsasS\'job_description\'\r\np20\r\nS\'\\xe7\\xa7\\x91\\xe5\\xad\\xa6\\xe6\\x9d\\xbe\\xe9\\xbc\\xa0\\xe4\\xbc\\x9a-\\xe5\\x8e\\x9f\\xe5\\x88\\x9b\\xe5\\x88\\x97\\xe8\\xa1\\xa8\'\r\np21\r\nsS\'needLoop\'\r\np22\r\ng14\r\nsS\'getblocks\'\r\np23\r\n(dp24\r\nS\'end_str\'\r\np25\r\nS\'</html>\'\r\np26\r\nsS\'start_str\'\r\np27\r\nS\'<html>\'\r\np28\r\nsS\'cnt_str\'\r\np29\r\nS\'comblock\'\r\np30\r\nssa(dp31\r\ng2\r\n(lp32\r\nsg5\r\ng6\r\nsg7\r\n(lp33\r\nS\'inline:///${comblock}\'\r\np34\r\nasg10\r\n(lp35\r\n(dp36\r\ng13\r\nS\'0\'\r\np37\r\nsg15\r\n(lp38\r\nS\'<h3 class=\"storytitle\"><a class=\"black\" href=\"([^\"]*)\"[^>]*>([^<]*)</a></h3>\'\r\np39\r\nasg18\r\nS\'title\'\r\np40\r\nsasg20\r\nS\'\\xe7\\xa7\\x91\\xe5\\xad\\xa6\\xe6\\x9d\\xbe\\xe9\\xbc\\xa0\\xe4\\xbc\\x9a-\\xe5\\x8e\\x9f\\xe5\\x88\\x9b\\xe6\\xa0\\x87\\xe9\\xa2\\x98\\xe9\\x93\\xbe\\xe6\\x8e\\xa5\'\r\np41\r\nsg22\r\ng37\r\nsa(dp42\r\nS\'endflag\'\r\np43\r\ng14\r\nsS\'outputkeys\'\r\np44\r\n(lp45\r\nS\'title1\'\r\np46\r\naS\'title2\'\r\np47\r\nasa.', '', 'æ–‡ç« æ ‡é¢˜');

-- ----------------------------
-- Table structure for wg_scan
-- ----------------------------
DROP TABLE IF EXISTS `wg_scan`;
CREATE TABLE `wg_scan` (
  `scan_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `job_id` bigint(20) DEFAULT NULL,
  `scan_start` varchar(256) DEFAULT NULL,
  `scan_end` varchar(256) DEFAULT NULL,
  `scan_flag` varchar(256) DEFAULT NULL,
  `isfinish` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`scan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of wg_scan
-- ----------------------------
INSERT INTO `wg_scan` VALUES ('1', '5', '2014-09-15 16:37:40', null, '2', '0');
INSERT INTO `wg_scan` VALUES ('2', '5', '2014-09-15 16:50:50', null, '2', '0');
INSERT INTO `wg_scan` VALUES ('3', '421', '2014-09-15 17:02:14', null, '2', '0');
INSERT INTO `wg_scan` VALUES ('4', '421', '2014-09-15 17:03:11', null, '2', '0');
INSERT INTO `wg_scan` VALUES ('5', '421', '2014-09-15 17:08:46', null, '2', '0');
INSERT INTO `wg_scan` VALUES ('6', '5', '2014-09-15 17:09:14', null, '2', '0');
INSERT INTO `wg_scan` VALUES ('7', '5', '2014-09-15 17:34:11', null, '2', '0');
INSERT INTO `wg_scan` VALUES ('12', '5', '2014-09-15 18:57:59', '2014-09-15 19:00:19', '0', '1');
