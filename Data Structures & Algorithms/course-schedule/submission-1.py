class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        # Use a plain list as the queue
        queue = [i for i in range(numCourses) if in_degree[i] == 0]

        # Use a simple pointer index instead of popleft()
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1

            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # len(queue) contains all successfully unlocked courses
        return len(queue) == numCourses