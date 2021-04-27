#!/bin/sh

{
echo '[{}'

[ "$1" = "-t" ] && lol='--tags --simplify-by-decoration'

for commit in $(git log $lol --pretty=oneline | cut -d' ' -f1 | tac) ; do
        git checkout $commit >/dev/null || exit 1
        echo ',{"commit":"'$(echo $commit | cut -c 1-7)'"'
        echo ',"tag":"'$(git tag -l --points-at HEAD)'","cloc":'
        cloc --json --vcs=git .
        echo '}'
done

echo ']'
} | jq -c .
