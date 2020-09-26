#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 
# @Time    : 2020-09-26 21:45:17
# @Author  : Lydia
# @Site    : 
# @File    : frenchdech.py.py
# @Software: PyCharm

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])  # 构建少数属性但是没有方法的对象


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]
