class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            root1 = find(u)
            root2 = find(v)

            if root1 == root2:
                return [u, v]

            if size[root1] < size[root2]:
                root1, root2 = root2, root1

            parent[root2] = root1
            size[root1] += size[root2]