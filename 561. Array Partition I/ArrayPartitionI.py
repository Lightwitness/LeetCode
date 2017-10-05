#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: ArrayPartitionI.py
@time: 2017/10/5 11:52
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])