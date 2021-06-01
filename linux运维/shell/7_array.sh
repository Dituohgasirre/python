#!/bin/bash

# 定义整型变量
declare -i num

num=10
num+=20

echo $num
echo "----------------------"

# 定义常量(不允许修改)
declare -r const=90
echo $const
echo "----------------------"

#------------------------------------------------------------------------------
# 定义索引数组
declare -a a

a=(1 "hello" 33 44 55 4 5)

a+=(7 8 9)
a+=(10)

a[100]=999
echo "a[10] = "${a[10]}
echo "a[100] = "${a[100]}
# echo ${a[0]}
# echo ${a[1]}
# echo ${a[2]}
echo "数据元素个数: "${#a[*]}
# echo ${#a[@]}
# echo ${a[*]}
# echo ${a[@]}


a[0]=100
a[0]+=200

# for i in ${a[*]} ; do
    # echo $i
# done

#删除数组的第一个元素
unset a[0]

# for i in {0..${#a[*]}} ; do       大括号不支持变量解析
len=${#a[*]}
for i in $(seq 0 $[len - 1]) ; do
    echo ${a[$i]}
done

echo "-------------------------"
#------------------------------------------------------------------------------
# 定义key/Value数组
declare -A b

b['name']=kyo
b['sex']='男'
b['data']=${a[*]}


echo ${b[@]}
echo ${!b[@]}
echo ${b["name"]}
echo ${b["sex"]}

