#!/bin/bash

if ls a.txt >& /dev/null
then
    echo "a.txt 存在"
elif ls b.txt >& /dev/null
then
    echo "b.txt 存在"
else
    echo "文件不存在"
fi

read -p "请输入分数: " num

if [ $num -ge 90 ] ; then
    echo "A"
elif [ $num -ge 80 ] ; then
    echo "B"
elif [ $num -ge 70 ] ; then
    echo "C"
else
    echo "D"
fi

if test $num -ge 90 ; then
    echo "A"
elif test $num -ge 80 ; then
    echo "B"
elif test $num -ge 70 ; then
    echo "C"
else
    echo "D"
fi

read -p "请输入[1 - 3]: " n
case "$n" in
    1)
        echo "11111111111111111"
        ;;
    2)
        echo "22222222222222222"
        ;;
    3)
        echo "33333333333333333"
        ;;
    *)
        echo "其它情况..."
        ;;
esac








