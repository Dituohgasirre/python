#!/usr/bin/env python3

import random
import sys

def bubble(d):
    #  冒泡 相邻两个进行比较, 左值比右值大进行交换
    l = len(d)
    for j in range(l - 1):
        for i in range(l - j - 1):
            if d[i] > d[i + 1]:
                d[i], d[i + 1] = d[i + 1], d[i]

    return d

def select(d):
    #  选择 查找最小值跟第左边元素交换, 在剩余范围内再次查找最小值与第二个元素交换
    l = len(d)
    for j in range(l - 1):
        m = d[j]
        index = j
        for i in range(j + 1, l):
            if d[i] < m:
                m = d[i]
                index = i

        d[j], d[index] = d[index], d[j]

    return d

def insert(d):
    #  已知左边有序, 将当前元素到左边找合适位置插入
    l = len(d)

    for i in range(1, l):
        t = d[i]
        j = i
        while t < d[j - 1] and j > 0:
            d[j] = d[j - 1]
            j -= 1
        d[j] = t

    return d

def rand(l, d=None):
    if d is None:
        d = []

    for i in range(l):
        d.append(random.randint(1, 10000000))

    return d

def main():
    sortType = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    num = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    if sortType == 1:
        d = bubble(rand(num))
    elif sortType == 2:
        d = select(rand(num))
    elif sortType == 3:
        d = insert(rand(num))
    else:
        d = rand(num)
        d.sort()
    #  print(d)


if __name__ == "__main__":
    main()
