import timeit

import regex as re
import threading
import multiprocessing as mp
import datetime

BATCH_SIZE = 100_000_000
MAX_PROCESS = 5


def start_wait(processes, mp_results):
    proc_count = len(processes)
    print(f'For proc: {proc_count}, results count: {len(mp_results)}')
    start_c = 0
    while start_c < proc_count:
        end_c = min(start_c+MAX_PROCESS, proc_count)
        for i in range(start_c, end_c):
            processes[i][0].start()
        print(f'Started {end_c} processes')
        for i in range(start_c, end_c):
            mp_results.append(processes[i][1].get())
            processes[i][0].join()
        print(f'Completed {end_c} processes')
        start_c = end_c
    print(f'completed proc: {proc_count} / {end_c}, results count: {len(mp_results)}')


# maps read - loop seeds

def read_maps(file_name):
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
    return map_names, map_of_lists


def read_almanac(file_name):
    seed_numbers = get_seeds_numbers(open(file_name).readline())
    processes = []
    sni = 0
    while sni <= len(seed_numbers)-2:
        start = seed_numbers[sni]
        incr = seed_numbers[sni + 1]
        end = start + incr
        pos_id = int(sni / 2)
        print(f'For pos={pos_id} {start} ~ {incr}')
        n_start = start
        while n_start < end:
            n_end = min(n_start + BATCH_SIZE, end)
            q = mp.Queue()
            p = mp.Process(target=find_min_in_a_set, args=(file_name, pos_id, n_start, n_end, q))
            print(f'Created Process pos: {pos_id} - {start} {incr} , s: {n_start}, e: {n_end}')
            processes.append((p, q))
            n_start = n_end
        sni += 2
    print(f'created process count: {len(processes)}')
    mp_results = []
    start_wait(processes, mp_results)
    min_sid = None
    min_location = None
    for batch in mp_results:
        if min_location is None or batch[0] < min_location:
            min_location = batch[0]
            min_sid = batch[1]
    print(f'{min_sid} with {min_location}')
    return min_location, {'seeds': [], 'map_of_maps': [], 'worked_paths': []}


def find_min_in_a_set(file_name, id, start, end, q):
    start_time = timeit.default_timer()
    map_names, map_of_lists = read_maps(file_name)
    min_location = None
    min_sid = None
    for sid in range(start, end):
        last_lookup = sid
        for mn in map_names:
            last_lookup = lookup_next(map_of_lists[mn], last_lookup)
        if min_location is None or last_lookup < min_location:
            min_location = last_lookup
            min_sid = sid
    duration = (timeit.default_timer() - start_time) / 60
    dur_min = int(duration)
    print(f'Completed Process pos: {id}, s:{start}, e={end}, min_l: {min_location}, min_sid: {min_sid}, dur={dur_min} min')
    q.put([min_location, min_sid])


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
    def __init__(self, map_names, map_of_lists, id, begin, end):
        super(ProcThread, self).__init__()
        self.map_names = map_names
        self.map_of_lists = map_of_lists
        self.begin = begin
        self.id = id
        self.end = end
        self.min = (None, None)

    def run(self):
        self.min = find_min_in_a_set(self.map_names, self.map_of_lists, self.id, self.begin, self.end)
