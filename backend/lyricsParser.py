import json
import re
import pyphen
import random

dic = pyphen.Pyphen(lang='en_US')

# REMOVE SPECIAL CHARACTERS
def remove_special_characters(lyrics):
	try:
		removed_characters = "".join(ch for ch in lyrics if ch.isalnum() or ch.isspace())
		return removed_characters
	except Exception as e:
		print(f"Error: {e}")
		return None

# ADDING TIDDLY DIDDLIES
def make_funny(lyrics, meter, abc):
	final_lyrics = remove_special_characters(lyrics)
	with open('data/words.json', 'r') as file:
		data = json.load(file)
	
	lilts = data['filler_words']
	for i in range(3):
		final_lyrics += ' '
		final_lyrics += random.choice(lilts)
	
	return final_lyrics

# REPLACE WORDS WITH IRISH ONES
def irishify(lyrics, meter, abc):
	new_lyrics = make_funny(lyrics, meter, abc)
	with open('data/words.json', 'r') as file:
		data = json.load(file)
	
	changable = data['changable_words']
	changed = data['changed_words']

	for original, replacement in zip(changable, changed):
		pattern = r'\b' + re.escape(original) + r'\b'
		new_lyrics = re.sub(pattern, replacement, new_lyrics, flags=re.IGNORECASE)
	return new_lyrics