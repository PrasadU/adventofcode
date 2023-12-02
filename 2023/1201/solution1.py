import re
main_replace = re.compile(r'\D*(\d)\S*(\d)\D*')
single_pre = re.compile(r'(\d)(?!\s)\D+')
single_post = re.compile(r'(?<!\s)\D+(\d)\s')
non_digit = re.compile(r'\s\D+\s')
non_digit_only = re.compile(r'\D')


def func_1201(file_name, debug = False):
    input_str = open(file_name).read()
    with_singles = main_replace.sub(r' \1\2 ', input_str.strip())
    print(with_singles)
    print("======")
    with_singles = single_pre.sub(r' \1\1 ', with_singles)
    print(with_singles)
    print("======")
    with_singles = single_post.sub(r' \1\1 ', with_singles)
    print(with_singles)
    print("======")
    lines = re.split(r'\s+', with_singles)
    print(lines)
    sum = 0
    for linex in lines:
        line = linex.strip()
        if non_digit_only.match(line):
            print(f"skipping {line}")
        elif line != '':
            sum += int(line)
            if len(line) < 2:
                print(f">>>>>>>>>>>> bad line {line}")
    return sum