#!/bin/bash
cd "$(dirname "$0")"

pybabel compile -d ./translations
