class BST:
    count = 0
    def __init__(self, val, cnt=0):
        self.val = val
        self.cnt = cnt

    @staticmethod
    def build(arr, st, ed):
        if st > ed:
            return

        mid = (st + ed) / 2
        root = BST(arr[mid])
        root.right = BST.build(arr, mid + 1, ed)
        root.cnt = BST.count
        BST.count += 1
        root.left = BST.build(arr, st, mid - 1)
        return root

    @staticmethod
    def query(root, val):
        while root:
            if root.val == val:
                return root.cnt
            elif root.val > val:
                root = root.left
            else:
                root = root.right

    @staticmethod
    def query_larger(root, val):
        prev = None
        while root:
            if root.val == val:
                return root.cntto
            elif root.val > val:
                prev = root
                root = root.left
            else:
                prev = root
                root = root.right
        if prev and prev.val < val:
            return prev.cnt
        else:
            return prev.cnt + 1

if __name__ == '__main__':
    root = BST.build(range(10), 0, 9)
    print(BST.query_larger(root, 8.1))
