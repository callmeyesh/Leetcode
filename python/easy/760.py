"""
Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]
"""


class Solution(object):
    def anagramMapping(self, A, B) -> list:
        indexMap = {b: index for index, b in enumerate(B)}
        return [indexMap[a] for a in A]


if __name__ == "__main__":
    Solution().anagramMapping([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
