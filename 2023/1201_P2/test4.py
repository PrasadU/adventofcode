from solution4 import func_1201_4
from solution5 import func_1201_5


def test_1201_example_solution4():
    assert func_1201_4('2023/1201_P2/example1.txt') == 641


def test_1201_example2_solution4():
    assert func_1201_4('2023/1201_P2/example2.txt') == 281


def test_1201_input_solution4():
    print(f"ans = {func_1201_4('2023/1201_P2/input.txt')}")


def test_1201_example_solution5():
    assert func_1201_5('2023/1201_P2/example1.txt') == 641


def test_1201_example2_solution5():
    assert func_1201_5('2023/1201_P2/example2.txt') == 281


def test_1201_input_solution5():
    print(f"ans = {func_1201_5('2023/1201_P2/input.txt', True)}")
