from solution import read_cards


def test_input():
    cards_and_total = read_cards('input.txt')
    assert cards_and_total[1] == 23941
    assert cards_and_total[3] == 5571760


def test_example():
    card_and_total = read_cards('example.txt')
    exp_card_values = [8, 2, 2, 1, 0, 0]
    for i in range(len(exp_card_values)):
        assert exp_card_values[i] == card_and_total[0][i+1][4]
    assert card_and_total[1] == 13
    assert card_and_total[3] == 30
