#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/build.py
python3 scripts/qa.py

npx wrangler pages deploy dist \
  --project-name practical-ai-workflows \
  --branch main \
  --commit-dirty=true
