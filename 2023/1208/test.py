import math
from solution1 import *


def test_example():
    assert get_step_count('example1.txt', 'AAA') == 2
    assert get_step_count('example2.txt', 'AAA') == 6
    assert get_step_count('input.txt', 'AAA') == 17287
    assert get_dual_step_count('example3.txt') == 6
    for i in ['AAA', 'GPA', 'GTA', 'VDA', 'BBA', 'VSA']:
        steps = get_step_count_ends('input.txt', i)
        print(f'input: {i} >> {steps}')
        

def test_condition():
    args = [(['AZ', 'BZ', 'CZ'], True),
            (['AZ', 'AA', 'CZ'], False),
            (['AA', 'BB', 'CC'], False)]    
    for ex in args:
        res = all(e.endswith('Z') for e in ex[0])
        assert res == ex[1]


def test_read_steps():
    assert read_steps('example1.txt') == [1, 0]
    assert read_steps('example2.txt') == [0, 0, 1]
    assert get_steps('lrlrlr') == [0, 1, 0, 1, 0, 1]
    assert get_steps('rlrl') == [1, 0, 1, 0]
    assert get_steps('rrrl') == [1, 1, 1, 0]
    assert get_steps('llll') == [0, 0, 0, 0]


def test_read_maps():
    exp = {
        'AAA': ('BBB', 'BBB'),
        'BBB': ('AAA', 'ZZZ'),
        'ZZZ': ('ZZZ', 'ZZZ')
    }
    assert read_paths('example2.txt') == exp
