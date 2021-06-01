#!/bin/bash

a="hello/usr/src/local/share/src/kyo/src/bin"

echo "a = $a"
echo '$a + "kyo" = '"${a}kyo"

echo "length(a) = ${#a}"

echo "a[4] = ${a:4:1}"

echo "a[4:3] = ${a:4:3}"

echo "----------------------------------"
echo "a = $a"
echo '${a%/*} = '${a%/*}
echo '${a%%/*} = '${a%%/*}
echo '${a#*/} = '${a#*/}
echo '${a##*/} = '${a##*/}


echo 'replace = '${a/src/SRC}
echo 'replace all = '${a//src/SRC}

b=${c-BBBB}
c=$(ls /etc/)

echo "c = $c, b = $b"

# -----------------------------------------------------------------------------
#截取IP地址
export LANG=en_US.UTF-8
export LANGUAGE=en_US:en_US:en
ip=$(ifconfig)
ip=${ip#*inet addr:}
echo "#${ip%%  Bcast:*}#"


