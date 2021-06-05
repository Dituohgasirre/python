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


while read line
do
    # fetch ip
    #lease 10.1.1.42 {
    if grep -qE ' (([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]) ' <<< "$line"; then
        ip=$(grep -Eo '(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])' <<< "$line")
    fi

    # fetch mac
    #  hardware ethernet e0:05:c5:ee:fa:c9;
    if grep -qE 'ethernet ([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}' <<< "$line"; then
        mac=$(grep -Eo '([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}' <<< "$line")
        echo "${ip} ${mac}"
    fi
done < "$file"
