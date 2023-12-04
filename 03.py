import re

with open("03.txt") as f:
    lines = [a.strip() for a in f.readlines()]

# parse lines to find numbers and special chars, storing their positions along with values, e.g.:
# symbols = [('*', 1, 3), ('#', 3, 6), ('*', 4, 3)]
# numbers = {0: [(0, 467), (5, 114)], 1: [], 2: [(2, 35), (6, 633)], ...}
symbols, numbers = [], {i: [] for i in range(len(lines))}
for line_no, line in enumerate(lines):
    for symbol in [(match.group(), line_no, match.start()) for match in re.finditer(r'[^.\d]', line)]:
        symbols.append(symbol)

    for number in [(int(match.start()), int(match.group())) for match in re.finditer(r'[\d]+', line)]:
        numbers[line_no].append(number)


s = 0
# iterate over symbols and find adjacent values in surrounding rows
for _, row, col in symbols:
    for pos, value in numbers[row - 1] + numbers[row] + numbers[row + 1]:
        if pos - 1 <= col <= pos + len(str(value)):
            s += value

print(s)
assert s == 559667


s = 0
# iterate over stars and find adjacent values in surrounding rows
for row, col in [(row, col) for c, row, col in symbols if c == '*']:
    found_number = None
    for pos, value in numbers[row - 1] + numbers[row] + numbers[row + 1]:
        if pos - 1 <= col <= pos + len(str(value)):
            if found_number:
                s += found_number * value
                break
            else:
                found_number = value

print(s)
assert s == 86841457

