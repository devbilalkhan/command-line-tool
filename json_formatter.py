"""
Simple command line tool in python
"""
from encodings import utf_8
import sys
import json


def json_format(data, sort_keys=True, indent=4):
    """
    Returns a formatted JSON string
    """
    return json.dumps(json.loads(data), sort_keys=sort_keys, indent=indent)


def main(path, sort_keys):
    """
    Entry point
    """
    print(sort_keys)
    with open(path, "r", encoding=utf_8) as _f:
        print(json_format(_f.read(), sort_keys))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(
            """
    This is a CLI tool in python that formats JSON.
    It takes a single sort flag as an option.


    Usage: python3 json_formatter.py [--flag] [path to json file]
    """
        )
        sys.exit(0)

    # SORT_FLAG = True if "--sort" in sys.argv else False
    SORT_FLAG = bool("--sort" in sys.argv)
    main(sys.argv[-1], sort_keys=SORT_FLAG)
