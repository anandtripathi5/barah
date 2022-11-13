#!/usr/bin/env bash

set -e
set -x

#black --check .
isort --check-only apis
flake8 .