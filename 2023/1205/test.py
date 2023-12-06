from solution1 import read_almanac


def test_input():
    read_almanac('input.txt')


def test_example():
    almanac = read_almanac('example.txt')
    expected_seeds = [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
    expected_paths = {
        79: [79, 81, 81, 81, 74, 78, 78, 82],
        55: [55, 57, 57, 53, 46, 82, 82, 86],
    }

    # assert almanac[1]['seeds'] == expected_seeds
    # seed_to_soil = almanac[1]['map_of_maps']['seed-to-soil']
    # for i in range(49):
    #     assert seed_to_soil.setdefault(i, i) == i
    # for i in range(50, 98):
    #     assert seed_to_soil.setdefault(i, i) == 52 + (i-50)
    # assert seed_to_soil.setdefault(98, 98) == 50
    # assert seed_to_soil.setdefault(99, 99) == 51
    # for i in range(100, 110):
    #     assert seed_to_soil.setdefault(i, i) == i
    # for sid in expected_paths.keys():
    #     assert almanac[1]['worked_paths'][sid] == expected_paths[sid]
    assert almanac[0] == 46

