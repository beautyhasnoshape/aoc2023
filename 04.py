with open("04.txt") as f:
    lines = [a.strip() for a in f.readlines()]

all_winning_cards, all_my_cards = [], []
for line in lines:
    winning_cards, my_cards = map(lambda a: list(map(int, a.split())), line.split(':')[1].split('|'))
    all_winning_cards.append(winning_cards), all_my_cards.append(my_cards)

s = 0
for winning_cards, my_cards in zip(all_winning_cards, all_my_cards):
    common_cards = [card for card in winning_cards if card in my_cards]
    s += 0 if len(common_cards) == 0 else 2 ** (len(common_cards) - 1)

print(s)
assert s == 22897


bonus_cards = [1] * len(lines)
for idx, winning_cards, my_cards in zip([i for i in range(len(lines))], all_winning_cards, all_my_cards):
    draw_score = sum(winning_card in my_cards for winning_card in winning_cards)
    for i in range(draw_score):
        bonus_cards[idx + i] += bonus_cards[idx - 1]

s = sum(bonus_cards)
print(s)
assert s == 5095824

