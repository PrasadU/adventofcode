import regex as re
from game_record import Game, GameSet

GAME_REC_PATTERN = re.compile(r'Game (\d+):([\s;]*[^;]*)+')
GAME_SET_PATTERN = re.compile(r'([\s;,]*(\d+)\s*(red|green|blue))+')


def read_game_file(file_name):
    games = []
    ex_file = open(file_name)
    for line in ex_file.readlines():
        games.append(parse_line(line))
    return games


def parse_line(rec_line) -> Game:
    sets = []
    matches = GAME_REC_PATTERN.match(rec_line)
    if matches:
        id = matches.group(1)
        set_strs = matches.captures(2)
        for set_str in set_strs:
            set_matches = GAME_SET_PATTERN.search(set_str)
            if set_matches:
                counts = set_matches.captures(2)
                colours = set_matches.captures(3)
                red = 0
                blue = 0
                green = 0
                for i, j in enumerate(colours):
                    if j == 'red':
                        red = int(counts[i])
                    if j == 'blue':
                        blue = int(counts[i])
                    if j == 'green':
                        green = int(counts[i])
                sets.append(GameSet(red, blue, green))
        return Game(int(id), sets)
    

def possible_games(games, maxes) -> (list, int):
    possible = []
    gid_total = 0
    for game in games:
        if game.is_possible(maxes):
            possible.append(game.gid)
            gid_total += game.gid
    print(f'possible games {possible}')
    return possible, gid_total
