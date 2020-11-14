#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 22:03:22
# @Author  : Lydia
# @Site    : 
# @File    : iadd.py
# @Software: PyCharm
import dis
if __name__ == '__main__':
    t = (1, 2, [30, 40])
    # t[2] += [50, 60]
    dis.dis('s[a] += b')