# README

This repository contains a list of words that are not commonly used in Australian English, but are commonly used in US English. The list is intended to help writers and editors avoid using US spelling in Australian English documents created in Microsoft Word.

The list is not exhaustive and may be updated over time as new words are added or removed. If you have any suggestions for words to add or remove, please feel free to submit a pull request.

The list is organized alphabetically.

This list was produced using a custom prompt that generated a comprehensive list of all the different forms of the "-ize" words in US English, including noun forms, adjective forms, verb conjugations, and direct synonym alternates. The prompt also ensured that any words already present in the existing dictionary were ignored and not duplicated. (See Dictionary Creation Prompt.md for more details on the prompt used to generate the list with the forms of each word.)

Hunspell is used as a review aid for generated forms, not as a hard filter. Any unrecognized words are written to `unknown_words.txt` for optional manual inspection before merging the expanded list into the exclusion dictionary.

# Installation Pre-requisites

The installation notes below are intended for the Microsoft Office 365 installation.
For all other Microsoft Word version installation instructions, please refer to http://wordfaqs.ssbarnhill.com/ExcludeWordFromDic.htm

# Installation

- Close Microsoft Word.
- Navigate to the folder where the existing exclusion file lives. 
  - On Windows: Open the following folder in Windows Brower %AppData%\Microsoft\UProof
  - On Mac: Open the following folder in Finder ~/Library/Group Containers/UBF8T346G9.Office/User Content.localized/Startup.localized/Word
- Open the ExcludeDictionaryEN0C09.lex file in a text editor.
  - - If the file doesn't exist, create a new text file in that folder and name it ExcludeDictionaryEN0C09.lex
- Copy the content of the /Users/arbux/GitHub/un-australian-spelling-exclusion-list/ExcludeDictionaryEN0c09-additions.lex file to the ExcludeDictionaryEN0C09.lex folder you opened in the previous step.
- Save the updated ExcludeDictionaryEN0C09.lex file and close the text editor.
- Reopen Microsoft Word and the new words should now be excluded from the spell check.

# Contributing

If you have suggestions for additional words to add to the exclusion list, please feel free to submit a pull request with the new words added to the ExcludeDictionaryEN0C09-additions.lex file. Please ensure that the new words are in the correct format and do not contain any duplicates.

# Tools Used

On a MacBook Pro:
- Visual Studio Code for editing the text files.
- Microsoft Word for testing the exclusion list.
- GitHub for version control and collaboration.
- Github Copilot for generating the list of words and their forms based on the custom prompt.
- Daniel Imms - https://marketplace.visualstudio.com/items?itemName=Tyriar.sort-lines
- Python for expanding the base verbs into all their forms. (Python script: expand_ize.py)
- Hunspell for flagging generated words that may merit manual review against US English. https://github.com/hunspell/hunspell
