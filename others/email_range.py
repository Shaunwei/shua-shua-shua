import heapq


class Solution:
    def __init__(self):
        pass

    def solve1(self, input_):
        '''
        Heap Sort
        '''
        pairs_heap = self.build_heap(input_)

        rets = []
        if not pairs_heap:
            return rets
        cur_st, cur_ed = heapq.heappop(pairs_heap)
        while pairs_heap:
            mst, med = heapq.heappop(pairs_heap)
            if cur_ed + 1 < mst:
                rets.append([cur_st, cur_ed])
                cur_st = mst
                cur_ed = med
            else:
                cur_ed = max(cur_ed, med)
        rets.append([cur_st, cur_ed])
        return rets

    def build_heap(self, input_):
        heap = []
        for pair in input_.split(','):
            vals = pair.split(':')
            st = int(vals[0].strip())
            ed = int(vals[1].strip())
            heapq.heappush(heap, (st, ed))
        return heap


    def solve2(self, input_):
        '''
        sort
        '''
        pairs = ([int(p[0]), int(p[1])] for p in self.parse(input_))
        rets = []
        st, ed = None, None
        for mst, med in sorted(pairs):
            if st is None and ed is None:
                st, ed = mst, med
            elif ed + 1 < mst:
                rets.append([st, ed])
                st, ed = mst, med
            else:
                ed = max(ed, med)
        rets.append([st, ed])
        return rets

    def parse(self, input_):
        return (pair.split(':') for pair in input_.split(','))





if __name__ == '__main__':
    inputs_ = [
        '5:10,  1:2, 3:4',
        '1: 3, 2: 4, 1:9',
        '1: 4,   5: 10,  11:20',
        '5:10, 1:2',
        '1: 30',
        '10: 20, 20: 30, 30: 40'
    ]
    s = Solution()
    for input_ in inputs_:
        print(s.solve1(input_))
        print(s.solve2(input_))
