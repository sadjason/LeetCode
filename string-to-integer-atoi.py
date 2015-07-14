# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @return an integer
    def atoi(self, str):
        # 1. 忽略所有空白字符
        # 2. 忽略'.'及之后的所以字符
        # 3. 注意正负号

        len_str = len(str)
        firstInvalidCharIndex = -1

         # 寻找第一个有效字符index
        for i in range(0, len_str):
            c = str[i]
            if c == ' ':
                continue
            elif c == '+' or c == '-':
                if i + 1 < len_str:
                    d = str[i+1]
                    if d <= '9' and d >= '0':
                        firstInvalidCharIndex = i
                        break
                    else:
                        return 0
                else:
                    return 0
            elif c <= '9' and c >= '0':
                firstInvalidCharIndex = i
                break
            else:
                return 0

        if firstInvalidCharIndex < 0:
            return  0

        signedHadAppear = False        # 小数点已经出现了
        aMultiplier = 1
        result = 0

        for i in range(firstInvalidCharIndex, len_str)[::-1]:
            c = str[i]
            if c == '+' and not signedHadAppear:
                result = result
                signedHadAppear = True
            elif c == '-' and not signedHadAppear:
                result = 0 - result
                signedHadAppear = True
            elif c >= '0' and c <= '9':
                num = ord(c) - ord('0')
                result += num * aMultiplier
                aMultiplier *= 10
            else:
                # 非法字符
                result = 0
                aMultiplier = 1
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648

        return result