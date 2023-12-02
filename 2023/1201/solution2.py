import os.path
import re

first_digit_pattern = re.compile(r'^[\D\s]*(\d).*$')
last_digit_pattern = re.compile(r'^.*(\d)[\D\s]*$')


def func_1201_2(file_name, debug = False):
    total = 0
    build__log = "build/1201.log"
    if debug and os.path.exists(build__log):
        os.remove(build__log)
    log = open(build__log, "a")
    with open(file_name) as f:
        for line in f:
            digits = first_digit_pattern.sub(r'\1', line).strip() + last_digit_pattern.sub(r'\1', line).strip()
            if debug:
                log.write(f"{line.strip()} >> {digits}\n")
            total += int(digits)
    return total
