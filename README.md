# **pymused**

pymused is a Python library for music theory, aimed at harmonic analysis. It's inspired by the fantastic [teoria](https://github.com/saebekassebil/teoria) js library.  This library is currently early in active development.

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

Now with chaining, let's figure out what the frequency of a pitch a minor tenth below Bb4 is.

```python
Pitch('Bb4').transpose('m-10').frequency()  # 196.0
```

## Documentation
#### 		Pitch(spn | coord)

​			spn: Scientific pitch notation (e.g. 'Ab4', 'C3')

​			coord: Coordinate array

##### 						Pitch.name() -> str

​			Returns letter name of note with no accidental or octave (e.g. A, B, C).

##### 						Pitch.accidental() -> str

​			Returns accidental (e.g. '#', 'b', 'x').

##### 						Pitch.octave() -> int

​			Returns octave (e.g. 4, 5).

##### 						Pitch.string() -> str

​			Returns scientific pitch notation of pitch (e.g. 'Ab4', 'Bb3').

##### 					Pitch.simple() -> str

​			Returns name and accidental without octave (e.g. 'Ab', 'C')

##### 		Pitch.accidental_value() -> int

​			Returns the semitone modification of the accidental, where 'b' = -1, '#' = 1, 'x' = 2, etc.

##### 		Pitch.chroma() -> int

​			Returns the [chroma value](https://en.wikipedia.org/wiki/Chroma_feature).

##### 		Pitch.key(diatonic: bool = False) -> int

​			diatonic: If true, accidentals are not taken into consideration

​			Returns key number on a piano.

##### 		Pitch.midi() -> int

​			Returns [midi note number](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies).

##### 					Pitch.frequency() -> float

​			Returns frequency in hertz of the pitch. Calculation uses A4 = 440hz in equal temperament.

##### 		Pitch.coord() -> [int, int]

​			Returns note coordinate.

##### 		Pitch.transpose(interval) -> Pitch

​			interval: Interval to transpose pitch, as either string (e.g. 'P4') or Interval

​			Returns transposed pitch.

#### Interval(name | coord | pitch1, pitch2)

​			name: Name of interval (e.g. P5 for perfect fifth)

​			coord: Coordinate array

​			pitches: Interval between two pitches, in either 

##### Interval.value() -> int

​			Returns an integer representing the interval (e.g. 5 for fifth),

##### Interval.base() -> int

​			Returns an integer representing the [simple interval](https://en.wikipedia.org/wiki/Interval_(music)#Simple_and_compound) (e.g. 5)

##### Interval.simple() -> str

​			Returns a string representing the interval (e.g. P5 for perfect fifth).

##### Interval.invert() -> Interval

​			Return the inversion of the simple interval. Operates inplace.

##### Interval.quality() -> str

​			Returns a string representing the interval quality (e.g. P for perfect).

##### Interval.semitones() -> int

​			Returns the interval distance in semitones (e.g. 4 for major second).

##### Interval.string() -> str

​			Returns a string representation of the interval (e.g. d10 for dim tenth).

## Contributing

​	If you are interesting in contributing, feel free to create a pull request.

​	Here's a list of future features I have, feel free to add your own as well.

- ##### Scale
  - [ ] Create tests
  - [ ] Add more arg options (from_pitches, from_intervals, from_name)
  - [ ] Type method which returns scale type
  - [ ] Name method which returns scale name (root + type)
  - [ ] Method to return scale at length (e.g. create two octave scales, scale up to fifth, etc.)
  
- ##### Chord
  - [ ] Add more arg options (from_pitches, from_name)
  - [ ] Add support for voicings

- ##### Pitch
  - [ ] Pitch.from_key(key): Set pitch from key on piano. Use most common names (optional sharp or flat key arg)
  
