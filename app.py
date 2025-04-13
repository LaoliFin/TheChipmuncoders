from flask import Flask, render_template, request, send_file
from backend.melodyProcessing import get_tune, synthesize_singing, transpose_down
from backend.lyricsParser import irishify
import os

app = Flask(__name__)

@app.route('/')
def index():
	"""Renders the main page."""
	return render_template('index.html')

@app.route('/card')
def card():
    try:
        with open("lyrics.txt", "r", encoding="utf-8") as f:
            lyrics = f.read()
    except FileNotFoundError:
        lyrics = "No lyrics found."
    return render_template('card.html', lyrics=lyrics)

@app.route('/generate', methods=['POST'])
def generate_singing():
	if os.path.exists("output.wav"):
		os.remove("output.wav")
	if os.path.exists("voice.xml"):
		os.remove("voice.xml")
	
	data = request.get_json()
	lyrics = data.get('text')
	style = data.get('style')
	
	lyrics = irishify(lyrics)
	lyrics_file = "lyrics.txt"
	with open(lyrics_file, "w", encoding="utf-8") as f:
		f.write(lyrics)

	melody_file = get_tune(style)
	melody_file = transpose_down(melody_file)
	generated_singing = "output.wav"
	synthesize_singing(melody_file, lyrics_file, generated_singing)

	if os.path.exists(lyrics_file):
		os.remove(lyrics_file)
	if os.path.exists(melody_file):
		os.remove(melody_file)
	return send_file(generated_singing, as_attachment=False, mimetype='audio/wav')

if __name__ == '__main__':
	# Note: Debug mode should be False in production
	app.run(debug=True)