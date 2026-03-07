# Persona
You are a cunning linguist. You have a distaste for US spelling in Australian English documents.

# Task

Generate a comprehensive list of all -ize **base verbs** in US English, one per line, alphabetically sorted. Cover all common, technical, and domain-specific -ize verbs.

Output only the base verbs (e.g. `personalize`), one per line, no commentary.
Output to file `baseverbs.txt`.

# Post processing

On a mac, run through:

```bash
# 1. Check the existing dictionary for any base verbs the LLM may have missed
grep -E '^[a-zA-Z]+ize$' ExcludeDictionaryEN0c09-additions.lex \
  | tr '[:upper:]' '[:lower:]' \
  | sort > existing_baseverbs.txt

comm -23 existing_baseverbs.txt <(sort baseverbs.txt) > missed_baseverbs.txt

# Review missed_baseverbs.txt, then merge any valid ones into baseverbs.txt (sorted, no duplicates)
cat baseverbs.txt missed_baseverbs.txt | sort -fu > baseverbs_merged.txt \
  && mv baseverbs_merged.txt baseverbs.txt

# 2. Expand base verbs into all word forms
python3 expand_ize.py < baseverbs.txt | sort > newwords.txt

# 3. Spell-check against US English for review only — dump any unrecognized generated forms to unknown_words.txt, but do not remove base verbs from baseverbs.txt on that basis alone
hunspell -d en_US -l < newwords.txt | sort -u > unknown_words.txt

# Review unknown_words.txt manually if desired. Since this is an exclusion list, keep the generated words unless you identify something clearly invalid.
# Do not merge unknown_words.txt separately; it is only a review report because all of its entries already come from newwords.txt.

# 4. Merge all generated words into the dictionary, sort case-insensitively (diacritic-insensitive), and deduplicate
cat newwords.txt ExcludeDictionaryEN0c09-additions.lex \
  | LC_ALL=en_US.UTF-8 sort -fu \
  > lex_merged.txt \
  && mv lex_merged.txt ExcludeDictionaryEN0c09-additions.lex
```

