#!/bin/sh
#
# This script retrieves the current ROR records of the ROR IDs listed in the organization.csv file from the ROR API, 
# indents them and places them in the data/ directory
#

F=organizations.csv
D=data

mkdir -p "$D"/
grep -oh -e ',https://ror\.org/0........,' $F \
| sed -e 's/,https:\/\/ror\.org\//https:\/\/api.ror.org\/organizations\//' -e 's/,$//' \
| wget -nv -P "$D"/ -i -

for X in "$D"/0??????[0-9][0-9]
do
	python3 -m json.tool --no-ensure-ascii --sort-keys --tab <"$X" >"$X".json && rm "$X"
done
