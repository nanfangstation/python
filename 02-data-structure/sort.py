#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 22:14:22
# @Author  : Lydia
# @Site    : 
# @File    : sort.py
# @Software: PyCharm
if __name__ == '__main__':
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(sorted(fruits))
    print(fruits)
    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=len, reverse=True))
    print(fruits.sort())
    print(fruits)