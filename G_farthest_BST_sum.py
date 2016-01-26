"""
given a BST, find the two nodes that sums up to a value and are the farthest apart.
"""
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __repr__(self):
        return '[ %d ]' % self.val

def get_tree():
    def build_tree(vals):
        if not vals:
            return
        mid = len(vals) / 2
        root = Tree(vals[mid])
        root.left = build_tree(vals[:mid])
        root.right = build_tree(vals[mid+1:])
        return root
    return build_tree(range(1, 8))

def print_tree(r):
    stack = []
    while stack or r:
        if r:
            stack.append(r)
            r = r.left
        else:
            r = stack.pop()
            print(r)
            r = r.right


class Solution:
    def find_farthest_nodes(self, tree, sums):
        values = self.in_order(tree)
        distance = 0
        nodes = [0, 0]
        for val in values:
            if val > sums or val > sums - val:
                break
            if self.bs(values, sums - val):
                d, n1, n2 = self.find_distance(tree, val, sums - val)
                if d > distance:
                    distance = d
                    nodes = [n1, n2]
        return nodes

    def in_order(self, root):
        values = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                values.append(root.val)
                root = root.right
        return values

    def bs(self, values, target):
        st, ed = 0, len(values) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if values[mid] == target:
                return True
            elif values[mid] < target:
                st = mid
            else:
                ed = mid
        return values[st] == target or values[ed] == target

    def find_distance(self, root, v1, v2):
        n1, p1 = self.find_path(root, v1)
        n2, p2 = self.find_path(root, v2)
        i = 0
        for i in xrange(min(len(p1), len(p2))):
            if p1[i] != p2[i]:
                break
        return len(p1[i:]) + len(p2[i:]), n1, n2

    def find_path(self, root, val):
        path = []
        while root.val != val:
            path.append(root.val)
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root, path



if __name__ == '__main__':
    # print_tree(get_tree())
    print(Solution().find_farthest_nodes(get_tree(), 7))
