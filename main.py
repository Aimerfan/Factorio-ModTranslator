# main.py
import sys
import json
import deepdiff


def trans_file_parser(content: str):
    records = content.splitlines()
    record_dict = {}
    label = ''
    record_dict[label] = {}
    for record in records:
        record = record.strip()
        if not record:
            continue
        elif record[0] == '[':
            label = record[1:-1]
            record_dict[label] = {}
        else:
            tokens = record.split('=', 1)
            if len(tokens) != 2:
                print(f'record parse error "{tokens}"')
            record_dict[label][tokens[0]] = tokens[1]
    return record_dict


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('參數數量錯誤')

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        file_content = f.read()
        origin_dict = trans_file_parser(file_content)

    with open(sys.argv[2], 'r', encoding='utf-8') as f:
        file_content = f.read()
        new_dict = trans_file_parser(file_content)

    diff = deepdiff.DeepDiff(origin_dict, new_dict)
    print(diff.to_json())
