#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 11:43:45
# @Author  : Lydia
# @Site    : 
# @File    : listcomps.py
# @Software: PyCharm
if __name__ == '__main__':
    symbols = '$&^*'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)
