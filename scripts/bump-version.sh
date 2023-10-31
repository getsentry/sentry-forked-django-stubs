#!/usr/bin/env bash
set -euxo pipefail

if ! grep -E '^.*\+sentry[0-9]+' <<< "$2"; then
    : "version must be D.D.D+sentryD got: $2"
    exit 1
fi
sed -i "s/^    version="'"'".*"'"'",$/    version="'"'"$2"'"'",/" setup.py
