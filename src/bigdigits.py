#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Desc    : 命令行提供一个数值并在控制台中使用"大"的数字打印出来
# @Time    : 2020-08-23 02:26:56
# @Author  : Lydia
# @Site    : 
# @File    : bigdigits.py
# @Software: PyCharm

import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
