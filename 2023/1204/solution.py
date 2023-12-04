import regex as re
import math


def read_cards(file_name):
    cards = {}
    won_cards = {}
    total_value = 0
    lines = open(file_name).readlines()
    for line in lines:
        lm = re.finditer(r'Card *(\d+):( +(\d+))+\s+\|( +(\d+))+', line)
        if lm:
            for m in lm:
                card_id = int(m.group(1))
                win_numbers = m.captures(5)
                card_numbers = m.captures(3)
                card_matches = [n for n in card_numbers if n in win_numbers]
                card_match_len = len(card_matches)
                card_value = 0
                if card_match_len > 0:
                    card_value = int(math.pow(2, card_match_len - 1))
                    count_of_cards = 1 + won_cards.setdefault(card_id, 0)
                    for i in range(card_id+1, card_id+1+card_match_len):
                        won_cards[i] = won_cards.setdefault(i, 0) + count_of_cards
                total_value += card_value
                cards[card_id] = (win_numbers, card_numbers, card_matches, card_match_len, card_value)
                print(f'#{card_id} >> {card_value}')
    new_cards_count = 0
    for cid in cards.keys():
        new_cards_count += won_cards.setdefault(cid, 0)
    total_cards = new_cards_count+len(cards.keys())
    print(f'\n\n# lines, cards: {len(lines)}, {len(cards)}')
    print(f'total value = {total_value}')
    print(f'extra cards won = {new_cards_count}')
    print(f'Total cards = {total_cards}')
    return cards, total_value, new_cards_count, total_cards
