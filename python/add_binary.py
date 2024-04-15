"""Created by sgoswami on 7/3/17."""
"""Given two binary strings, return their sum (also a binary string).
For example,
a = \"11\"
b = \"1\"
Return \"100\"."""


class Solution(object):
    def addBinary(self, a: str, b: str)-> str:
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)

        result = ""
        carry = 0
        for i in range(max_length - 1, -1, -1):
            ones = (a[i] == '1') + (b[i] == '1') + (carry == '1')

            if ones == 0:
                result = '0' + result
                carry = '0'
            elif ones == 1:
                result = '1' + result
                carry = '0'
            elif ones == 2:
                result = '0' + result
                carry = '1'
            else:
                result = '1' + result
                carry = '1'
        if carry == '1':
            result = '1' + result
        return result




