#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def f(a, L=[]):
    '''
    Default argument value is mutable
    默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。
    '''
    L.append(a)
    return L


if __name__ == '__main__':
    print(f(1))
    print(f(2))
    print(f(3))
