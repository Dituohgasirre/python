--  学校管理平台

--  设置MySQL服务器字符编码的全局变量
SET @@character_set_server = utf8;
SET @@collation_server = utf8_general_ci;

--  创建学校管理系统的数据库
DROP DATABASE IF EXISTS oa;
CREATE DATABASE oa;

--  切换数据库
USE oa;

--  学校信息表
CREATE TABLE school (
    id int PRIMARY KEY AUTO_INCREMENT,
    state tinyint DEFAULT 0 COMMENT '记录状态',
    name varchar(64) NOT NULL COMMENT '学校名称',
    description text COMMENT '学校简介',
    location text NOT NULL COMMENT '学校位置',
    remark longtext COMMENT '学校备注',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '学校信息表';


--  员工信息表
CREATE TABLE teacher (
    id int PRIMARY KEY AUTO_INCREMENT,
    state tinyint DEFAULT 0 COMMENT '记录状态',
    sid int NOT NULL COMMENT '所属学校ID',
    name varchar(64) NOT NULL COMMENT '员工名字',
    gender tinyint NOT NULL COMMENT '性别',
    remark longtext COMMENT '员工备注',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '员工信息表';

--  课程信息表
CREATE TABLE course (
    id int PRIMARY KEY AUTO_INCREMENT,
    state tinyint DEFAULT 0 COMMENT '记录状态',
    sid int NOT NULL COMMENT '所属学校ID',
    name varchar(64) NOT NULL COMMENT '课程名字',
    remark longtext COMMENT '课程备注',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '课程信息表';


--  教师与课程的关系表
CREATE TABLE t_to_c (
    id int PRIMARY KEY AUTO_INCREMENT,
    sid int NOT NULL COMMENT '所属学校ID',
    tid int NOT NULL COMMENT '教师员工ID',
    cid int NOT NULL COMMENT '课程ID',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '教师与课程的关系';

--  班级信息表
CREATE TABLE class (
    id int PRIMARY KEY AUTO_INCREMENT,
    state tinyint DEFAULT 0 COMMENT '记录状态',
    sid int NOT NULL COMMENT '所属学校ID',
    name varchar(255) NOT NULL COMMENT '班级名字',
    remark longtext COMMENT '班级备注',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '班级信息表';

--  班级与课程 教师的关系表
CREATE TABLE c_to_tc (
    id int PRIMARY KEY AUTO_INCREMENT,
    tid int NOT NULL COMMENT '教师和课程关系表ID',
    cid int NOT NULL COMMENT '班级ID',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '班级与课程 教师的关系表';


--  学生信息表
CREATE TABLE student (
    id int PRIMARY KEY AUTO_INCREMENT,
    state tinyint DEFAULT 0 COMMENT '记录状态',
    sid int NOT NULL COMMENT '所属学校ID',
    cid int NOT NULL COMMENT '所属班级ID',
    name varchar(255) NOT NULL COMMENT '姓名',
    gender tinyint NOT NULL COMMENT '性别',
    phone char(16) NOT NULL COMMENT '联系电话',
    remark longtext COMMENT '学生备注',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '学生信息表';

--  学生和课程关系表
CREATE TABLE choose (
    id int PRIMARY KEY AUTO_INCREMENT,
    state tinyint DEFAULT 0 COMMENT '记录状态',
    cid int NOT NULL COMMENT '课程ID',
    sid int NOT NULL COMMENT '学生ID',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间',
    update_time timestamp NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间'
) COMMENT '学生和课程关系表';


--  成绩信息表
CREATE TABLE score (
    id int PRIMARY KEY AUTO_INCREMENT,
    state tinyint DEFAULT 0 COMMENT '记录状态',
    cid int NOT NULL COMMENT '学生和课程关系ID',
    score decimal(5, 2) NOT NULL COMMENT '分数',
    remark longtext COMMENT '成绩备注',
    md5sum varchar(64) NOT NULL COMMENT '记录校验和',
    addtime timestamp default current_timestamp COMMENT '添加时间'
) COMMENT '成绩信息表';


