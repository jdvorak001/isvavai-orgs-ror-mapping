[![en](https://img.shields.io/badge/lang-en-white.svg)](./README.md)
[![cs](https://img.shields.io/badge/lang-cs-red.svg)](./README.cs.md)
&larr; <i>česky zde</i>

# Mapping IS VaVaI Organizations and Funders to ROR

This dataset provides the mapping of organizations and funders from the [IS VaVaI](https://www.isvavai.cz/) 
(the national [CRIS](https://en.wikipedia.org/wiki/Current_research_information_system) 
in [Czechia](https://en.wikipedia.org/wiki/Czech_Republic)) 
to [ROR](https://ror.org/), the international Research Organization Registry.

## Scope

The IS VaVaI tracks organizations that received funding for research, technology development and innovation 
from public budgets in Czechia or that have participated in such funded projects. Also the funders of these projects are registered.

## Aim

This dataset is intended to help put the research information collected in the IS VaVaI into an international context.

It is part of the activities of the [Working Group for Research Data Management in the Czech Republic](https://www.wg-rdm.cz/).

## Changelog

2022-06-18: add the funders from the IS VaVaI

2022-06-18: update the ROR names in our file with those from API following the [ROR 1.1 release](https://doi.org/10.5281/zenodo.6657125)

2022-06-03: replace "... of the CAS" with "... of the Czech Academy of Sciences" in the English override names

2022-01-20: 112 organizations:
- All the 26 public universities, one military university and one state university are covered. These are the organizations listed in Annexes 1 and 2 of the [Higher Education Act](https://www.msmt.cz/areas-of-work/tertiary-education/the-higher-education-act) of the Czech Republic.
- All the [54 institutes and support units](https://www.avcr.cz/en/about-us/cas-structure/research-institutes/) of the [Academy of Sciences of the Czech Republic](https://www.avcr.cz/en/about-us/mission-of-the-cas/) are covered. 
- Some other organizations, mostly those which had reported considerable numbers of research outputs in the IS VaVaI/RIV, are covered. 

## Format

### Organizations — [organizations.csv](organizations.csv)
The data about the research performing organizations, 
a UTF-8 encoded file in the Comma Separated Values format
with the following columns:
1. IS_VaVaI_id: The identifier of the organization in IS VaVaI.
2. IS_VaVaI_Name_CS: The name of the organization in Czech as recorded in the IS VaVaI.
3. ROR_id: The ROR id of the organization.
4. ROR_Name: The name of the organization from ROR. Mostly in English.
5. Override_Name_EN: An override of the English name if we think the one provided in ROR could be improved.
6. Notes: Any notes about the mapping, esp. about a possible uncertainty.

This file is to be kept sorted: [util/sort-orgs.sh](util/sort-orgs.sh) is the script to sort it.

### Funders — [funders.csv](funders.csv)
The data about the IS VaVaI funders, 
a UTF-8 encoded file in the Comma Separated Values format
with the following columns:
1. IS_VaVaI_code: The code of the funder in IS VaVaI.
2. IS_VaVaI_Name_CS: The name of the funder in Czech as recorded in the IS VaVaI.
3. IS_VaVaI_Name_EN: The name of the funder in English as recorded in the IS VaVaI.
4. ROR_id: The ROR id of the organization.
5. ROR_Name: The name of the organization from ROR. Mostly in English.
6. Override_Name_EN: An override of the English name if we think the one provided in ROR could be improved.
7. FundRef_id: The Crossref Fundref ID (use the prefix `https://doi.org/10.13039/` to access the [Funder Registry](https://www.crossref.org/services/funder-registry/) record).
8. Notes: Any notes about the mapping, esp. about a possible uncertainty.

This file is to be kept sorted: [util/sort-funders.sh](util/sort-funders.sh) is the script to sort it.

## Access

You can always get the latest version of the mapping files from  
[https://github.com/jdvorak001/isvavai-orgs-ror-mapping/raw/main/organizations.csv](https://github.com/jdvorak001/isvavai-orgs-ror-mapping/raw/main/organizations.csv) and
[https://github.com/jdvorak001/isvavai-orgs-ror-mapping/raw/main/funders.csv](https://github.com/jdvorak001/isvavai-orgs-ror-mapping/raw/main/funders.csv), respectively.

Alternatively, you can clone this repo and access the `organizations.csv` and `funders.csv` files there. Don't forget to `git pull` from time to time.

## Terms of use

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license" href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" /></a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher" href="https://orcid.org/0000-0001-8985-152X"><span property="dct:title">Jan Dvořák</span></a> and other contributors
  have waived all copyright and related or neighboring rights to
  <span property="dct:title">Mapping IS VaVaI Organizations to ROR</span>.
  This work is published from <span property="vcard:Country" datatype="dct:ISO3166" content="CZ" about="https://github.com/jdvorak001/isvavai-orgs-ror-mapping"> Czech Republic</span>.
</p>

## Contributing

If you found the ROR id for an institution, 
[edit the organizations.csv](https://github.com/jdvorak001/isvavai-orgs-ror-mapping/edit/main/organizations.csv) file 
here on GitHub, place the organization as a new line at the end of the file. 
Please make sure the line follows the [format description](#format) above,
use Preview to check your changes before committing.
When committing, use a message like "Add ROR id for ${English name}" and start a pull request.

Alternatively, if you have looked up a larger number of ROR ids, [send](mailto:jan.dvorak@ff.cuni.cz) them to me 
in a spreadsheet file and I'll add them for you.

By contributing you agree to the the [Terms of use](#terms-of-use).

## Contributors

The project of organizing, maintaining, extending and publishing this dataset 
is led by [Jan Dvořák](https://orcid.org/0000-0001-8985-152X)
in affiliation with the [Institute of Information Studies and Librarianship](https://uisk.ff.cuni.cz/en/) 
of the [Charles University](https://ror.org/024d6js02).