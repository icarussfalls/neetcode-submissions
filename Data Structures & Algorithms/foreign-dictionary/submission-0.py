class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Initialize graph and indegree
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        # 2. Compare adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Invalid prefix case
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # 3. Start with characters having indegree 0
        queue = deque(
            c for c in indegree if indegree[c] == 0
        )

        result = []

        # 4. Topological sort
        while queue:
            char = queue.popleft()
            result.append(char)

            for nei in graph[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        # 5. Cycle detection
        if len(result) != len(indegree):
            return ""

        return "".join(result)