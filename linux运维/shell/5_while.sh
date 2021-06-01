#!/bin/bash

# n=0
# while test $n -le 10 ; do
    # echo "$n"
    # let n++
    # # break
    # # continue
# done

# for i in 1 2 3 4 5 6 7 8 9 10 ; do
    # echo $i
# done

# for i in {10..1..2} ; do
    # echo $i
# done

for i in ls /etc/*.conf ; do
    echo $i
done

for ((i = 0; i < 10; i++)) ; do
    echo $i
done

# while ! ls a.txt >& /dev/null ; do
# while ! test -e a.txt ; do
    # echo "while..."$n
    # let n++
    # sleep 0.1
# done
