#!/bin/bash
cd "$(dirname "$0")"

pybabel extract -F ./babel.cfg -k _l -o ./messages.pot ../../.
