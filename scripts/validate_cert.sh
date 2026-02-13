#!/usr/bin/env bash
set -euo pipefail

command -v ajv >/dev/null 2>&1 || exit 0

for s in docs/spec/*.schema.json; do
  for d in docs/examples/*.json; do
    ajv validate -s "$s" -d "$d"
  done
done
