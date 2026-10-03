# locgraph

A tool for drawing a graph of LoC per commit.

## Usage

Requires Python 3, Git, and `cloc` or `tokei` on your PATH.

```sh
cd /path/to/codebucket
/path/to/locgraph/locgraph.py /path/to/dump.csv
```

You can use the flag `-t` or `--tags` to tell `locgraph.py` to go through
every tag, instead of every commit.

You can use the flag `-T` or `--tokei` to tell `locgraph.py` to use `tokei`
instead of `cloc` for counting the lines of code.

You can pass your language to `locgraph.py` right after the output.

```sh
/path/to/locgraph/locgraph.py --tags --tokei /path/to/dump.csv Python
```
