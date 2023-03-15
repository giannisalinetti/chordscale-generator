#!/usr/bin/python3

#    Chords and scales random generator.
#    Giovan Battista Salinetti 2015/03/02
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
import textwrap
import argparse

parser = argparse.ArgumentParser(
        prog = 'chordscale-generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description = '''
Chords and Scales Generator.
This tool helps musicians to create random sequence of chords and scales to practice them on the instrument.
        '''
        )
mode_arg = parser.add_argument('-m', '--mode', help='Generation mode. Valid options: "chord", "scale"')
length_arg = parser.add_argument('-l', '--length', type=int, help='Length of sequence. Valid options: positive INT')
args = parser.parse_args()

# Constants
LINE_SEPARATOR = '-' * 72
TONES = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]

# Chords list can grow over time
CHORD_TYPES = [ "Major", 
           "Minor", 
           "Diminished", 
           "Augmented", 
           "Maj7", 
           "Min7", 
           "Min/Maj7", 
           "7", 
           "7sus4", 
           "Min7b5", 
           "Dim7", 
           "7alt", 
           "7b9", 
           "7b9#9", 
           "Maj7#5", 
           "7#11", 
           "7b5", 
           "7sus4b2", 
           "7b13", 
           "7b9b13", 
           "13", 
           "Maj6", 
           "Min6", 
           "7#5" ]

# Scales list can grow over time
SCALE_TYPES = [ "Major", 
           "Natural Minor", 
           "Melodic Minor", 
           "Harmonic Minor", 
           "Harmonic Major", 
           "Whole Tone", 
           "Half-Whole Dimished",
           "Whole-Half Dimished",
           "Dorian",
           "Frigian",
           "Lydian",
           "Mixolydian",
           "Aelian",
           "Locrian",
           "SuperLocrian"]

def tone_set(n):
    tone_list = []
    for t in range(0, n):
        tone_list.append(random.choice(TONES))
    return tone_list

def chord_set(n):
    chord_list = []
    for c in range(0, int(args.length)):
        chord_list.append(random.choice(CHORD_TYPES))
    return chord_list

def scale_set(n):
    scale_list = []
    for s in range(0, n):
        scale_list.append(random.choice(SCALE_TYPES))
    return scale_list

def chord_text_printer():
    print("\033[1m" + "Printing chord chart..." + "\033[0m")
    print(LINE_SEPARATOR)
    chord_out = chord_set(int(args.length))
    tone_out = tone_set(int(args.length))
    for i in range(0, int(args.length)):
         print(tone_out[i], chord_out[i])
    print(LINE_SEPARATOR)

def scale_text_printer():
    print("\033[1m" + "Printing scale chart..." + "\033[0m")
    print(LINE_SEPARATOR)
    scale_out = scale_set(int(args.length))
    tone_out = tone_set(int(args.length))
    for i in range(0, int(args.length)):
         print(tone_out[i], scale_out[i])
    print(LINE_SEPARATOR)

# Check arguments
if args.mode != 'chord' and args.mode != 'scale':
    raise argparse.ArgumentError(mode_arg, 'Mode cannot be different from "scale" or "chord"')

if args.length <= 0:
    raise argparse.ArgumentError(length_arg, 'Length must be a positive integer')

# Print chord sequence in plain text
if args.mode == 'chord':
    chord_text_printer()

# Print scale sequence in plain text
if args.mode == 'scale':
    scale_text_printer()
