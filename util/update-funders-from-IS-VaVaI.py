#!/usr/bin/env python3

# This script updates the 

import csv
import json
import shutil
from urllib.request import urlopen

fundersData = json.loads( urlopen('https://www.isvavai.cz/dokumenty/open-data/ciselniky/poskytovatel-podpory.jsonld').read() )
funders = {}
for X in fundersData['položky']:
    code = X['kód']
    if code != 'USC':
        funders[code] = { "IS_VaVaI_code" : code, "IS_VaVaI_Name_CS" : X['název']['cs'], "IS_VaVaI_Name_EN" : X['název']['en'] }

with open( 'funders.csv' ) as fin:
    reader = csv.DictReader( fin )
    with open( 'funders.csv.tmp', 'w', newline='' ) as fout:
        writer = csv.DictWriter( fout, reader.fieldnames, dialect=reader.dialect, quoting=csv.QUOTE_MINIMAL )
        writer.writeheader()        
        for row in reader:
            isvavai_code = row['IS_VaVaI_code']
            if isvavai_code in funders:
                row["IS_VaVaI_Name_CS"] = funders[isvavai_code]["IS_VaVaI_Name_CS"]
                row["IS_VaVaI_Name_EN"] = funders[isvavai_code]["IS_VaVaI_Name_EN"]
                del funders[isvavai_code]
            writer.writerow( row )
        for X in funders.values():
            writer.writerow( X )

shutil.move( 'funders.csv.tmp', 'funders.csv' )
