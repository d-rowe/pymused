# **pymused**

pymused is a Python library for music theory, aimed at harmonic analysis. It's inspired by the fantastic [teoria](https://github.com/saebekassebil/teoria) js library.  Currently early in active development.

If you are looking for in depth computational musicology, check out MIT's [music21](https://github.com/cuthbertLab/music21) project.

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
Pitch('Bb4').transpose('m-10').frequency()  # 196.0
```

## Future Features

- Chord object
- Progression object
- Key object

## TODO

- ##### Scale
  - [ ] Create tests
  - [ ] Add more arg options (from_pitches, from_intervals, from_name)
  - [ ] Type method which returns scale type
  - [ ] Name method which returns scale name (root + type)
  
- ##### Pitch
  - [ ] Pitch.from_key(key): Set pitch from key on piano. Use most common names (optional sharp or flat key arg)
  
- ##### Documentation
  - [ ] Create documentation section
