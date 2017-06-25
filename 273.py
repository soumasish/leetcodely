"""Created by sgoswami on 4/14/17 as part of leetcode"""
"""Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1"""
"""123 -> \"One Hundred Twenty Three\"
   12345 -> \"Twelve Thousand Three Hundred Forty Five\"
   1234567 -> \"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven\""""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        units = ['', 'One','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen','Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty','Sixty', 'Seventy', 'Eighty', 'Ninety']
        num_str = []
        self.helper(num, num_str, units, tens)
        return ' '.join(num_str)

    def helper(self, num, num_str, units, tens):
        if num < 20:
            num_str.append(units[num])
            return
        if 20 <= num < 100:
            suffix = num//10
            num_str.append(tens[suffix])
            return self.helper(num % 10, num_str, units, tens)
        if 100 <= num < 1000:
            suffix = num//100
            num_str.append(units[suffix])
            num_str.append('Hundred')
            return self.helper(num % 100, num_str, units, tens)
        if 1000 <= num < 20000:
            suffix = num//1000
            num_str.append(units[suffix])
            num_str.append('Thousand')
            return self.helper(num % 1000, num_str, units, tens)
        if 20000 <= num < 100000:
            suffix = num//10000
            num_str.append(tens[suffix])
            return self.helper(num % 1000, num_str, units, tens)
        if 100000 <= num < 1000000:
            suffix = num // 100000
            num_str.append(units[suffix])
            num_str.append('Hundred')
            return self.helper(num % 1000, num_str, units, tens)
        if 1000000 <= num < 1000000000:
            suffix = num//1000000
            num_str.append(units[suffix])
            num_str.append('Million')
            return self.helper(num % 1000000, num_str, units, tens)
        else:
            suffix = num//1000000000
            num_str.append(units[suffix])
            num_str.append('Billion')
            return self.helper(num % 1000000, num_str, units, tens)

if __name__ == '__main__':
    s = Solution()
    print(s.numberToWords(99000))



