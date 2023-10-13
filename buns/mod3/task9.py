def get_location_robot(steps):
    moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    current_move = 0
    x, y = 0, 0

    for i in range(1, steps + 1):
        move = moves[current_move % 4]
        x += move[0]
        y += move[1]

        if (i % 2 == 0) and (i // 2 % 4 == 0 or i // 2 % 4 == 2):
            current_move = (current_move + 1) % 4

    return (x, y)

steps = int(input())
print(get_location_robot(steps))
