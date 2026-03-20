#!/usr/bin/env python3
"""Expand -ize base verbs into all their word forms.

Usage:
    python3 generate_word_forms.py < ../data/baseverbs.txt | sort > ../output/newwords.txt 
"""
import sys

# Extra forms beyond the standard 9, keyed on base verb.
# Standard forms (always generated): base, -es, -ed, -ing, -able, -ation,
# -ations, -er, -ers.
EXTRAS = {
    'aggrandize':   ['aggrandizement', 'aggrandizements'],
    'antagonize':   ['antagonism', 'antagonisms', 'antagonist', 'antagonists', 'antagonistic'],
    'baptize':      ['baptism', 'baptisms'],
    'criticize':    ['criticism', 'criticisms'],
    'exorcize':     ['exorcism', 'exorcisms', 'exorcist', 'exorcists'],
    'hypnotize':    ['hypnotism', 'hypnotist', 'hypnotists'],
    'idealize':     ['idealism', 'idealist', 'idealists', 'idealistic'],
    'mesmerize':    ['mesmerism'],
    'organize':     ['organizational'],
    'plagiarize':   ['plagiarism', 'plagiarist', 'plagiarists'],
    'proselytize':  ['proselytism', 'proselyte', 'proselytes'],
    'recognize':    ['recognition', 'recognitions'],
    'terrorize':    ['terrorism', 'terrorist', 'terrorists'],
    'vandalize':    ['vandalism', 'vandal', 'vandals'],
}

# Words where the standard -ation/-ations forms are NOT valid and should be
# suppressed (replaced by entries in EXTRAS instead).
NO_ATION = {
    'recognize',
    'baptize',
    'exorcize',
    'hypnotize',
    'mesmerize',
    'plagiarize',
    'proselytize',
    'terrorize',
    'vandalize',
    'antagonize',
    'idealize',
}

for line in sys.stdin:
    base = line.strip()
    if not base or not base.endswith('ize'):
        continue

    stem = base[:-1]  # strip trailing 'e': "personalize" -> "personaliz"

    print(base)                 # personalize
    print(stem + 'es')          # personalizes
    print(stem + 'ed')          # personalized
    print(stem + 'ing')         # personalizing
    print(stem + 'able')        # personalizable
    if base not in NO_ATION:
        print(stem + 'ation')       # personalization
        print(stem + 'ations')      # personalizations
    print(stem + 'er')          # personalizer
    print(stem + 'ers')         # personalizers

    for extra in EXTRAS.get(base, []):
        print(extra)
