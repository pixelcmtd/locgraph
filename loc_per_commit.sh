#!/bin/sh

{
echo '[{}'

[ "$1" = "-t" -o "$2" = "-t" ] && lol='--tags --simplify-by-decoration'
lel='cloc --json --vcs=git' ; kek=cloc
[ "$1" = "-T" -o "$2" = "-T" ] && { lel='tokei -o json' ; kek=tokei ; }

for commit in $(git log $lol --pretty=oneline | cut -d' ' -f1 | tac) ; do
        git checkout $commit >/dev/null || exit 1
        echo ',{"commit":"'$(echo $commit | cut -c 1-7)'"'
        echo ',"tag":"'$(git tag -l --points-at HEAD)'","'$kek'":'
        $lel .
        echo '}'
done

echo ']'
} | jq -c .
