# README

This repository contains a list of words that are not commonly used in Australian English, but are commonly used in US English. The list is intended to help writers and editors avoid using US spelling in Australian English documents created in Microsoft Word.

The list is not exhaustive and may be updated over time as new words are added or removed. If you have any suggestions for words to add or remove, please feel free to submit a pull request.

## Folder Structure

The project is organized as follows:

- `src/`: Contains Python scripts for processing the word lists.
- `data/`: Contains input and intermediate data files.
- `output/`: Contains generated output files.
- `docs/`: Contains documentation files.
- `tests/`: Contains test scripts (if applicable).
- `LICENSE` and `README.md`: Root-level files for licensing and project overview.

## Features

- Comprehensive list of -ize base verbs in US English.
- Automatic expansion of base verbs into all word forms.
- Integration with Hunspell for optional manual review of generated words.
- Easy installation for Microsoft Word exclusion dictionaries.

## Installation Pre-requisites

The installation notes below are intended for the Microsoft Office 365 installation.
For all other Microsoft Word version installation instructions, please refer to http://wordfaqs.ssbarnhill.com/ExcludeWordFromDic.htm

## Installation

- Close Microsoft Word.
- Navigate to the folder where the existing exclusion file lives. 
  - On Windows: Open the following folder in Windows Browser `%AppData%\Microsoft\UProof`
  - On Mac: Open the following folder in Finder `~/Library/Group Containers/UBF8T346G9.Office/`
- Open the `ExcludeDictionaryEN0C09.lex` file in a text editor.
  - If the file doesn't exist, create a new text file in that folder and name it `ExcludeDictionaryEN0C09.lex`.
- Copy the content of the `data/ExcludeDictionaryEN0c09-additions.lex` file to the `ExcludeDictionaryEN0C09.lex` file you opened in the previous step.
- Save the updated `ExcludeDictionaryEN0C09.lex` file and close the text editor.
- Reopen Microsoft Word and the new words should now be excluded from the spell check.

## Contributing

If you have suggestions for additional words to add to the exclusion list, please feel free to submit a pull request with the new words added to the `data/ExcludeDictionaryEN0c09-additions.lex` file. Please ensure that the new words are in the correct format and do not contain any duplicates.

## Tools Used

On a MacBook Pro:
- Visual Studio Code for editing the text files.
- Microsoft Word for testing the exclusion list.
- GitHub for version control and collaboration.
- GitHub Copilot for generating the list of words and their forms based on the custom prompt.
- Daniel Imms - https://marketplace.visualstudio.com/items?itemName=Tyriar.sort-lines
- Python for expanding the base verbs into all their forms. (Python script: `src/generate_word_forms.py`)
- Hunspell for flagging generated words that may merit manual review against US English. https://github.com/hunspell/hunspell

## Supporting Wordlists

This project integrates data from the following publicly available wordlists:

1. **[dwyl/english-words](https://github.com/dwyl/english-words)**
   - License: Unlicense
   - Content: Over 466,000 English words, including -ize verbs. Available in plain text and JSON formats.

2. **[dariusk/corpora](https://github.com/dariusk/corpora)**
   - License: CC0
   - Content: JSON-based corpora with common nouns, adjectives, and verbs. Useful for linguistic experiments.

3. **[atebits/Words](https://github.com/atebits/Words)**
   - License: CC0
   - Content: Wordlist from the Letterpress game, including US, UK, and Australian spellings.
