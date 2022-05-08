#!/bin/bash
cd "$(dirname "$0")"

pybabel init -i ./messages.pot -d ./translations -l $1
