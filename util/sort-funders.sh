#!/bin/sh
#
# This script sorts the contents of the funders.csv file
#

F=funders.csv
PIPEFILE=/tmp/isvavai-funders-heading.csv

rm -f $PIPEFILE 2>/dev/null
mkfifo -m 600 $PIPEFILE || exit 1
sed <$F -e '1w '"$PIPEFILE" -e '1d' \
| LANG=C sort \
| cat "$PIPEFILE" - >$F.tmp \
&& mv $F.tmp $F \
&& echo Total $( expr $( wc -l <$F ) - 1 ) records