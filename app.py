from flask import Flask, render_template, request, send_file
from backend.melodyProcessing import get_song_midi, get_tune, synthesize_singing
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
	"""Renders the main page."""
	return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_singing():
	if os.path.exists("output.wav"):
		os.remove("output.wav")
	if os.path.exists("output.wav"):
		os.remove("output.wav")
	
	data = request.get_json()
	text = data.get('text')
	style = data.get('style')
	
	lyrics = text # call the lyricsParser functions
	with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8') as lyrics_file:
			lyrics_file.write(text)
			lyrics_path = lyrics_file.name

	melody_path = get_tune(style)
	generated_singing = "output.wav"
	synthesize_singing(melody_path, lyrics_path, generated_singing)

	if os.path.exists(lyrics_path):
		os.remove(lyrics_path)
	if os.path.exists(melody_path):
		os.remove(melody_path)
	return send_file(generated_singing, as_attachment=False, mimetype='audio/wav')

if __name__ == '__main__':
	# Note: Debug mode should be False in production
	app.run(debug=True)