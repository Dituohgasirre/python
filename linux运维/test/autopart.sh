#!/bin/bash

sudo fdisk /dev/sda << EOF
p
d
1
d
2
n



+10G
n
e




n

+20G
p
q
EOF


