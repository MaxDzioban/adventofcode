x, y = 0, 0
visited = set()
visited.add((x, y))
with open("day_3_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        for move in line:
            if move == '^':
                y += 1
            elif move == 'v':
                y -= 1
            elif move == '>':
                x += 1
            elif move == '<':
                x -= 1
            visited.add((x, y))
print(len(visited))


santa_x = santa_y = 0
robo_x = robo_y = 0

visited = set()
visited.add((0, 0))
with open("day_3_year_2015.txt", "r", encoding="utf-8") as file:
    for line in file:
        for i, direction in enumerate(line):
            if i % 2 == 0:
                x, y = santa_x, santa_y
            else:
                x, y = robo_x, robo_y
            if direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == '<':
                x -= 1
            visited.add((x, y))
            if i % 2 == 0:
                santa_x, santa_y = x, y
            else:
                robo_x, robo_y = x, y
print(len(visited))