#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: ArrayPartitionI_WrongAR.py
@time: 2017/10/5 11:56
"""

#错误原因：超时，由于使用插入排序，所以时间过长，并且循环过多影响程序
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for j in range(1,len(nums)):
            key = nums[j]
            i = j-1
            #向前查找比key小的元素
            while i >= 0 and nums[i] > key:
                nums[i+1] = nums[i]
                i = i -1
            nums[i+1] = key
        sum = 0
        for  i in range(0,len(nums),2):
            sum += nums[i]
        return sum



