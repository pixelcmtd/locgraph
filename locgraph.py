#!/usr/bin/env python3

import csv
import json
from sys import argv

if len(argv) < 3:
    print('Usage: locgraph <commits.json> <out.csv> [<lang>]')
    exit(1)

commits = json.load(open(argv[1], 'r'))
commits.pop(0)

w = csv.writer(open(argv[2], 'w'))
w.writerow(['tag/commit', 'blank', 'comment', 'code', 'files'])

for commit in commits:
    lang = argv[3] if len(argv) > 3 else 'SUM' if 'cloc' in commit else 'Total'
    if 'cloc' in commit and lang in commit['cloc']:
        cloc = commit['cloc'][lang]
        w.writerow([commit['tag'] if commit['tag'] != '' else commit['commit'],
                    cloc['blank'],
                    cloc['comment'],
                    cloc['code'],
                    cloc['nFiles']])
    elif 'tokei' in commit and lang in commit['tokei']:
        tokei = commit['tokei'][lang]
        w.writerow([commit['tag'] if commit['tag'] != '' else commit['commit'],
                    tokei['blanks'],
                    tokei['comments'],
                    tokei['code'],
                    -1])
    else:
        w.writerow([commit['tag'] if commit['tag'] != '' else commit['commit'], -1, -1, -1, -1])
