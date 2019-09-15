# **pymused**

pymused is a Python library for music theory, aimed at harmonic analysis. It's inspired and modeled after the great Javascript library, [teoria](https://github.com/saebekassebil/teoria).  Currently early in development.

If you are looking for in depth computer-aided musicology, I would highly suggest MIT's [music21](https://web.mit.edu/music21/).

## Current Features

- Pitch object:  Handles accidental, octave, key, and midi information
- Interval object:  Handles the interval between two pitches with semitones, quality, and degree information.

## Example Usage

```python
from pymused import *

# Pitches
csharp = Pitch('C#4')
csharp.freq()              # Returns: 277.18
csharp.key()               # Returns: 41
csharp.midi()              # Returns: 61
csharp.name()              # Returns: 'C'
csharp.accidental()        # Returns: '#'
csharp.accidental_value()  # Returns: 1
csharp.octave()            # Returns: 4

# Intervals
bflat = Pitch('Bb3')
g = Pitch('G4')
majorsixth = Interval(bflat, g)
majorsixth.value()      # Returns: 6
majorsixth.quality()    # Returns: 'M'
majorsixth.string()     # Returns: 'M6'
majorsixth.semitones()  # Returns: 9
majorsixth.coord        # Returns: [5, 9]

# Interval also accepts string input
Interval('P12').semitones()  # Returns: 19
```

## Future Features

- Chord object
- Progression object
- Key object

## TODO

- ##### Pitch object
  - [x] Base methods off of coord (e.g. C4 -> [0, 0, 4])
  - [ ] Pitch.from_tuple(name, accidental, octave)
- [ ] Pitch.from_key(key): Set pitch from key on piano. Use most common names (optional sharp or flat key arg)
  
- ##### Interval object

  - [x] Interval.from_between(pitch, pitch): Set interval from two pitches
  - [x] Interval.from_string(name): Set interval from interval name
  - [ ] Interval.from_to(pitch, interval_name): Returns pitch
