import random
import json
from music21 import converter, interval
import subprocess
import os
import requests

def get_song_midi(songdata):
	id = songdata.get('tune_id')
	meter = songdata.get('meter')
	abc = songdata.get('abc')
	print(id)
	url = f"https://thesession.org/tunes/{id}/abc"
	response = requests.get(url)
	abc_notation = response.text
	versions = converter.parseData(abc_notation, format='abc')
	music = versions[0]

	midi_path = f"tune_{songdata.get('tune_id')}.mid"
	music.write('midi', fp = midi_path)
	return midi_path, meter, abc

def get_tune(style):
	tunes = []

	with open("data/tunes.json", "r", encoding="utf-8") as songlist:
		songs = json.load(songlist)
		for song in songs:
			if song.get('type') == style:
				tunes.append(song)
		
	melody = random.choice(tunes)
	midi, meter, abc = get_song_midi(melody)
	return midi, meter, abc

def synthesize_singing(midi, lyrics, output):
    try:
        result = subprocess.run([
            "python", "-m", "midi2voice",
            "-l", lyrics,
            "-m", midi
        ], capture_output=True, text=True, check=True)
        
        if result.returncode != 0:
            print(f"Error in subprocess: {result.stderr}")
            print(f"Output: {result.stdout}")
            return

        if os.path.exists("voice.wav"):
            os.rename("voice.wav", output)
    except subprocess.CalledProcessError as e:
        print(f"Subprocess failed: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return


def transpose_down(midi):
	high_midi = converter.parse(midi)
	octave_down = interval.Interval(-12)

	low_midi = high_midi.transpose(octave_down)
	low_midi.write("midi", fp = midi)
	return midi