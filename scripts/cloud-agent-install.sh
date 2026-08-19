#!/usr/bin/env bash
set -euo pipefail

# Idempotent Cloud Agent install: verify Python and run solution smoke tests.
python3 --version
python3 scripts/verify_environment.py
