#!/usr/bin/python3

#    Chords and scales random generator. Version 0.1.
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

#    This program takes two arguments as input from the user: chord or scale progression and the number of elements
#    The 'chords' and the 'scales' lists can be expanded with new material without altering the rest of the code

#    TODO:
#    Export to file facilities (html, csv, xml, improve plain text)

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

def tone_set(n):
    tone_list = []
    tones = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
    for t in range(0, n):
        tone_list.append(random.choice(tones))
    return tone_list

def chord_set(n):
    chord_list = []
    chords = [ "Major", 
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
    for c in range(0, int(args.length)):
        chord_list.append(random.choice(chords))
    return chord_list

def scale_set(n):
    scale_list = []
    scales = [ "Major", 
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
    for s in range(0, n):
        scale_list.append(random.choice(scales))
    return scale_list

def print_separator():
    width = 72
    print('-' * width)

# Check arguments
if args.mode != 'chord' and args.mode != 'scale':
    raise argparse.ArgumentError(mode_arg, 'Mode cannot be different from "scale" or "chord"')

if args.length <= 0:
    raise argparse.ArgumentError(length_arg, 'Length must be a positive integer')

# Print chord sequence in plain text
if args.mode == 'chord':
    print("\033[1m" + "Printing chord chart..." + "\033[0m")
    print_separator()
    chord_out = chord_set(int(args.length))
    tone_out = tone_set(int(args.length))
    for i in range(0, int(args.length)):
         print(tone_out[i], chord_out[i])
    print_separator()

# Print scale sequence in plain text
if args.mode == 'scale':
    print("\033[1m" + "Printing scale chart..." + "\033[0m")
    print_separator()
    scale_out = scale_set(int(args.length))
    tone_out = tone_set(int(args.length))
    for i in range(0, int(args.length)):
         print(tone_out[i], scale_out[i])
    print_separator()

