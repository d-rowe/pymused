# **pymused**

pymused is a Python library for music theory, aimed at harmonic analysis. It's inspired and modeled after the great Javascript library, [teoria](https://github.com/saebekassebil/teoria).  Currently early in development.

If you are looking for in depth computer-aided musicology library, I would highly suggest MIT's [music21](https://web.mit.edu/music21/).

## Current Features

- Pitch object:  Handles accidental, octave, key, and midi information
- Interval object:  Handles the interval between two pitches with semitones, quality, and degree information.

## Examples

Create a pitch

```python
from pymused import *

aflat = Pitch('Ab4') # 4th octave Ab
```

Create an interval

```python
# Create with the string name
perf_fifth = Interval('P5')

# Create from the distance between two pitches
perf_fifth = Interval(Pitch('C4'), Pitch('G4'))

# or with two pitch strings
perf_fifth = Interval('C4', 'G4')

# Descending intervals have a - between the quality and degree
desc_fourth = Interval('P-4')
```

Transpose a pitch

```python
# Transpose the pitch by the interval we created
aflat.transpose(perf_fifth)  # Pitch('Eb5')

# We can use an interval string as well
aflat.transpose('P5')  # Pitch('Eb5')

# We can also use the + or - operators
aflat + perf_fifth  # Pitch('Eb5')

aflat - perf_fifth  # Pitch('Db4')
```

Now with chaining, let's figure out what the frequency of a pitch a minor tenth below Bb4 is.

```python
Pitch('Bb4').transpose('m-10').freq()  # 196.0
```

## Future Features

- Accidental object
- Scale object
- Chord object
- Progression object
- Key object

## TODO

- ##### Pitch object
  - [x] Base methods off of coord ([degree, semitone])
  - [x] Pitch.interval(name): Returns a Pitch an interval away
  - [ ] Pitch.from_tuple(name, accidental, octave)
  - [ ] Pitch.from_key(key): Set pitch from key on piano. Use most common names (optional sharp or flat key arg)
  - [ ] Add support for n flats, sharps, and diminishments/augmentations. Done with accidental object.
  
- ##### Interval object
  - [x] Interval.from_between(pitch, pitch): Set interval from two pitches
  - [x] Interval.from_string(name): Set interval from interval name
  - [x] Add add and sub methods that return interval
  
- ##### Documentation
  - [ ] Create documentation section
