import regex as re
import math


def get_dual_step_count(file_name):
    steps = read_steps(file_name)
    paths = read_paths(file_name)
    main_keys = [k for k in paths.keys() if k.endswith('A')]
    print(f'{file_name}: s: {len(steps)}, p: {len(paths)} \nkeys:{main_keys}')
    step_len = len(steps)
    next_steps = [k for k in main_keys]
    step_count = 0
    curr_step = 0
    while not all(e.endswith('Z') for e in next_steps):
        for i, cs in enumerate(next_steps):
            next_steps[i] = paths[cs][steps[curr_step]]
        curr_step += 1
        step_count += 1
        if curr_step > step_len-1:
            curr_step = 0
        if step_count % 100_000_000 == 0:
            print(f'{step_count}')
        if step_count > 10_000_000_000:
            print('not matching after 10B')
            break
    return step_count


def ends_match(v, s) -> bool:
    return not v.endswith(s)
    

def exact_match(v, s) -> bool:
    return s != v


def get_step_count_ends(file_name, start_step):
    return __get_step_count_func__(file_name, start_step, ends_match, 'Z', 20)    


def get_step_count(file_name, start_step):
    return __get_step_count_func__(file_name, start_step)[0]    


def __get_step_count_func__(file_name, start_step, func=exact_match, end_step='ZZZ', req_no_of_matches=1):
    steps = read_steps(file_name)
    paths = read_paths(file_name)
    step_len = len(steps)
    step_count = 0
    next_step = start_step
    curr_step = 0
    no_of_matches = 0
    all_matches = []
    just_matched = False
    while no_of_matches < req_no_of_matches:
        while func(next_step, end_step) or just_matched:
            just_matched = False
            next_step = paths[next_step][steps[curr_step]]
            curr_step += 1
            step_count += 1
            if curr_step > step_len-1:
                curr_step = 0
        all_matches.append(step_count)
        no_of_matches += 1
        just_matched = True
    return all_matches

    
def read_paths(file_name):
    paths = {}
    for line in open(file_name).readlines():
        if len(line.strip()) > 0:
            matches = re.match(r'(\w+)\s*=\s*\((\w+),\s(\w+)\)', line)
            if matches:
                paths[matches.group(1)] = (matches.group(2), matches.group(3))
    return paths


def read_steps(file_name):
    line = open(file_name).readline().strip()
    return get_steps(line)


def get_steps(line):
    steps = []
    for c in line:
        if str.lower(c) == 'l':
            steps.append(0)
        if str.lower(c) == 'r':
            steps.append(1)
    return steps


if __name__ == '__main__':
    print(f'simple: {get_step_count("input.txt", "AAA")}')
    print(f'multi:  {get_dual_step_count("example3.txt")}')
    #print(f'multi:  {get_dual_step_count("input.txt")}')
    lcm = (17287*13771*20803*23147*19631*17873)/math.gcd(17287, 13771, 20803, 23147, 19631, 17873)
    print(f'lcm = {int(lcm)}')
