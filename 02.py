with open("02.txt") as f:
    lines = [a.strip() for a in f.readlines()]

color_max = {'red': 12, 'green': 13, 'blue': 14}
s = 0
for idx, line in enumerate(lines):
    game = [(int(g.split()[0]), g.split()[1]) for g in line.split(':')[1].replace(',', ';').split(';')]  # list of pairs
    s += 0 if len([1 for value, color in game if value > color_max.get(color)]) > 0 else idx + 1

print(s)
assert s == 2164


s = 0
for idx, line in enumerate(lines):
    color_min = {'red': 0, 'green': 0, 'blue': 0}

    game = [(int(g.split()[0]), g.split()[1]) for g in line.split(':')[1].replace(',', ';').split(';')]  # list of pairs
    for value, color in game:
        color_min[color] = max(value, color_min[color])

    s += color_min['red'] * color_min['green'] * color_min['blue']

print(s)
assert s == 69929
