with open("01.txt") as f:
    lines = [a.strip() for a in f.readlines()]


def get_value(s):
    a = next((x for x in s if x.isdigit()), None)
    b = next((x for x in reversed(s) if x.isdigit()), None)

    return int(a + b)


s = sum(get_value(line) for line in lines)
print(s)
assert 54697 == s


digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

s = 0
for line in lines:
    for idx in range(0, len(line)):  # move cursor over the line and replace found text-digit
        for i, digit in enumerate(digits):
            if line[idx:].startswith(digit):
                line = line[:idx] + str(i+1) + line[idx+1:]
                break

    s += get_value(line)
print(s)
assert 54885 == s
