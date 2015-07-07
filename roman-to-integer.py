# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        # Ⅰ-1，V-5，X-10，L-50，C-100，D-500，M-1000
        # 1、相同的数字连写，所表示的数等于这些数字相加得到的数，如，III = 3；
        # 2、小的数字（限于Ⅰ、X和C）在大的数字的左边，所表示的数等于大数减小数得到的数，如，IV = 4，IX = 9；
        # 3、小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如，VII = 8, XII = 12；
        romans = dict((('I',1), ('V',5), ('X',10), ('L',50), ('C',100), ('D',500), ('M',1000)))
        ret = 0
        for i in xrange(len(s)):
            if i > 0 and romans[s[i]] > romans[s[i-1]]:
                ret -= 2 * romans[s[i-1]]
            ret += romans[s[i]]
        return ret