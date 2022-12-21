# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        # solution: use a hashmap to store the last appearance of a character
        # and use that to partition a string.

        # base case when string is one character
        if (len(s) == 1):
            return [1]
        
        # dictionary to store last index
        lastIndex = {}

        # populate index
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        # initialize variables
        partitions = []
        start = 0
        end = 0

        # iterate through the string
        for i in range(len(s)):
            # store the highest bound to a substring
            end = max(end, lastIndex[s[i]])

            # if we reach the "end" bound that means there are no characters 
            # before it that are repeated after
            if (i == end):
                # store the length of the substring
                partitions.append(i - start + 1)

                # store the start of the next substring
                start = i + 1

        # return the list of substring lengths
        return partitions

s = input('Enter a string to partition: ')
print(s)

solution = Solution()
print(solution.partitionLabels(s))
