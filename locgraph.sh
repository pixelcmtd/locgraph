#!/bin/sh

commits="$(git log --pretty=oneline | cut -d' ' -f1 | tac)"
