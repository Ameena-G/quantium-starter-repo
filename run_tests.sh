#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

# Activate virtual environment
if [ -d "venv" ]; then
  source venv/Scripts/activate
else
  echo "Virtual environment not found"
  exit 1
fi

# Run test suite
pytest

# If pytest succeeds, exit with 0
exit 0
