import regex as re


def read_almanac(file_name):
    lines = open(file_name).readlines()
    seeds = get_seeds(lines[0])
    map_of_maps = {}
    last_map_name = ''
    for i in range(1, len(lines)):
        cur_line = lines[i].strip()
        if (len(cur_line)) == 0:
            continue
        if cur_line.endswith('map:'):
            map_name = re.match(r'\w map:').group(1)
            map_of_maps[map_name]
            last_map_name = map_name
        map_m = list(map(str_to_int, re.match(r'(\d+) +(\d+) +(\d+)').groups()))
        
    return {'seeds': seeds}, 0


def get_seeds(line) -> [str]:
    seeds = []
    m_itr = re.finditer(r'seeds:( (\d+))*', line)
    if m_itr:
        for m in m_itr:
            seeds = list(map(str_to_int, m.captures(2)))
    print(f'seeds: {seeds}')
    return seeds


def str_to_int(str_val) -> int:
    return int(str_val)