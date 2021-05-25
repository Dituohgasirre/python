/*
KYO_HEADER {
    HOST = localhost
    PORT = 3306
    USER = root
    PASSWD = 123123
    DATABASE = company
}
*/

use company;

--  select dept.deptname, sum(sal) as total from emp, dept where emp.deptno=dept.deptno group by dept.deptname having total >= 20000 order by total limit 1;

            --  select
                --  e.empno '工号',
                --  e.ename '姓名',
                --  case e.sex when 'm' then '男' else '女' end '性别',
                --  e.birthday '生日',
                --  e.hiredate '入职日期',
                --  e.sal '工资',
                --  d.deptname '部门名称',
                --  m.ename '上级领导'
            --  from
                --  emp e, emp m, dept d
            --  where
                --  m.empno=e.managerno and m.deptno=d.deptno;

        --  查找部门人数大于2的部门号 部门名称和人数
            select
                e.deptno, d.deptname, count(*) as total
            from
                emp e, dept d
            where
                e.deptno=d.deptno
            group by
                d.deptname, e.deptno
            having
                total > 2;

--  update emp set deptno=2, sal=sal+1000,
    --  managerno=(
        --  select
            --  e.empno
        --  from
            --  (select empno from emp where deptno=2) e,
            --  (select distinct managerno from emp where deptno=2) m
        --  where
            --  e.empno=m.managerno)
--  where ename='mark';

show databases;
