with open("03.txt") as f:
    lines = [a.strip() for a in f.readlines()]

symbols, numbers = [], {i: [] for i in range(len(lines))}

# parse lines to find numbers and special chars, storing their positions along with values, e.g.:
# symbols = [('*', 1, 3), ('#', 3, 6), ('*', 4, 3)]
# numbers = {0: [(0, 467), (5, 114)], 1: [], 2: [(2, 35), (6, 633)], ...}
for line_no, line in enumerate(lines):
    num = ''
    is_digit = False
    for idx, c in enumerate(line):
        if c.isdigit():
            num += c
            if idx == len(line) - 1:
                numbers[line_no].append((idx - len(num), int(num)))
        else:
            if not c.isdigit() and not c == '.':
                symbols.append((c, line_no, idx))
            if len(num) > 0:
                numbers[line_no].append((idx - len(num), int(num)))
            num = ''

s = 0
# iterate over symbols and find adjacent values in surrounding rows
for symbol in symbols:
    c, row, col = symbol
    for pos, value in numbers[row - 1] + numbers[row] + numbers[row + 1]:
        pos_left = pos
        pos_right = pos + len(str(value)) - 1
        if pos_left - 1 <= col <= pos_right + 1:
            s += value

print(s)
assert s == 559667

s = 0
# iterate over stars and find adjacent values in surrounding rows
for symbol in symbols:
    c, row, col = symbol
    if c != '*':
        continue
    found_number = None
    for pos, value in numbers[row - 1] + numbers[row] + numbers[row + 1]:
        pos_left = pos
        pos_right = pos + len(str(value)) - 1
        if pos_left - 1 <= col <= pos_right + 1:
            if found_number:
                s += found_number * value
                found_number = None
            else:
                found_number = value
print(s)
assert s == 86841457

