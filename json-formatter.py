import os
import sys
import json


def json_format(data, sort_keys=True, indent=4):
    return json.dumps(json.loads(data), sort_keys=sort_keys, indent=indent)

def main(path):
    with open(path, 'r') as _f:
        print(
            json_format(_f.read())
        )


if __name__ == '__main__':
    main(sys.argv[-1])
    