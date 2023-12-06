import regex as re
import threading

def read_almanac(file_name):
    lines = open(file_name).readlines()
    map_names = []
    map_of_lists = {}
    last_map_name = ''
    for i in range(1, len(lines)):
        cur_line = lines[i].strip()
        if (len(cur_line)) == 0:
            continue
        elif cur_line.endswith('map:'):
            map_name = re.match(r'(\S+)\s+map:', cur_line).group(1)
            last_map_name = map_name
            map_names.append(map_name)
            map_of_lists[map_name] = []
        else:
            # read line
            raw_def = list(map(str_to_int, re.match(r'(\d+) +(\d+) +(\d+)', cur_line).groups()))
            map_of_lists[last_map_name].append((raw_def[1], raw_def[0], raw_def[2]))
    # maps read - loop seeds
    seed_numbers = get_seeds_numbers(lines[0])
    threads = []
    sni = 0
    while sni <= len(seed_numbers)-2:
        start = seed_numbers[sni]
        end = start + seed_numbers[sni+1]
        print(f'running {seed_numbers[sni]} ~ {seed_numbers[sni+1]}')
        thread = ProcThread(map_names, map_of_lists, start, end)
        threads.append(thread)
        thread.start()
        sni += 2
    for thread in threads:
        thread.join()

    min_sid = None
    min_location = None
    for batch in threads:
        if min_location is None or batch.min[0] < min_location:
            min_location = batch.min[0]
            min_sid = batch.min[1]
    print(f'{min_sid} with {min_location}')
    return min_location, {'seeds': [], 'map_of_maps': map_of_lists, 'worked_paths': []}


def find_min_in_a_set(map_names, map_of_lists, start, end):
    min_location = None
    min_sid = None
    for sid in range(start, end):
        last_lookup = sid
        for mn in map_names:
            last_lookup = lookup_next(map_of_lists[mn], last_lookup)
        if min_location is None or last_lookup < min_location:
            min_location = last_lookup
            min_sid = sid
    return min_location, min_sid


def lookup_next(rules_list, key):
    key_value = key
    for rule in rules_list:
        if rule[0] <= key < rule[0]+rule[2]:
            key_value = rule[1] + key - rule[0]
            break
    return key_value


def get_seeds_numbers(line) -> [str]:
    seed_numbers = []
    m_itr = re.finditer(r'seeds:( (\d+))*', line)
    if m_itr:
        for m in m_itr:
            seed_numbers = list(map(str_to_int, m.captures(2)))
    print(f'seed_numbers: {seed_numbers}')
    return seed_numbers


def str_to_int(str_val) -> int:
    return int(str_val)


class ProcThread(threading.Thread):
    def __init__(self, map_names, map_of_lists, begin, end):
        super(ProcThread, self).__init__()
        self.map_names = map_names
        self.map_of_lists = map_of_lists
        self.begin = begin
        self.end = end
        self.min = (None, None)

    def run(self):
        self.min = find_min_in_a_set(self.map_names, self.map_of_lists, self.begin, self.end)
