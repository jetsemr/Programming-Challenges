# Author: Jet Semrick
# Date: 12-22-2022
# Problem: Given two binary strings a and b, return their sum as a binary string.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]

a = input("Enter a binary string: ")
b = input("Enter a binary string: ")

solution = Solution()
print("Result:", solution.addBinary(a,b))