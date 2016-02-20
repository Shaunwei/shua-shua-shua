class Solution:
    def __init__(self, friends):
        self.friends = friends

    def find_friends_dfs(self):
        visited = [False] * len(self.friends)
        ret = []
        for i in range(len(self.friends)):
            if not visited[i]:
                friends = []
                self.dfs(i, friends, visited)
                ret.append(friends)
        return ret

    def dfs(self, i, friends, visited):
        visited[i] = True
        friends.append(i)
        for j in range(i + 1, len(self.friends)):
            if not visited[j] and self.friends[i][j]:
                self.dfs(j, friends, visited)


    def find_friends_uf(self):
        '''
        take the leftmost as parent
        only search left bottom part of friends matrix
        '''
        nodes = {i: [i] for i in range(len(self.friends))}
        for i in range(len(self.friends)):
            # j point the values before i
            for j in range(i):
                if self.friends[j][i]:
                    # remove i node
                    del nodes[i]
                    # append to its parent node
                    nodes[j].append(i)
        return list(nodes.values())



if __name__ == '__main__':
    friends = [
          [ True,  True, False, False, False],
          [ True,  True, False, False, False],
          [False, False,  True,  True, False],
          [False, False,  True,  True, False],
          [False, False, False, False,  True]
        ]
    s = Solution(friends)
    print('DFS ->', s.find_friends_dfs())
    print('Union Find ->', s.find_friends_uf())
'''
DFS -> [[0, 1], [2, 3], [4]]
Union Find -> [[0, 1], [2, 3], [4]]
'''
