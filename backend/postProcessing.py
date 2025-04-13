import librosa
import soundfile as sf

def chipmunkify(audio_path, output_path):
    """
    Applies a chipmunk effect by increasing pitch and speed of the audio.
    Saves the result to output_path.
    """
    # Load the audio
    y, sr = librosa.load(audio_path, sr=None)

    # Convert to STFT
    D = librosa.stft(y)

    # Apply time-stretching
    D_fast = librosa.effects.time_stretch(librosa.magphase(D)[0], rate=1.5)

    # Reconstruct audio from stretched magnitude using Griffin-Lim
    y_fast = librosa.griffinlim(D_fast)

    # Now pitch shift the time-stretched audio
    y_chipmunk = librosa.effects.pitch_shift(y_fast, sr=sr, n_steps=4)

    # Export
    sf.write(output_path, y_chipmunk, sr)

# Example usage
#chipmunkify("../extras/najboljsi.wav", "../extras/chp.wav")
