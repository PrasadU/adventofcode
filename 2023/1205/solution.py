import regex as re


def read_almanac(file_name):
    lines = open(file_name).readlines()
    seeds = get_seeds(lines[0])
    map_names = []
    map_of_maps = {}
    last_map_name = ''
    for i in range(1, len(lines)):
        cur_line = lines[i].strip()
        if (len(cur_line)) == 0:
            continue
        elif cur_line.endswith('map:'):
            map_name = re.match(r'(\S+)\s+map:', cur_line).group(1)
            last_map_name = map_name
            map_names.append(map_name)
            map_of_maps[map_name] = {}
        else:
            # read line
            raw_def = list(map(str_to_int, re.match(r'(\d+) +(\d+) +(\d+)', cur_line).groups()))
            for ri in range(raw_def[2]):
                map_of_maps[last_map_name][raw_def[1] + ri] = raw_def[0] + ri
    worked_paths = {}
    min_location = None
    min_sid = None
    for sid in seeds:
        worked_paths[sid] = [sid]
        last_lookup = sid
        for mn in map_names:
            last_lookup = map_of_maps[mn].setdefault(last_lookup, last_lookup)
            worked_paths[sid].append(last_lookup)
        if min_location is None or last_lookup < min_location:
            min_location = last_lookup
            min_sid = sid
        print(f'{min_sid} with {min_location} : {sid} : {worked_paths[sid]}')

    return min_location, {'seeds': seeds, 'map_of_maps': map_of_maps, 'worked_paths': worked_paths}


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