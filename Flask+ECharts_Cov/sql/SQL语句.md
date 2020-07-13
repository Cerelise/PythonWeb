# SQL语句

## history表

CREATE TABLE history (
ds datetime NOT NULL COMMENT '日期',
confirm int(11) DEFAULT NULL COMMENT '累计确诊',
confirm_add int(11) DEFAULT NULL COMMENT '当日新增确诊',
suspect int(11) DEFAULT NULL COMMENT '剩余疑似',
suspect_add int(11) DEFAULT NULL COMMENT '当日新增疑似',
heal int(11) DEFAULT NULL COMMENT '累计治愈',
heal_add int(11) DEFAULT NULL COMMENT '当日新增治愈',
dead int(11) DEFAULT NULL COMMENT '累计死亡',
dead_add int(11) DEFAULT NULL COMMENT '当日新增死亡',
PRIMARY KEY (ds) USING BTREE
)ENGINE=InNODB DEFAULT CHARSET=utf8mb4;



## details表

CREATE TABLE details (
id int(11) NOT NULL AUTO_INCREMENT,
update_time datetime DEFAULT NULL COMMENT '数据最后更新时间',
province varchar(50) DEFAULT NULL COMMENT '省',
city varchar(50) DEFAULT NULL COMMENT '市',
confirm int(11) DEFAULT NULL COMMENT '累计确诊',
confirm_add int(11) DEFAULT NULL COMMENT '新增确诊',
heal int(11) DEFAULT NULL COMMENT '累计治愈',
dead int(11) DEFAULT NULL COMMENT '累计死亡',
PRIMARY KEY(id)
)ENGINE =InnoDB DEFAULT CHARSET=utf8mb4;