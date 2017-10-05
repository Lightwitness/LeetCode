#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: EncodeAndDecodeTinyURL.py
@time: 2017/10/5 10:45
"""
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        return longUrl


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))