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

# 3. Spell-check against US English — review unknown_words.txt and remove any invalid base verbs from baseverbs.txt, then repeat from step 2
hunspell -d en_US -l < newwords.txt | sort -u > unknown_words.txt

# 4. Merge new words into the dictionary, sort case-insensitively (diacritic-insensitive), and deduplicate
cat newwords.txt ExcludeDictionaryEN0c09-additions.lex \
  | LC_ALL=en_US.UTF-8 sort -fu \
  > lex_merged.txt \
  && mv lex_merged.txt ExcludeDictionaryEN0c09-additions.lex
```

