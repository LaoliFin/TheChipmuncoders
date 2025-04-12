import json
import re
import random
# RAZDELI PO VERZIH


#ADD DIDDLYDEIDEEDOHS
#TODO: make it linked to syllables instead
def make_funny(lyrics):
    with open('data/words.json', 'r') as file:
        data = json.load(file)

    tiddles = data['filler_words']
    tiddles_iter = iter(tiddles)

    def insert_word(match):
        word = random.choice(tiddles)
        return f".{word}{match.group(1)}"

    modified = re.sub(r'\.(\S)', insert_word, lyrics)
    return modified

# REMOVE SPECIAL CHARACTERS
def remove_special_characters(lyrics):
    new_lyrics = make_funny(lyrics)
    try:
        removed_characters = "".join(ch for ch in new_lyrics if ch.isalnum() or ch.isspace())
        return removed_characters
    except Exception as e:
        print(f"Error: {e}")
        return None


# REPLACE WORDS WITH IRISH ONES
def irishify(lyrics):
    new_lyrics = remove_special_characters(lyrics)
    with open('data/words.json', 'r') as file:
        data = json.load(file)
    
    changable = data['changable_words']
    changed = data['changed_words']

    for original, replacement in zip(changable, changed):
        pattern = r'\b' + re.escape(original) + r'\b'
        new_lyrics = re.sub(pattern, replacement, new_lyrics, flags=re.IGNORECASE)
    return new_lyrics

# ADD FIXES FOR PRONOUNCIATION
print(irishify(remove_special_characters(make_funny("Hello... tes!t tes?t te#st my My MY tea wh of you. little man boy"))))