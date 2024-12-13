*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations


*** Test Cases ***
Only the filtered citation is visible to the user"

    Go To    ${HOME_URL}

 
    Click Link                New citation
    Wait Until Element Is Visible    author
    Input Text               author    TestAuthor1
    Input Text               title     TestTitle1
    Input Text               year      2020
    Input Text               journal   TestJournal1
    Click Button             Create

    Wait Until Page Contains            TestAuthor1

    Click Link                New citation
    Wait Until Element Is Visible    author
    Input Text               author    TestAuthor2
    Input Text               title     TestTitle2
    Input Text               year      2021
    Input Text               journal   TestJournal2
    Click Button             Create

    Wait Until Page Contains            TestAuthor2

    Input Text               id=citationSearch   TestAuthor1

    Sleep    2s
    ${first_citation_style}=    Execute JavaScript    return document.querySelectorAll('.citation-item')[0].style.display
    Should Be Equal    ${first_citation_style}    ${EMPTY}

    ${second_citation_style}=    Execute JavaScript    return document.querySelectorAll('.citation-item')[1].style.display
    Should Be Equal    ${second_citation_style}    none
