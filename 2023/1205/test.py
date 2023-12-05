from solution1 import read_almanac


def test_input():
    read_almanac('input.txt')


def test_example():
    almanac = read_almanac('example.txt')
    expected_seeds = [79, 14, 55, 13]
    expected_paths = {
        79: [79, 81, 81, 81, 74, 78, 78, 82],
        14: [14, 14, 53, 49, 42, 42, 43, 43],
        55: [55, 57, 57, 53, 46, 82, 82, 86],
        13: [13, 13, 52, 41, 34, 34, 35, 35],
    }

    assert almanac[1]['seeds'] == expected_seeds
    # seed_to_soil = almanac[1]['map_of_maps']['seed-to-soil']
    # for i in range(49):
    #     assert seed_to_soil.setdefault(i, i) == i
    # for i in range(50, 98):
    #     assert seed_to_soil.setdefault(i, i) == 52 + (i-50)
    # assert seed_to_soil.setdefault(98, 98) == 50
    # assert seed_to_soil.setdefault(99, 99) == 51
    # for i in range(100, 110):
    #     assert seed_to_soil.setdefault(i, i) == i
    for sid in expected_seeds:
        assert almanac[1]['worked_paths'][sid] == expected_paths[sid]
    assert almanac[0] == 35

