[![cs](https://img.shields.io/badge/lang-cs-white.svg)](./README.cs.md)
[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)
&larr; <i>English here</i>

# Přiřazení identifikátoru ROR organizacím z IS VaVaI

Tato datová sada obsahuje přiřazení identifikátoru [ROR](https://ror.org/) (Research Organizations Registry) 
organizacím z [IS VaVaI](https://www.isvavai.cz/) (Informační systém výzkumu, vývoje a inovací).

## Rozsah

V IS VaVaI jsou uvedeny organizace, které získaly podporu na výzkum, vývoj či inovace z veřejných rozpočtů ČR 
nebo které se účastnily takových projektů a které vykazovaly výsledky takových aktivit.

## Cíle

Tato datová sada chce pomoci zapojit údaje IS VaVaI do mezinárodního kontextu.

Je také jedním z výstupů [Pracovní skupiny pro správu vědeckých dat v ČR](https://www.wg-rdm.cz/).

## Aktuální stav

16.01.2022: 111 organizací:
- Všech 26 veřejných vysokých škol, jedna vojenská a jedna státní vysoká škola jsou pokryty. Toto jsou organizace uvedené v [Přílohách 1 a 2 zákona o vysokých školách (zák. č. 111/1998 Sb.)](https://www.zakonyprolidi.cz/cs/1998-111#prilohy).
- Z [54 ústavů a podpůrných organizačních jednotek](https://www.avcr.cz/cs/o-nas/struktura/pracoviste-av/) [Akaademie věd České republiky](https://www.avcr.cz/) je pokrytých 53.
  - [Slovanskému ústavu Akademie věd České republiky](http://www.slu.cas.cz/index.html) dosud nebyl identifikátor ROR přidělen. [Požádal jsem](https://github.com/ror-community/ror-updates/issues/431) o něj u ROR.
- Dále jsou pokryty některé další organizace: většinou ty s nejvíce výsledky v RIV. 

## Formát

Data jsou umístěna v souboru **[organizations.csv](organizations.csv)**, 
což je soubor typu CSV v kódování UTF-8
s následujícími sloupci:
1. IS_VaVaI_id: Identifikátor organizace v IS VaVaI.
2. IS_VaVaI_Name_CS: Jméno organizace v češtině podle IS VaVaI.
3. ROR_id: Přiřazený identifikátor ROR.
4. ROR_Name: Jméno organizace podle ROR.
5. Override_Name_EN: Přepisující jméno v angličtině, pokud jsme toho názoru, že ROR_Name by si zasloužilo vylepšení.
6. Notes: Poznámky o přiřazení, zejména o jeho omezeních.

Tento soubor má být udržován setříděný pomocí skriptu [util/sort-orgs.sh](util/sort-orgs.sh).

## Podmínky použití

Tato datová sada je dána k volnému užití.

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license" href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" /></a>
  <br />
  V míře, která je v souladu s platným právem přípustná, 
  <a rel="dct:publisher" href="https://orcid.org/0000-0001-8985-152X"><span property="dct:title">Jan Dvořák</span></a>
  i další přispěvatelé
  se tímto vzdávají všech autorských práv i práv souvisejících a příbuzných, stejně jako všech souvisejících nároků, včetně nároků uplatnitelných u soudu, 
  které se vztahují k <span property="dct:title" xml:lang="cs">Přiřazení identifikátoru ROR organizacím z IS VaVaI</span> =
  <span property="dct:title" xml:lang="en">Mapping IS VaVaI Organizations to ROR</span>.
  Toto dílo je zveřejněno z <span property="vcard:Country" datatype="dct:ISO3166" content="CZ" about="https://github.com/jdvorak001/isvavai-orgs-ror-mapping">České republiky</span>.
</p>
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  To the extent possible under law,
  <a rel="dct:publisher" href="https://orcid.org/0000-0001-8985-152X"><span property="dct:title">Jan Dvořák</span></a> and other contributors
  have waived all copyright and related or neighboring rights to
  <span property="dct:title">Mapping IS VaVaI Organizations to ROR</span>.
  This work is published from <span property="vcard:Country" datatype="dct:ISO3166" content="CZ" about="https://github.com/jdvorak001/isvavai-orgs-ror-mapping"> Czech Republic</span>.
</p>

## Příspěvky

Pokud jste nalezli identifikátor ROR organizace, kterou ještě nemáme,
[upravte soubor organizations.csv](https://github.com/jdvorak001/isvavai-orgs-ror-mapping/edit/main/organizations.csv)
zde na GitHubu a na jeho konec přidejte řádek v odpovídající struktuře (viz [Formát](#formát)).
Před uložením se ujistěte, že Váš řádek je správně zobrazen, pokud vyberete "Preview".
Při commitování použijte hlášku ve tvaru "Add ROR id for ${anglické jméno organizace}" a zahajte Pull request.

Alternativně, pokud jste dohledali větší počet identifikátorů ROR, [pošlete mi](mailto:jan.dvorak@ff.cuni.cz) 
je v sešitu a já je přidám za Vás.

Navržením příspěvku souhlasíte s [Podmínkami použití](#podmínky-použití).
