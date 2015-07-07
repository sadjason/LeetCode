# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        # Ⅰ-1，V-5，X-10，L-50，C-100，D-500，M-1000
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        j = 0
        ret = ''
        while num > 0:
            while num < integers[j]:
                j += 1
            ret += romans[j]
            num -= integers[j]
        return ret