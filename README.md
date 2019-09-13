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
c = Pitch('C4')
c.freq()  # Returns: 261.63
c.key     # Returns: 40
c.midi    # Returns: 60
c.octave  # Returns: 4

# Intervals
bflat = Pitch('Bb3')
g = Pitch('G4')
majorsixth = Interval(bflat, g)
majorsixth.degree                # Returns: 6
majorsixth.quality()             # Returns: 'M'
majorsixth.semitones             # Returns: 9
majorsixth.toString()            # Returns: 'M6'

```

