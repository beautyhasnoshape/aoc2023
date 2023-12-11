import math
from functools import reduce

with open("08.txt") as f:
    lines = [a.strip() for a in f.readlines()]


instructions = [0 if a == 'L' else 1 for a in lines[0]]
nodes = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

node = nodes.get('AAA')
for step in range(10 ** 100):
    next_name = node[instructions[step % len(instructions)]]
    if next_name == 'ZZZ':
        break

    node = nodes[next_name]

s = step + 1
print(s)
assert s == 24253


def lcm(numbers):
    def lcm_of_two(a, b):
        return abs(a * b) // math.gcd(a, b) if a and b else 0

    return reduce(lcm_of_two, numbers, 1)


n, r = [nodes[key] for key in nodes.keys() if str(key).endswith('A')], []
for node in n:
    for step in range(10 ** 100):
        next_name = node[instructions[step % len(instructions)]]
        if str(next_name).endswith('Z'):
            r.append(step + 1)
            break

        node = nodes[next_name]

s = lcm(r)
print(s)
assert s == 12357789728873
