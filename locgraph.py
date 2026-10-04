#!/usr/bin/env python3

import argparse
import csv
import json
import subprocess

parser = argparse.ArgumentParser(description='Write lines of code per commit to CSV.')
parser.add_argument('-t', '--tags', action='store_true',
                    help='go through tags instead of every commit')
parser.add_argument('-T', '--tokei', action='store_true',
                    help='use tokei instead of cloc')
parser.add_argument('output', help='CSV output path')
parser.add_argument('lang', nargs='?', help='language to count, defaults to all languages')
args = parser.parse_args()

log = ['git', 'log', '--pretty=format:%H']
if args.tags:
    log.extend(['--tags', '--simplify-by-decoration'])

counter = 'tokei' if args.tokei else 'cloc'
command = ['tokei', '-o', 'json'] if args.tokei else ['cloc', '--json', '--vcs=git']
commits = []

for commit in reversed(subprocess.check_output(log, text=True).splitlines()):
    subprocess.run(['git', 'checkout', commit], stdout=subprocess.DEVNULL,
                   check=True)
    tag = subprocess.check_output(['git', 'tag', '-l', '--points-at', 'HEAD'],
                                  text=True).strip()
    stats = json.loads(subprocess.check_output(command + ['.'], text=True))
    commits.append({'commit': commit[:7], 'tag': tag, counter: stats})

with open(args.output, 'w', newline='') as output:
    w = csv.writer(output)
    w.writerow(['tag/commit', 'blank', 'comment', 'code', 'files'])

    for commit in commits:
        lang = args.lang if args.lang is not None else 'SUM' if 'cloc' in commit else 'Total'
        line = [commit['tag'] if commit['tag'] != '' else commit['commit']]
        if 'cloc' in commit and lang in commit['cloc']:
            cloc = commit['cloc'][lang]
            line.extend([cloc['blank'],
                         cloc['comment'],
                         cloc['code'],
                         cloc['nFiles']])
        elif 'tokei' in commit and lang in commit['tokei']:
            tokei = commit['tokei'][lang]
            line.extend([tokei['blanks'],
                         tokei['comments'],
                         tokei['code'],
                         -1])
        else:
            line.extend([-1, -1, -1, -1])
        w.writerow(line)
