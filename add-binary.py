# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        carry = '0'
        n1, n2 = len(a), len(b)
        ret = ''
        
        for i in xrange(max(n1, n2)):
            if i < n1 and i < n2:
                t1, t2 = a[n1-1-i], b[n2-1-i]
                if t1 == '1' and t2 == '1' and carry == '1':
                    ret, carry = '1' + ret, '1'
                elif t1 == '1' and t2 == '1' and carry == '0':
                    ret, carry = '0' + ret, '1'
                elif t1 == '1' and t2 == '0' and carry == '1':
                    ret, carry = '0' + ret, '1'
                elif t1 == '0' and t2 == '1' and carry == '1':
                    ret, carry = '0' + ret, '1'
                elif t1 == '0' and t2 == '0' and carry == '1':
                    ret, carry = '1' + ret, '0'
                elif t1 == '0' and t2 == '1' and carry == '0':
                    ret, carry = '1' + ret, '0'
                elif t1 == '1' and t2 == '0' and carry == '0':
                    ret, carry = '1' + ret, '0'
                elif t1 == '0' and t2 == '0' and carry == '0':
                    ret, carry = '0' + ret, '0'
            else:
                t = None
                if i < n1:
                    t = a[n1-1-i]
                else:
                    t = b[n2-1-i]
                if t == '1' and carry == '1':
                    ret, carry = '0' + ret, '1'
                elif t == '1' and carry == '0':
                    ret, carry = '1' + ret, '0'
                elif t == '0' and carry == '1':
                    ret, carry = '1' + ret, '0'
                else:
                    ret, carry = '0' + ret, '0'
        if carry == '1':
            ret = '1' + ret
        return ret