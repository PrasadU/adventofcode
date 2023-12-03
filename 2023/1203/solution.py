import regex as re


def read_schema(file_name):
    lines = open(file_name).readlines()
    line_count = len(lines)
    symbol_pos = []
    symbol_hits = {}
    line_valid_pos = {}
    for i in range(line_count):
        line_valid_pos[i] = []
    symbol_id = 0
    for ln, line in enumerate(lines):
        m_symbols = re.finditer(r'([^.\d])', line.strip())
        l_len = len(line)
        if m_symbols:
            for ms in m_symbols:
                symbol_id += 1
                symbol = ms.group()
                start_pos = ms.start()
                symbol_pos.append((ln, start_pos, symbol, symbol_id))
                symbol_hits[symbol_id] = []
                x = start_pos
                y = start_pos
                if start_pos > 0:
                    x = start_pos - 1
                if start_pos < l_len-1:
                    y = start_pos + 1
                valid_pos = (x, y, symbol_id)
                if ln > 0:
                    line_valid_pos[ln-1].append(valid_pos)
                line_valid_pos[ln].append(valid_pos)
                if ln < line_count-1:
                    line_valid_pos[ln+1].append(valid_pos)
    valid_parts = []
    invalid_parts = []
    total = 0
    for ln, line in enumerate(lines):
        m_codes = re.finditer(r'(\d+)', line.strip())
        if m_codes:
            for m_code in m_codes:
                code = int(m_code.group(1))
                csp = m_code.start()
                cep = m_code.end()-1
                is_valid = False
                for slot in line_valid_pos[ln]:
                    is_valid = (csp < slot[0] and cep >= slot[0]) \
                               or (csp <= slot[1] and cep > slot[1]) \
                               or (csp >= slot[0] and cep <= slot[1])
                    print(f"checking line: {ln} code:{code} at {csp}, {cep} for slot {slot[0]},{slot[1]} >> {is_valid}")
                    if is_valid:
                        valid_parts.append(code)
                        total += code
                        symbol_hits[slot[2]].append(code)
                        break
                if not is_valid:
                    invalid_parts.append(code)
    print(f"symbol count: {len(symbol_pos)}, locations: {symbol_pos}")
    print(f"positions: {valid_parts}")
    print(f"invalid positions: {invalid_parts}")
    astrik_symbol_ids = [spos[3] for spos in symbol_pos if spos[2] == '*']
    gear_total = 0
    for sid in astrik_symbol_ids:
        hits = symbol_hits[sid]
        if len(hits) == 2:
            gear_total += hits[0] * hits[1]
    print(f'* symbol ids: {astrik_symbol_ids}')
    print('==================================')
    print(f'* symbol id count: {len(astrik_symbol_ids)}')
    print(f"valid total: {total}")
    print(f"gear  total: {gear_total}")
    return valid_parts, invalid_parts, total, gear_total
