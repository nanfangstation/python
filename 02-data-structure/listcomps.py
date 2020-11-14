#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 11:43:45
# @Author  : Lydia
# @Site    : 
# @File    : listcomps.py
# @Software: PyCharm
if __name__ == '__main__':
    # 把字符串变unicode码位
    symbols = '$&^*'
    codes_one = []
    for symbol in symbols:
        codes_one.append(ord(symbol))
    print(codes_one)
    # 列表推导 适用于创建新的列表
    codes_two = [ord(symbol) for symbol in symbols]
    print(codes_two)
