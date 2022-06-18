#!/usr/bin/bash

find "$@" -name \*.json \
| while read F 
do
	python3 -m json.tool --no-ensure-ascii --sort-keys --tab <$F >$F.tmp && mv $F.tmp $F
done

	