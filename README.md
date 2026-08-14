# locgraph

A tool for drawing a graph of LoC per commit.

## Usage

```sh
cd /path/to/codebucket
/path/to/locgraph/loc_per_commit.sh > /path/to/locgraph/dump.json
cd /path/to/locgraph
./locgraph.py dump.json dump.csv
```

You can use the flag `-t` to tell `loc_per_commit.sh` to go through every tag,
instead of every commit.

You can use the flag `-T` to tell `loc_per_commit.sh` to use `tokei` instead of
`cloc` for counting the lines of code.

You can pass your language to `locgraph.py` right after the output.
