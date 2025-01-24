/*
 Navicat Premium Dump SQL

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80039 (8.0.39)
 Source Host           : localhost:3306
 Source Schema         : play_music

 Target Server Type    : MySQL
 Target Server Version : 80039 (8.0.39)
 File Encoding         : 65001

 Date: 24/01/2025 12:07:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_list
-- ----------------------------
DROP TABLE IF EXISTS `t_list`;
CREATE TABLE `t_list`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `mid` int NULL DEFAULT NULL,
  `uid` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `mid`(`mid` ASC) USING BTREE,
  INDEX `uid`(`uid` ASC) USING BTREE,
  CONSTRAINT `t_list_ibfk_1` FOREIGN KEY (`mid`) REFERENCES `t_music` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `t_list_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `t_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of t_list
-- ----------------------------
INSERT INTO `t_list` VALUES (5, 1, 2);
INSERT INTO `t_list` VALUES (6, 5, 2);
INSERT INTO `t_list` VALUES (7, 4, 2);
INSERT INTO `t_list` VALUES (11, 2, 2);
INSERT INTO `t_list` VALUES (12, 3, 2);
INSERT INTO `t_list` VALUES (13, 1, 1);
INSERT INTO `t_list` VALUES (14, 2, 1);

-- ----------------------------
-- Table structure for t_music
-- ----------------------------
DROP TABLE IF EXISTS `t_music`;
CREATE TABLE `t_music`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `music_name` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of t_music
-- ----------------------------
INSERT INTO `t_music` VALUES (1, '广州花儿合唱团 - 中国字 中国人', 'D:/KuGou/广州花儿合唱团 - 中国字 中国人.mp3');
INSERT INTO `t_music` VALUES (2, '圈圈点点 - 你是我的好朋友', 'D:/KuGou/圈圈点点 - 你是我的好朋友.mp3');
INSERT INTO `t_music` VALUES (3, '宋小睿 - 学猫叫 (童声版)', 'D:/KuGou/宋小睿 - 学猫叫 (童声版).mp3');
INSERT INTO `t_music` VALUES (4, '萧敬腾 - 给．爱人', 'D:/KuGou/萧敬腾 - 给．爱人.mp3');
INSERT INTO `t_music` VALUES (5, '宋小睿 - 最美的光', 'D:/KuGou/宋小睿 - 最美的光.mp3');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES (1, 'zs', '123');
INSERT INTO `t_user` VALUES (2, 'lisi', '123');

SET FOREIGN_KEY_CHECKS = 1;
