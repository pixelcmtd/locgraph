#!/bin/sh

echo '[{}'

for commit in $(git log --pretty=oneline | cut -d' ' -f1 | tac) ; do
        git checkout $commit >/dev/null
        echo ',{"commit":"'$(echo $commit | cut -c 1-7)'","cloc":'
        cloc --json .
        echo '}'
done

echo ']'
