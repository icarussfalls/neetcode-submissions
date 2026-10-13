class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      if not heights or not heights[0]:
        return []

      ROWS, COLS = len(heights), len(heights[0])
      pac = set()
      atl = set()

      def dfs(r: int, c: int, visited: set, prev_height: int):
        if (
            r < 0
            or r >= ROWS
            or c < 0
            or c >= COLS
            or (r, c) in visited
            or heights[r][c] < prev_height
        ):
          return

        visited.add((r, c))

        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

      for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

      for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

      return [[r, c] for r, c in pac & atl]