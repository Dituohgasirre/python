#!/bin/bash

# 最少16位
# 包含小写字母
# 包含大写字母
# 包含数字
# 包含标点符号

passwd="$1"

# length
if ! grep -qE '.{16,}' <<< "$passwd"; then
    echo "too short" >&2
    exit 1
fi

# lowercase
if ! grep -qE '[a-z]' <<< "$passwd"; then
    echo "lowercase letter is required" >&2
    exit 1
fi

# uppercase
if ! grep -qE '[A-Z]' <<< "$passwd"; then
    echo "uppercase letter is required" >&2
    exit 1
fi

# number
if ! grep -qE '[0-9]' <<< "$passwd"; then
    echo "number is required" >&2
    exit 1
fi

# punctuation
if ! grep -qE '[[:punct:]]' <<< "$passwd"; then
    echo "punctuation is required" >&2
    exit 1
fi

echo "passwd is good"
exit 0
