"""
given a m*n matrix, print the matrix spirally clockwise
"""

def print_spiral(matrix):
    m, n = len(matrix), len(matrix[0])

    top, down = 0, m - 1
    left, right = 0, n - 1

    while True:
        for j in xrange(left, right + 1):
            print(matrix[top][j])
        top += 1
        if top > down or left > right:
            break
        for i in xrange(top, down + 1):
            print(matrix[i][right])
        right -= 1
        if top > down or left > right:
            break
        for j in reversed(xrange(left, right + 1)):
            print(matrix[down][j])
        down -= 1
        if top > down or left > right:
            break
        for i in reversed(xrange(top, down + 1)):
            print(matrix[i][left])
        left += 1
        if top > down or left > right:
            break


if __name__ == '__main__':
    matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    print_spiral(matrix)
