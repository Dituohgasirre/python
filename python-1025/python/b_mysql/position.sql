-- Kyo MySQL IDE

/* Kyo MySQL IDE Config
    @Host localhost
    @User root
    @Password 123123
    @Port 3306
    @DataBase ajing
KYO MySQL IDE Config */

SET @@CHARACTER_SET_SERVER = utf8;
SET @@COLLATION_SERVER = utf8_general_ci;

show tables;

select count(*) from j_position;
--  select * from j_position limit 10;
select * from j_position where county_name='南山区' and province_name='广东省';
--  地级市
--  select count(*) from j_position_city;
--  select * from j_position_city limit 10;
--  地级市下一级
--  select count(*) from j_position_county;
--  select * from j_position_county limit 10;
--  省级
--  select count(*) from j_position_provice;
--  select * from j_position_provice;
--  镇 街道办
--  select count(*) from j_position_town;
--  select * from j_position_town limit 100;
--  村 社区
--  select count(*) from j_position_village;
--  select * from j_position_village limit 10;

