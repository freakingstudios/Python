from pydub import AudioSegment

# Load audio files
intro = AudioSegment.from_file("intro.mp3")
verse1 = AudioSegment.from_file("verse1.mp3")
chorus = AudioSegment.from_file("chorus.mp3")
verse2 = AudioSegment.from_file("verse2.mp3")
outro = AudioSegment.from_file("outro.mp3")

# Concatenate audio files
song = intro + verse1 + chorus + verse2 + outro

# Export the final song
song.export("song.mp3", format="mp3")
