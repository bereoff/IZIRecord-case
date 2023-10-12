#!/usr/bin/env bash

set -e

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

$@