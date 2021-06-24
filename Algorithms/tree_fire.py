import math
import collections


class Solution:
    def count_saved_trees(self, grid, fire, station):
        tree_count, self.grid = 0, grid
        self.m ,self.n = len(grid), len(grid[0])
        self.dist_arr = [[math.inf, math.inf] for _ in range(self.m * self.n)]

        self.bfs(fire, set(), index=0)
        self.bfs(station, set(), index=1)

        for idx, dist in enumerate(self.dist_arr):
            row, col = idx//self.n, idx%self.n
            if grid[row][col] == -1: continue
            # station >= fire
            if math.inf not in dist and dist[1] >= dist[0]:
                tree_count += grid[row][col]
        print(tree_count)
        print(self.dist_arr)
        return tree_count

    def bfs(self, start, visited, index):
        queue = collections.deque([[start[0], start[1], 0]])

        while queue:
            r, c, dist = queue.popleft()
            if self.grid[r][c] == -1: continue
            visited.add((r, c))
            self.dist_arr[(r * self.n) + c][index] = dist
            for d_x, d_y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_x, new_y = r + d_x, c + d_y
                if self.valid(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append([new_x, new_y, dist + 1])

    def valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

if __name__ == "__main__":
    s = Solution()
    print(s.count_saved_trees([[1,1],[4,-1],[-1,-1],[4,-1]], (3,1), (0,0)) == 6, "number 1")
