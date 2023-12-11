with open("11.txt") as f:
    lines = [a.strip() for a in f.readlines()]

galaxies = [(x + 1, y + 1) for y, row in enumerate(lines) for x, cell in enumerate(row) if cell == '#']
w, h = len(lines[0]), len(lines)

empty_x = [x + 1 for x in range(w) if w == len([1 for y in range(h) if lines[y][x] == '.'])]
empty_y = [y + 1 for y in range(h) if h == len([1 for x in range(w) if lines[y][x] == '.'])]


def calc_distances(g: [(int, int)], expand_x: [int], expand_y: [int], factor: int=1) -> int:
    d, g_count = 0, len(g)

    for i, j in [(i, j) for i in range(g_count) for j in range(i + 1, g_count)]:
        g1, g2 = g[i], g[j]
        min_x, max_x, min_y, max_y = min(g1[0], g2[0]), max(g1[0], g2[0]), min(g1[1], g2[1]), max(g1[1], g2[1])
        distance = max_x - min_x + max_y - min_y

        distance += sum([factor - 1 for x in range(min_x + 1, max_x) if x in expand_x])
        distance += sum([factor - 1 for y in range(min_y + 1, max_y) if y in expand_y])

        d += distance

    return d


s = calc_distances(galaxies, empty_x, empty_y, 2)
print(s)
assert s == 10033566


s = calc_distances(galaxies, empty_x, empty_y, 1000000)
print(s)
assert s == 560822911938
