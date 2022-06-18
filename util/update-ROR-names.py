#!/usr/bin/env python3

# This script updates the ROR names in the CSV files given on the command line 
# to fit the names in the corresponding json files downloaded in the data/ directory (see util/retrieve-orgs-data.sh)
# Where this name equals the override name, the latter is cleared

import csv
import json
import shutil
import sys

for filename in sys.argv[1:]:
    filename_tmp = filename + ".tmp"
    with open( filename ) as fin:
        reader = csv.DictReader( fin )
        fields = reader.fieldnames
        with open( filename_tmp, 'w', newline='' ) as fout:
            writer = csv.DictWriter( fout, fields, dialect=reader.dialect, quoting=csv.QUOTE_MINIMAL )
            writer.writeheader()        
            for row in reader:
                ror_id = row['ROR_id']
                if ror_id != "":
                    with open( 'data/' + ror_id.replace( 'https://ror.org/', '' ) + '.json' ) as fx:
                        ror_record = json.load( fx )
                    row['ROR_Name'] = ror_record['name']
                    if row['ROR_Name'] == row['Override_Name_EN']:
                        row['Override_Name_EN'] = ''
                    if 'FundRef_id' in fields:
                        fundref_ids = ror_record['external_ids'].get('FundRef')
                        print( "was here: " + str(fundref_ids))
                        if fundref_ids != None:
                            preferred_fundref_id = fundref_ids['preferred']
                            row['FundRef_id'] = preferred_fundref_id if preferred_fundref_id != None else fundref_ids['all'][0]
                writer.writerow( row )
    
    shutil.move( filename_tmp, filename )
