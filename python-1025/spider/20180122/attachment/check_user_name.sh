#!/bin/bash

echo -n "Please enter your name: "
read name

if echo "$name" | grep -qE '^[a-zA-Z]+$'; then
    echo "name is valid"
else
    echo "invalid name!"
fi
