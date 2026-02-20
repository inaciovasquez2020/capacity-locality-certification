import json
import sys
import hashlib
try:
import jsonschema
except ImportError:
print("missing dependency: jsonschema (pip install jsonschema)", file=sys.stderr)
sys.exit(2)
def sha256_bytes(b: bytes) -> str:
return hashlib.sha256(b).hexdigest()
def load_json(path: str):
with open(path, "rb") as f:
data = f.read()
return data, json.loads(data.decode("utf-8"))
def main():
if len(sys.argv) != 3:
print("usage: python3 tools/bom/verify_bom_cert.py <schema.json> <cert.json>", file=sys.stderr)
sys.exit(2)
schema_path, cert_path = sys.argv[1], sys.argv[2]
_, schema = load_json(schema_path)
cert_bytes, cert = load_json(cert_path)

jsonschema.validate(instance=cert, schema=schema)

sig = cert.get("signature")
if sig:
    payload_hash = sig.get("payload_hash_sha256", "")
    if payload_hash and payload_hash != sha256_bytes(cert_bytes):
        raise SystemExit("payload_hash_sha256 mismatch")

print("OK: schema-validated")
if name == "main":
main()
