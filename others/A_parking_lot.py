def move_cars(current, final):
    if len(current) <= 1:
        return 0
    if len(current) == 2 and current[0] == final[0]:
        return 0

    moves = 0
    for i, car in enumerate(current):
        if car == final[i]:
            if car == '_':
                # need to move car to this spot first
                moves += 1
        else:
            moves += 1
    # if there are two spots, only needs 1 move not 2 moves
    return moves - 1


if __name__ == '__main__':
    current = ['A', 'B', 'C', '_']
    final = ['_', 'B', 'A', 'C']
    print(move_cars(current, final)) # 2

    current = ['A', 'B', '_']
    final = ['B', 'A', '_']
    print(move_cars(current, final)) # 2

    current = ['A', '_', 'B', 'C']
    final = ['B', '_', 'C', 'A']
    print(move_cars(current, final)) # 3

    current = ['A', '_']
    final = ['_', 'A']
    print(move_cars(current, final)) # 1

    current = ['_', 'A']
    final = ['_', 'A']
    print(move_cars(current, final)) # 0

