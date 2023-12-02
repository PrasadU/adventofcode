import os.path
import re

first_digit_pattern = re.compile(r'^[\D\s]*(\d).*$')
last_digit_pattern = re.compile(r'^.*(\d)[\D\s]*$')

number_map = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', 'seven': '7', "eight": '8', "nine": '9'}


def repl2(m):
    print(f"looking up {m.group(1)}")
    return number_map[m.group(1)]


def func_1201_5(file_name, debug = False):
    total = 0
    build__log = "build/1201P2.log"
    if debug and os.path.exists(build__log):
        os.remove(build__log)
    log = open(build__log, "a")
    with open(file_name) as f:
        for line in f:
            update_str = re.sub(r'(?<!\d)(one|two|three|four|five|six|seven|eight|nine)', repl2, line)
            print(f"F: {update_str}")
            update_str = re.sub(r'(one|two|three|four|five|six|seven|eight|nine)(?!(\d|one|two|three|four|five|six|seven|eight|nine))', repl2, update_str)
            print(f"B: {update_str}")
            digits = first_digit_pattern.sub(r'\1', update_str).strip() + last_digit_pattern.sub(r'\1', update_str).strip()
            if debug:
                log.write(f"{line.strip()} >> {digits}\n")
            total += int(digits)
            print(f"{line.strip()} >> {digits} >> {total}")
            
    return total
