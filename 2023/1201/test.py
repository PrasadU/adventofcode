from solution3 import func_1201_3
from solution2 import func_1201_2
from solution1 import func_1201


def test_1201_example_solution2():
    assert func_1201_2('2023/1201/example.txt') == 142


def test_1201_input_solution2():
    print(f"ans = {func_1201_2('2023/1201/input.txt', True)}")


def test_1201_example_solution1():
    assert func_1201('2023/1201/example1.txt') == 142+154


def test_1201_input_solution1():
    print(f"ans = {func_1201('2023/1201/input.txt')}")


def test_1201_example_solution3():
    assert func_1201_3('2023/1201/example1.txt') == 142+154


def test_1201_input_solution3():
    print(f"ans = {func_1201_3('2023/1201/input.txt')}")
