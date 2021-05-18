#!/bin/bash

# for line in $(cat /etc/passwd) ; do
    # echo $line
# done

# l=$(wc -l /etc/passwd | cut -d\  -f1)

# echo $l
# for i in $(seq 1 $l) ; do
    # line=$(head -n $i /etc/passwd | tail -n 1)
    # echo $i....$line
# done

# cat -n /etc/passwd | while read line ; do
    # echo $line
# done

while read line ; do
    echo $line
done < <(cat -n /etc/passwd)

