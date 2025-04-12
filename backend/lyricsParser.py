import json
import re
# RAZDELI PO VERZIH


# REMOVE SPECIAL CHARACTERS
def remove_special_characters(lyrics):
    try:
        removed_characters = "".join(ch for ch in lyrics if ch.isalnum() or ch.isspace())
        return removed_characters
    except Exception as e:
        print(f"Error: {e}")
        return None


# REPLACE WORDS WITH IRISH ONES
def irishify(lyrics):
    new_lyrics = lyrics
    with open('../data/words.json', 'r') as file:
        data = json.load(file)
    
    changable = data['changable_words']
    changed = data['changed_words']

    for original, replacement in zip(changable, changed):
        pattern = r'\b' + re.escape(original) + r'\b'
        new_lyrics = re.sub(pattern, replacement, new_lyrics, flags=re.IGNORECASE)
    return new_lyrics

# ADD FIXES FOR PRONOUNCIATION

print(irishify(remove_special_characters("Hello... tes!t tes?t te#st my My MY tea wh of you little man boy")))