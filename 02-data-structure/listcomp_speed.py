#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 13:41:58
# @Author  : Lydia
# @Site    : 
# @File    : listcomp_speed.py
# @Software: PyCharm
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))
if __name__ == '__main__':

    clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
    clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
    clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
    clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')