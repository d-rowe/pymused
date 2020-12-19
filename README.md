# **Pymused**

Pymused is a music theory library for Python, aimed at harmonic analysis.  This library is currently early in active development.

If you are looking to perform in depth computational musicology, check out MIT's [music21](https://github.com/cuthbertLab/music21) toolkit.

## Table of Contents

- [Examples](#examples)
- [Documentation](#documentation)
- [Contributing](#contributing)

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
aflat.transpose(perf_fifth)  # Pitch(Eb5)

# We can use an interval string as well
aflat.transpose('P5')  # Pitch(Eb5)

# We can also use the + or - operators
aflat + perf_fifth  # Pitch(Eb5)

aflat - perf_fifth  # Pitch(Db4)
```

Identify a chord and return the jazz notation

```python
Chord(['g', 'e', 'bb', 'd']).jazz()  # 'Em7b5/G'
```

Now with chaining, let's figure out what the frequency of a pitch a minor tenth below Bb4 is

```python
Pitch('Bb4').transpose('m-10').frequency()  # 196.0
```

## Contributing
If you are interesting in contributing, feel free to create a pull request.
Here's a list of future features I have, feel free to add your own as well.

- ##### Scale
  - [ ] Create more tests
  - [ ] Add from_pitches arg parser
  - [ ] Verify args in all parsing methods
  - [ ] Type method which returns scale type
  - [ ] Name method which returns scale name (root + type)
  - [ ] Method to return scale at length (e.g. create two octave scales, scale up to fifth, etc.)
  
- ##### Chord
  - [ ] Add from_name method
  - [ ] Add support for voicings
  - [ ] Verify args in all parsing methods
  - [ ] Add numbered inversions

- ##### Pitch
  - [ ] Pitch.from_key(key): Set pitch from key on piano. Use most common names (optional sharp or flat key arg)
  
- ##### README
  - [ ] Add Chord and Scale examples
  - [ ] Trim down examples
