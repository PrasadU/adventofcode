from solution import read_almanac


def test_example():
    almanac = read_almanac('example.txt')
    assert almanac[0]['seeds'] == [79, 14, 55, 13]
    assert almanac[1] == 35
    
