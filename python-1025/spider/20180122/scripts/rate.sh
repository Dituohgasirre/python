#!/bin/bash

if [ -z "$1" ];then
    echo "Wrong arguments" >&2
    echo "Usage: $(basename $0) <file>" >&2
    exit 1
fi

file=$1
if [ ! -f "$file" ]; then
    echo "$file not exists" >&2
    exit 1
fi

if [ ! -r "$file" ]; then
    echo "$file not readable" >&2
    exit 1
fi

data=$(grep -Eo '\w+' "$file" | sort | uniq -c)
total=$(awk '{s+=$1}END{print s}' <<< "$data")

while read num word
do
    rate=$(bc <<< "scale=3; $num / $total * 100")
    if grep -qE '^\.' <<< "$rate"; then
        rate="0${rate}"
    fi
    echo "${rate}%  $word"
done <<< "$data"
