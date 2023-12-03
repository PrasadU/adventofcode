from solution import read_schema 


def test_example():
    schema = read_schema('example.txt')
    assert schema[0] == [467, 35, 633, 617, 592, 755, 664, 598]
    assert schema[1] == [114, 58]
    assert schema[2] == 4361
    assert schema[3] == 467835
    
    
def test_input():
    schema = read_schema('input.txt')