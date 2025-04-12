import random
import json
from music21 import converter
import subprocess
import os
import requests

def get_song_midi(songdata):
	id = songdata.get('tune_id')
	url = f"https://thesession.org/tunes/{id}/abc"
	response = requests.get(url)
	abc_notation = response.text
	versions = converter.parseData(abc_notation, format='abc')
	music = versions[0]

	midi_path = f"tune_{songdata.get('tune_id')}.mid"
	music.write('midi', fp = midi_path)
	return midi_path

def get_tune(style):
	tunes = []

	with open("extras/tunes.json", "r", encoding="utf-8") as songlist:
		songs = json.load(songlist)
		for song in songs:
			if song.get('type') == style:
				tunes.append(song)
		
	melody = random.choice(tunes)
	midi = get_song_midi(melody)
	return midi

def synthesize_singing(midi, lyrics, output):
	subprocess.run([
		"python", "-m", "midi2voice",
		"-l", lyrics,
		"-m", midi
	], check=True)

	if os.path.exists("voice.wav"):
		os.rename("voice.wav", output)
	return