*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Variables ***
${bibtex_author}    author = {bibtext_author}
${bib_title}        title = {bib_title}
${bib_year}         year = {2024}
${bib_title}        title = {bib_title}

*** Test Cases ***
Check bibtext to clipboard output for article
    Go To                               ${HOME_URL}
    Click Link                          New citation
    Wait Until Page Contains Element    author
    Wait Until Page Contains Element    title
    Wait Until Page Contains Element    year
    Wait Until Page Contains Element    booktitle
    Input Text                          author                      bibtext_author
    Input Text                          title                       bib_title
    Input Text                          year                        2024
    Input Text                          booktitle                   bibbook_title
    Click Button                        Create
    Click Button                        Bibtex to clipboard
    ${pasted_text}=    Get Element Attribute    xpath://button[@onclick="toClipboard(this)"]    bibtex-clipboard-data
    Should Contain    ${pasted_text}    ${bibtex_author}
    Should Contain    ${pasted_text}    ${bib_title}
    Should Contain    ${pasted_text}    ${bib_year}
    Should Contain    ${pasted_text}    ${bib_title}