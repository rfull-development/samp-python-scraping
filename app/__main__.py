# Copyright (c) 2023 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
import json
import sys

from .analyze.sample import analyze
from .collect.sample import collect

argv = sys.argv
if len(argv) < 2:
    print("Usage: python -m app <url>")
    sys.exit(1)
url = argv[1]
req = collect(url)
results = analyze(req)
print(results)
