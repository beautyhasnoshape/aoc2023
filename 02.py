with open("02.txt") as f:
    lines = [a.strip() for a in f.readlines()]

c_max = {'red': 12, 'green': 13, 'blue': 14}
s = 0
for line in lines:
    gid, game = line[5:].split(':')
    gid = int(gid)
    game = game.replace(',', ';').split(';')

    ok = True
    for turn in game:
        v, c = turn.strip().split(' ')
        if int(v) > c_max.get(c.strip()):
            ok = False
            break
    if ok:
        s += int(gid)
print(s)
assert s == 2164

s = 0
for line in lines:
    gid, game = line[5:].split(':')
    gid = int(gid)
    game = game.split(';')
    c_min = {'red': 0, 'green': 0, 'blue': 0}
    for turns in game:
        turn = turns.split(',')
        for t in turn:
            _, v, c = t.split(' ')
            if int(v) > c_min.get(c.strip()):
                c_min[c.strip()] = int(v)

    s += c_min.get('red') * c_min.get('green') * c_min.get('blue')
print(s)
assert s == 69929
