# encoding: utf-8

__author__ = 'zhangwei'

# 不使用辅助内存
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0
            
        ret = 1
        for i in xrange(3, n):
            if i % 2 == 0:
                continue
            b, j = True, 3
            while j <= (i+2) / 3:
                if i % j == 0:
                    b = False
                    break
                j += 2
            if b:
                ret += 1
        
        return ret


# 使用辅助内存
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False
        ret = 0
        for i in xrange(2, n):
            if primes[i]:
                ret += 1
            for j in xrange(i+i, n):
                primes[j] = False
        return ret


# 使用辅助内存，优化版
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        primes = [False, False] + [True]*(n-2)
        nsqrt = int((n-1)**(0.5))
        for i in xrange(2, nsqrt+1):
            if primes[i]:
                for j in xrange(i**2, n, i):
                    primes[j] = False
        return sum(primes)