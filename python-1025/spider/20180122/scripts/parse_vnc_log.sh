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
    # fetch time
    #Sat Jul 26 14:24:49 2014
    if grep -qE '^([a-zA-Z]{3} ){2}[0-9]{1,2} ([0-9]{2}:){2}[0-9]{2} [0-9]{4}$'\
		 <<< "$line"
    then
        t=$(grep -E '^([a-zA-Z]{3} ){2}[0-9]{1,2} ([0-9]{2}:){2}[0-9]{2} [0-9]{4}$' \
		 <<< "$line")
    fi

    # fetch ip and port
    # Connections: accepted: 10.1.1.1::51038
    if grep -qE 'Connections: accepted' <<< "$line"; then
        ip=$(awk '{print $NF}' <<< "$line" | awk -F: '{print $1}')
        port=$(awk '{print $NF}' <<< "$line" | awk -F: '{print $NF}')
        echo "${t}, ${ip}, ${port}"
    fi
done < "$file"
