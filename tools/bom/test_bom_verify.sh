#!/usr/bin/env bash
set -euo pipefail

SCHEMA="certs/bom/schema/BOM_CERT.schema.json"
POS="certs/bom/examples/BOM_CERT_POS_0001.json"
NEG="certs/bom/examples/BOM_CERT_NEG_0001.json"

python3 tools/bom/verify_bom_cert.py "$SCHEMA" "$POS"

if python3 tools/bom/verify_bom_cert.py "$SCHEMA" "$NEG" >/dev/null 2>&1; then
  echo "FAIL: NEG example unexpectedly validated"
  exit 1
else
  echo "OK: NEG example rejected as expected"
fi
