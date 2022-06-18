#!/usr/bin/env python3

# This script updates the ROR names of the organizations from json files downloaded in the data/ directory (see util/retrieve-orgs-data.sh)
# Where this name equals the override name, the latter is cleared

import csv
import json
import shutil

with open( 'organizations.csv' ) as fin:
    reader = csv.DictReader( fin )
    with open( 'organizations.csv.tmp', 'w', newline='' ) as fout:
        writer = csv.DictWriter( fout, reader.fieldnames, dialect=reader.dialect, quoting=csv.QUOTE_MINIMAL )
        writer.writeheader()        
        for row in reader:
            ror_id = row['ROR_id']
            with open( 'data/' + ror_id.replace( 'https://ror.org/', '' ) + '.json' ) as fx:
                ror_record = json.load( fx )
            row['ROR_Name'] = ror_record['name']
            if row['ROR_Name'] == row['Override_Name_EN']:
                row['Override_Name_EN'] = ''
            writer.writerow( row )

shutil.move( 'organizations.csv.tmp', 'organizations.csv' )
