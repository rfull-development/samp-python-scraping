#!/bin/bash
# Copyright (c) 2023 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
pip install --upgrade pip
pip freeze > requirements.txt

DEPEND_LIST=`pip list --outdated --format=json | jq -r "map(.name) | join(\" \")"`
if [ -z "$DEPEND_LIST" ]; then
    echo "No packages to upgrade"
    exit 0
fi
pip install --upgrade $DEPEND_LIST
pip freeze > requirements.txt
