#!/bin/bash

mping() {
    echo 'mping $0: '$0
    echo 'mping $1: '$1
    echo 'mping $#: '$#
    echo 'mping $@: '$@
    echo 'mping $*: '$*
    ping $1 -c 1 &> /dev/null && echo "$1 link ok" || echo "$1 no link"
}

args() {
    local i j k

    i=99
    j="JJJJ"
    k=356.78

    echo 'args $#: '$#
    echo 'args $@: '$@
    echo 'args $*: '$*

    ret="Args Run..."

    echo "args Return String..."

    return 1
}

rec() {
    local n
    n=$1
    test $n -eq 10 && return
    echo $n
    rec $[n + 1]
}

# ret=""

echo 'main $0: '$0
echo 'main $1: '$1
echo 'main $#: '$#
echo 'main $@: '$@
echo 'main $*: '$*
echo '---------------------------------------'
mping 3.3.3.${1:-3}

args "$@" && echo "成功!!" || echo "失败!!"
echo "Ret = "$ret
echo "main ijk: "$i $j $k
# s=$?
# echo $s

s=$(args 1 2 3)
echo $s

rec 1


