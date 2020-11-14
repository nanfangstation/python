#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 21:38:36
# @Author  : Lydia
# @Site    : 
# @File    : slice.py
# @Software: PyCharm
if __name__ == '__main__':
    l = [10, 20, 30, 40, 50, 60]
    print(l[:2])
    print(l[2:])
    s = 'bicycle'
    # s[a, b, c]对s在a,b之间以c为间隔取值，负值意味着反向取值
    print(s[::3])
    print(s[::-1])
    print(s[::-2])