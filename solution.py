#!/usr/bin/python3
# Solution to "major-or-minor"
# @author: Jack Golden

note_names = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

a, b, c = map(int, input().split())

def find_type(root, third, fifth):
    if (third - root) % 12 == 3:
        return "minor"
    if (third - root) % 12 == 4:
        return "major"

# Check for each note if it's the root by seeing if the other notes are 3 or 4 and 7 semitones above it.
# Start by assuming `a` is the root:
if ((b - a) % 12 == 3 or (b - a) % 12 == 4) and (c - a) % 12 == 7:
    print(note_names[a % 12], find_type(a, b, c))
elif ((c - a) % 12 == 3 or (c - a) % 12 == 4) and (b - a) % 12 == 7:
    print(note_names[a % 12], find_type(a, c, b))
# Next, assume `b` is the root:
elif ((a - b) % 12 == 3 or (a - b) % 12 == 4) and (c - b) % 12 == 7:
    print(note_names[b % 12], find_type(b, a, c))
elif ((c - b) % 12 == 3 or (c - b) % 12 == 4) and (a - b) % 12 == 7:
    print(note_names[b % 12], find_type(b, c, a))
# Finally, assume `c` is the root:
elif ((a - c) % 12 == 3 or (a - c) % 12 == 4) and (b - c) % 12 == 7:
    print(note_names[c % 12], find_type(c, a, b))
else:
    print(note_names[c % 12], find_type(c, b, a))

