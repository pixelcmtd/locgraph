# locgraph

A tool for drawing a graph of LoC per commit.

## Usage

```sh
cd /path/to/codebucket
/path/to/locgraph/loc_per_commit.sh > /path/to/locgraph/dump.json
cd /path/to/locgraph
./locgraph.py dump.json dump.csv
```
