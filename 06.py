with open("06.txt") as f:
    lines = [a.strip() for a in f.readlines()]

time, dist = [[int(a) for a in line[10:].split()] for line in lines]


def calc(time: [], dist: []) -> int:
    result, idx_min, idx_max = 1, 0, 0
    for t, d in zip(time, dist):
        for idx in range(1, t):
            if idx * (t - idx) > d:
                idx_min = idx
                break

        for idx in reversed(range(1, t)):
            if idx * (t - idx) > d:
                idx_max = idx
                break

        result *= (idx_max - idx_min + 1)

    return result


s = calc(time, dist)
print(s)
assert s == 1083852


time = [int(''.join(str(a) for a in time))]
dist = [int(''.join(str(a) for a in dist))]

s = calc(time, dist)
print(s)
assert s == 23501589
