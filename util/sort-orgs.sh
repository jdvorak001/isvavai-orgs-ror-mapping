#!/bin/sh
#
# This script sorts the contents of the organization.csv file
#

F=organizations.csv
sed <$F -e '1w /tmp/isvavai-orgs-heading.csv' -e '1d' \
| LANG=C sort \
| cat /tmp/isvavai-orgs-heading.csv - >$F.tmp \
&& mv $F.tmp $F