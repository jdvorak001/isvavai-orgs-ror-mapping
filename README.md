# Mapping IS VaVaI Organizations to ROR

This dataset provides the mapping of organizations from the [IS VaVaI](https://www.isvavai.cz/) 
(the national [CRIS](https://en.wikipedia.org/wiki/Current_research_information_system) 
in [Czechia](https://en.wikipedia.org/wiki/Czech_Republic)) 
to [ROR](https://ror.org/), the international Research Organization Registry.

## Scope

The IS VaVaI tracks organizations that received funding for research, technology development and innovation 
from public budgets in Czechia or that have participated in such funded projects.

## Aim

This dataset is intended to help put the research information collected in the IS VaVaI into an international context.

It is part of the activities of the [Working Group for Research Data Management](https://www.wg-rdm.cz/).

## Format

The data is held in **[organizations.csv](organizations.csv)**, 
a UTF-8 encoded file in the Comma Separated Values format
with the following columns:
1. IS_VaVaI_id: The identifier of the organization in IS VaVaI.
2. IS_VaVaI_Name_CS: The name of the organization in Czech as recorded in the IS VaVaI.
3. ROR_id: The ROR id of the organization.
4. ROR_Name_EN: The English name of the organization from ROR.
5. Override_Name_EN: An override of the English name if we think the one provided in ROR could be improved.
6. Notes: Any notes about the mapping, esp. about a possible uncertainty.

## Terms of use

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://orcid.org/0000-0001-8985-152X">
    <span property="dct:title">Jan Dvořák</span></a>
  and other contributors
  have waived all copyright and related or neighboring rights to
  <span property="dct:title">Mapping IS VaVaI Organizations to ROR</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="CZ" about="https://github.com/jdvorak001/isvavai-orgs-ror-mapping">
  Czech Republic</span>.
</p>

## Contributing

If you found the ROR id for an institution, 
[edit the organizations.csv](https://github.com/jdvorak001/isvavai-orgs-ror-mapping/edit/main/organizations.csv) file 
here on GitHub, locate the line with the organization, place the ROR id and the English name from ROR there.
Make sure you check your changes in the Preview before committing.
When committing, start a pull request with the title "Add ROR id for ${English name}".

Alternatively, if you have looked up a larger number of ROR ids, send them to me 
in a spreadsheet file or some other similar form and I'll add them for you.

By contributing you agree to the the [Terms of use](#terms-of-use).
