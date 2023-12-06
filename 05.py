with open("05.txt") as f:
    lines = [a.strip() for a in f.readlines()]

seeds, m, mappings = [], [], []
for line in lines:
    if line.startswith('seeds: '):
        seeds = list(map(int, line[7:].split()))
    elif line == '' and len(m) > 0:
        mappings.append(m)
    elif 'map:' in line:
        m = []
    else:
        m.append(list(map(int, line.split())))
mappings.append(m)


def find_locations(bounds: list[tuple[int, int, int]], steps: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    """
    Computes the resultant location ranges based on provided seeds' ranges and mappings.

    Each seed's range is represented as (destination, source, size). The function calculates
    the overlap between these ranges and applies a shift based on the mappings, resulting in possible location ranges.

    :param bounds: A list of tuples representing seeds' ranges. Each tuple is in the format (destination, source, size).
    :param steps: A list of mappings that define the relationships between different planting steps.
                  Each mapping is a tuple in the format (destination, source, size).
    :return: A new list of tuples representing the resulting location ranges after reducing them to ranges relevant for
             input data
    """
    for step in steps:
        new_bounds = []
        for l1, r1 in [(d, d + l) for d, _, l in bounds]:  # source seed ranges
            for l2, r2, shift in [(s, s + l - 1, d - s) for d, s, l in step]:  # destination seed ranges
                l3, r3 = max(l1, l2), min(r1, r2)  # calculate intersection of two ranges

                if l3 <= r3:
                    new_bounds.append((l3 + shift, l3, r3 - l3 + 1))

        bounds = new_bounds

    return bounds


b = [(seed, seed, 1) for seed in seeds]  # (dst, src, size)
s = min([dst for dst, _, _ in find_locations(b, mappings)])
print(s)
assert s == 178159714


b = [(seeds[i], seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]  # (dst, src, size)
s = min([dst for dst, _, _ in find_locations(b, mappings)])
print(s)
assert s == 100165128

'''
A brute-force version for the first part:


s = 10 ** 20
for seed in seeds:
    for mapping in mappings:
        for a, b, c in mapping:
            if b <= seed <= b + c:
                seed = (seed - b) + a
                break
    s = min(s, seed)
    track = []

print(s)
assert s == 178159714

For the second part, the brute-force method (reversed search for the first hit
within the range 1..178159714) took approximately 1 hour.
'''
