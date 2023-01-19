from music21 import *

# Create a new stream
s = stream.Stream()

# Add notes to the stream
s.append(note.Note("C4", quarterLength = 1.0))
s.append(note.Note("D4", quarterLength = 1.0))
s.append(note.Note("E4", quarterLength = 1.0))
s.append(note.Note("F4", quarterLength = 1.0))
s.append(note.Note("G4", quarterLength = 1.0))
s.append(note.Note("A4", quarterLength = 1.0))
s.append(note.Note("B4", quarterLength = 1.0))
s.append(note.Note("C5", quarterLength = 1.0))

# Play the stream
s.show("midi")
