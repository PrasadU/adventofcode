import re

non_digit = re.compile(r'[^\d\s]')
collapse_digit = re.compile(r'(\d).*(\d)')
teen_replace = re.compile(r'teen')

number_map = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', 'seven': '7', "eight": '8', "nine": '9'}

# def create_regex():
#     for k in number_map:
#         reg_str = f"{k}"
#         replace_str = number_map[k]
#         regex_list.append(re.compile(reg_str))
#         replace_list.append(replace_str)
#         print(f"{k} > {reg_str} >> {replace_str}")
#         reg_str = f"{k}\\D*(\\s|$)"
#         replace_str = "r" + number_map[k] + "\\1"
#         regex_list.append(re.compile(reg_str))
#         replace_list.append(replace_str)
#         print(f"{k} > {reg_str} >> {replace_str}")


def repl(m):
    return f"{number_map[m.group(1)]}"


def func_1201_4(file_name, debug = False):
    # create_regex()
    # print("---------------------------------------")
    update_str = open(file_name).read().strip()
    # for regex, replace_str in zip(regex_list, replace_list):
    #     update_str = regex.sub(replace_str, update_str)
    #     print(update_str)
    #     print("---------------------------------------")
        
    update_str = teen_replace.sub('', update_str)
    print(update_str)
    print("---------------------------------------")
    update_str = re.sub(r'(?<!\d)(one|two|three|four|five|six|seven|eight|nine)', repl, update_str)
    print(update_str)
    print("---------------------------------------")
    update_str = re.sub(r'(one|two|three|four|five|six|seven|eight|nine)(?!\d)', repl, update_str)
    print(update_str)
    print("---------------------------------------")
    with_singles = non_digit.sub(r'', update_str)
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
        print(f"{line} >> {sum}")
    return sum