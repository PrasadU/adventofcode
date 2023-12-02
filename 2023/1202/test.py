from solution1 import possible_games, parse_line, read_game_file


def test_input():
    games = read_game_file('input.txt')
    print(f"{possible_games(games, (12, 14, 13))}")


def test_example():
    games = read_game_file('example.txt')
    assert possible_games(games, (12, 14, 13)) == ([1, 2, 5], 8)


def test_parsing():
    games = read_game_file('example.txt')
    assert len(games) == 5
    verify_game_data(games[0], 1, [(4, 3, 0), (1, 6, 2), (0, 0, 2)], (4, 6, 2))
    verify_game_data(games[1], 2, [(0, 1, 2), (1, 4, 3), (0, 1, 1)], (1, 4, 3))
    verify_game_data(games[2], 3, [(20, 6, 8), (4, 5, 13), (1, 0, 5)], (20, 6, 13))
    verify_game_data(games[3], 4, [(3, 6, 1), (6, 0, 3), (14, 15, 3)], (14, 15, 3))
    verify_game_data(games[4], 5, [(6, 1, 3), (1, 2, 2)], (6, 2, 3))

        
def verify_game_data(game, gid, sets, maxs):
    assert game
    assert game.gid == gid
    assert len(game.sets) == len(sets)
    for i in range(len(game.sets)):
        assert game.sets[i].red == sets[i][0], f'{gid} set: {i} red actual: {game.sets[i].red} exp: {sets[i][0]}'
        assert game.sets[i].blue == sets[i][1], f'{gid} set: {i} red actual: {game.sets[i].red} exp: {sets[i][0]}'
        assert game.sets[i].green == sets[i][2], f'{gid} set: {i} red actual: {game.sets[i].red} exp: {sets[i][0]}'
    assert game.get_max()[0] == maxs
