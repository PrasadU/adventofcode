import re
non_digit = re.compile(r'[^\d\s]')
collapse_digit = re.compile(r'(\d).*(\d)')


def func_1201_3(file_name, debug = False):
    input_str = open(file_name).read()
    with_singles = non_digit.sub(r'', input_str.strip())
    print(with_singles)
    print("======")
    with_singles = collapse_digit.sub(r'\1\2 ', with_singles)
    print(with_singles)
    print("======")
    lines = re.split(r'\s+', with_singles)
    print(lines)
    sum = 0
    for linex in lines:
        line = linex.strip()
        if line != '':
            if len(line) == 2:
                sum += int(line)
            elif len(line) < 2:
                sum += int(line+line)
            elif len(line) > 2:
                print(f">>>>>>>>>>>> bad line {line}")
    return sum