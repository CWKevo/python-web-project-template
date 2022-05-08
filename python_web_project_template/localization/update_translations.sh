#!/bin/bash
cd "$(dirname "$0")"

pybabel update -i messages.pot -d translations
