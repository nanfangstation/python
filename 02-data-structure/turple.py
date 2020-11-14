#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-11-14 21:16:13
# @Author  : Lydia
# @Site    : 
# @File    : turple.py
# @Software: PyCharm

if __name__ == '__main__':
    lax_coodinates = (33,9425, -118,408056)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567')]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)
    # 元组拆包
    for _, country in traveler_ids:
        print(country)