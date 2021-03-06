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
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {}
        for k in moves:
            d[k]+=1
        if (d['R']==d['L']&& d['U']==d['D']):
            return true
        else:
            return false