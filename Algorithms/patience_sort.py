from bisect import bisect_left
from heapq import merge

class PatienceSort:
    def __init__(self):
        self.piles = []

    def sort(self, arr):
        for ele in arr:
            idx = self.binary_search(ele)
            if idx < len(self.piles):
                self.piles[idx].append(ele)
            else:
                self.piles.append([ele])

        return list(merge(*[reversed(pile) for pile in self.piles]))

    def binary_search(self, target: int) -> int:
        left, right = 0, len(self.piles) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.piles[mid][-1] < target:
                left = mid + 1
            else:
                right = mid

        return left + 1 if self.piles and self.piles[left][-1] < target else left

    def longest_increasing_subsequence(self, arr):
        self.sort(arr)
        return len(self.piles)

print(PatienceSort().longest_increasing_subsequence([1, 9, 5, 21, 17, 6]))
