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
w.writerow(['tag/commit', 'blank', 'comment', 'code', 'files'])

for commit in commits:
    cloc = {'blank': 0, 'comment': 0, 'code': 0, 'nFiles': 0}
    if lang in commit['cloc']:
        cloc = commit['cloc'][lang]
    w.writerow([commit['tag'] if commit['tag'] != '' else commit['commit'],
                cloc['blank'],
                cloc['comment'],
                cloc['code'],
                cloc['nFiles']])
