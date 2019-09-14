# pymused

pymused is a Python library for music theory, aimed at harmonic analysis. It's inspired and modeled after the great Javascript library, [teoria](https://github.com/saebekassebil/teoria).  Currently early in development.

If you are looking for in depth computer-aided musicology, I would highly suggest MIT's [music21](https://web.mit.edu/music21/).

## Current Features

- Pitch object:  Handles accidental, octave, key, and midi information
- Interval object:  Handles the interval between two pitches with semitones, quality, and degree information.

## Example Usage

```python
from pymused import *

# Pitches
c = Pitch('C#4')
c.freq()            # Returns: 277.18
c.key()             # Returns: 41
c.midi()            # Returns: 61
c.name              # Returns: 'C'
c.accidental        # Returns: '#'
c.accidental_val()  # Returns: 1
c.octave            # Returns: 4

# Intervals
bflat = Pitch('Bb3')
g = Pitch('G4')
majorsixth = Interval(bflat, g)
majorsixth.degree      # Returns: 6
majorsixth.quality()   # Returns: 'M'
majorsixth.semitones   # Returns: 9
majorsixth.toString()  # Returns: 'M6'

```

## Future Features

- Chord object
- Score object

## TODO

- ##### Pitch object

  - [ ] Pitch.fromKey(key): Creates Pitch from key on piano. Use most common names (optional sharp or flat key arg)

- ##### Interval object

  - [ ] Interval(name): Creates Interval from name (e.g. M7, m-2)
  - [ ] Interval.between(pitch, pitch): Creates Interval from two pitches.