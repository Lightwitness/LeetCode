#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: JudgeRouteCircle.py
@time: 2017/10/5 11:18
"""
import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d=collections.Counter(moves)
        if (d['R']==d['L'])and(d['U']==d['D']):
            return True
        else:
            return False