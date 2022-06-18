#!/bin/sh
#
# This script extract the ROR records of the ROR IDs listed in the organization.csv file from the given file, 
# indents them and places them in the data2/ directory
#

F=organizations.csv
T=tmp/extract-orgs.txt
D=data2

echo 'This script can run up to 30 minutes, please be patient'

rm -rf "$D"
mkdir -p "$D"/ tmp
echo '    }' >$T
grep -oh -e ',https://ror\.org/0........,' $F \
| LANG=C sort \
| sed -e 's/^,/        "id": "/' -e 's/,$/",/' >>$T
fgrep -n -f $T "$1" \
| fgrep -e ':    }' -e ':        "id"' \
| gawk -F: '/"id"/ { B=$1-1; R=gensub( /\/\/ror\.org\/(0[0-9a-z]{6}[0-9]{2})",/, "\\1", "g", $4 ) } /\}/ { if ( B > 0 ) { print B "," $1 "w '$D'/" R ".json" }; B = 0 }' \
| gsed -n -f - "$1"

./util/format-jsons.sh "$D"
