#!/usr/bin/env python3

import argparse
import json
import subprocess

parser = argparse.ArgumentParser(description='Count lines of code per commit.')
parser.add_argument('-t', '--tags', action='store_true',
                    help='go through tags instead of every commit')
parser.add_argument('-T', '--tokei', action='store_true',
                    help='use tokei instead of cloc')
args = parser.parse_args()

log = ['git', 'log', '--pretty=format:%H']
if args.tags:
    log.extend(['--tags', '--simplify-by-decoration'])

counter = 'tokei' if args.tokei else 'cloc'
command = ['tokei', '-o', 'json'] if args.tokei else ['cloc', '--json', '--vcs=git']
commits = [{}]

for commit in reversed(subprocess.check_output(log, text=True).splitlines()):
    subprocess.run(['git', 'checkout', commit], stdout=subprocess.DEVNULL,
                   check=True)
    tag = subprocess.check_output(['git', 'tag', '-l', '--points-at', 'HEAD'],
                                  text=True).strip()
    stats = json.loads(subprocess.check_output(command + ['.'], text=True))
    commits.append({'commit': commit[:7], 'tag': tag, counter: stats})

print(json.dumps(commits, separators=(',', ':')))
