#!/bin/bash

# read
    # $REPLY
# read input
    # $input

# read -p "请输入三个数字: " n1 n2 n3
    # $n1 $n2 $n3

# echo "用户输入的内容是: "$n1 $n2 $n3

# read -n 3 -p "请输入三个字符: " s
# echo
# echo $s

read -p "请输入用户名: " username
read -t 3 -s -p "请输入密码: " passwd
echo
echo "用户名: $username, 密码: $passwd"

