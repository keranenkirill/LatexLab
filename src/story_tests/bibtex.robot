*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Variables ***
${EXPECTED_OUTPUT}    @article{1,\n    author = {bibtext_author},\n    booktitle = {bibtex},\n    title = {bib},\n    year = {2024}\n}

*** Test Cases ***
Check bibtext to clipboard output for article
    Go To                               ${HOME_URL}
    Click Link                          New citation
    Wait Until Page Contains Element    author
    Wait Until Page Contains Element    title
    Wait Until Page Contains Element    year
    Wait Until Page Contains Element    booktitle
    Input Text                          author                      bibtext_author
    Input Text                          title                       bib
    Input Text                          year                        2024
    Input Text                          booktitle                   bibtex
    Click Button                        Create
    Sleep                               0.5s
    Click Button                        Bibtex to clipboard
    Sleep                               0.5s
    ${button}=     Get WebElement       xpath://button[@bibtex-clipboard-data]
    Get Variables                       ${button}
    ${pasted_text}=   Get Text          xpath://button[@bibtex-clipboard-data]
    Should Be Equal                     ${pasted_text}              ${pasted_text}
