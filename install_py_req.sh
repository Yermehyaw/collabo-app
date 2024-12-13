#!/usr/bin/env bash
"""
Install python requirements in virtual env

NOTE: You must had already set up your virtual environment before running this file

"""
path="$PATH"

if [[ "$path" == /usr/bin* ]]; then
    echo 'ERROR: VENV NOT CREATED, Set up a vitual environment first'
    return 1
else
    req_file="./requirements.txt"
    echo 'Installing python requirements'
    if [[ -e "$req_file" ]]; then
	pip install -r requirements.txt
    else
	echo "requirements.txt NOT FOUND"
    fi
fi
