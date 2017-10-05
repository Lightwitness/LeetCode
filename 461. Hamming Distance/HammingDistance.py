#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: HammingDistance.py
@time: 2017/10/5 10:53
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y