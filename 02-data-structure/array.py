#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 22:36:46
# @Author  : Lydia
# @Site    : 
# @File    : array.py
# @Software: PyCharm
from array import array
from random import random
if __name__ == '__main__':
    a = array('d', (random() for i in range(10**7)))
    print(a[-1])

