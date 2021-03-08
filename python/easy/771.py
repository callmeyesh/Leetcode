"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        if not J and not S:
            return count

        j = set(J)
        for s in S:
            if s in j:
                count = count + 1
        return count

    def numJewelsInStones_constant_space(self, J, S):
        count = 0
        if not J and not S:
            return count

        char_arr = [0 for i in range(127)]
        for j in J:
            char_arr[ord(j)] = 1

        for s in S:
            count += char_arr[ord(s)]

        return count


if __name__ == "__main__":
    Solution().numJewelsInStones_constant_space("aA", "aAAbbbb")
