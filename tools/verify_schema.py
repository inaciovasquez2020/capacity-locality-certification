import json
import sys
from jsonschema import Draft202012Validator

def main():
    if len(sys.argv) != 3:
        print("usage: verify_schema.py schema.json cert.json", file=sys.stderr)
        return 2
    schema = json.load(open(sys.argv[1], "r", encoding="utf-8"))
    cert = json.load(open(sys.argv[2], "r", encoding="utf-8"))
    v = Draft202012Validator(schema)
    errs = sorted(v.iter_errors(cert), key=lambda e: e.path)
    if errs:
        for e in errs:
            print(f"schema error: {e.message}", file=sys.stderr)
        return 1
    print("ok")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
