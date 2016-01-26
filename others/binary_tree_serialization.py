import collections


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __repr__(self):
        return '[ %d ]' % self.val

def print_tree(r):
    queue = collections.deque()
    queue.append(r)
    while queue:
        node = queue.popleft()
        print(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Algorithm

class BSTSerilizer:
    delimiter = ','
    null = '#'
    @staticmethod
    def serilize(root):
        ret = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                ret.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ret.append(BSTSerilizer.null)
        return BSTSerilizer.delimiter.join(ret)

    @staticmethod
    def deserilize(ss):
        vals = ss.split(BSTSerilizer.delimiter)
        i = 0
        root = Tree(int(vals[i]))
        queue = collections.deque()
        queue.append(root)
        i += 1
        while queue:
            node = queue.popleft()
            if i < len(ss):
                if vals[i] == BSTSerilizer.null:
                    node.left = None
                else:
                    t = Tree(int(vals[i]))
                    node.left = t
                    queue.append(t)
                i += 1
                if vals[i] == BSTSerilizer.null:
                    node.right = None
                else:
                    t = Tree(int(vals[i]))
                    node.right = t
                    queue.append(t)
                i += 1
        return root


if __name__ == '__main__':
    '''
         3
       /   \
      9    20
          /  \
        15    7
    '''
    root = Tree(3)
    root.left = Tree(9)
    root.right = Tree(20)
    root.right.left = Tree(15)
    root.right.right = Tree(7)

    ss = serilize(root)
    print(ss)
    print_tree(deserilize(ss))
