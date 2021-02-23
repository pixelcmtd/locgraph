#!/usr/bin/env python3

import json
import csv
from sys import argv

lang = 'SUM'
if len(argv) > 3:
    lang = argv[3]

commits = json.load(open(argv[1], 'r'))
commits.pop(0)

w = csv.writer(open(argv[2], 'w'))
w.writerow(['commit', 'blank', 'comment', 'code', 'files'])

for commit in commits:
    cloc = commit['cloc'][lang]
    w.writerow([commit['commit'],
                cloc['blank'],
                cloc['comment'],
                cloc['code'],
                cloc['nFiles']])
