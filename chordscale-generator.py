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
import json

parser = argparse.ArgumentParser(
        prog = 'chordscale-generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description = '''
Chords and Scales Generator.
This tool helps musicians to create random sequence of chords and scales to practice them on the instrument.
        '''
        )
mode_arg = parser.add_argument('-m', '--mode', help='Generation mode. Valid options: "chord", "scale"')
length_arg = parser.add_argument('-l', '--length', type=int, default=16, help='Length of sequence. Valid options: positive INT')
out_arg = parser.add_argument('-o', '--output', default="text", help='Output type. Valid options: "text", "json"')
complexity_arg = parser.add_argument('-c', '--complexity', type=int, default=1, help='Sequence complexity. Valid range: 1-3')
args = parser.parse_args()

# Check arguments
if args.mode != 'chord' and args.mode != 'scale':
    raise argparse.ArgumentError(mode_arg, 'Mode cannot be empty or different from "scale" or "chord"')

if args.length <= 0:
    raise argparse.ArgumentError(length_arg, 'Length must be a positive integer')

if args.output != 'text' and args.output != 'json':
    raise argparse.ArgumentError(mode_arg, 'Output cannot be empty or different from "text" or "json"')

if args.complexity < 1 or args.complexity > 3:
    raise argparse.ArgumentError(length_arg, 'Complexity must be a positive integer in the range 1-3')

# Constants
__LINE_SEPARATOR = '-' * 72
TONES = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]

# Chords are organized in 3 lists with growing complexity
CHORD_TYPES_1 = [ "Major", 
           "Minor", 
           "Diminished", 
           "Augmented", 
           "Maj7", 
           "Min7", 
           "7", 
           "Min7b5"]

CHORD_TYPES_2 = [
           "Min/Maj7", 
           "7sus4", 
           "Maj7#5", 
           "13", 
           "Maj6", 
           "Min6", 
           "7#11"]

CHORD_TYPES_3 = [
           "7sus4b2", 
           "Dim7", 
           "7alt", 
           "7b9", 
           "7b9#9", 
           "7b13", 
           "7b5", 
           "7#5",
           "7b9b13"]


# Scales list can grow over time
SCALE_TYPES_1 = [ "Major", 
           "Natural Minor", 
           "Melodic Minor", 
           "Harmonic Minor", 
           "Harmonic Major", 
           "Whole Tone"
           ]

SCALE_TYPES_2 = [
           "Dorian",
           "Frigian",
           "Lydian",
           "Mixolydian",
           "Aelian",
           "Locrian",
           "Dorian b2",
           "Lydian #5",
           "Lydian b7",
           "Mixolydian b13",
           "Locrian ♮9", 
           "SuperLocrian",
           "Half-Whole Dimished",
           "Whole-Half Dimished"
        ]

SCALE_TYPES_3 = [
           "Locrian ♮9 ♮6",
           "Frigian b11",
           "Lydian minor",
           "Mixolydian b9",
           "Lydian #5 #9",
           "Locrian bb7"
        ]

# tone_set generates the final random tone set
def tone_set(n):
    tone_list = []
    for t in range(0, n):
        tone_list.append(random.choice(TONES))
    return tone_list

# chord_set generates the final random chord set
def chord_set(n, cmpx):
    chord_list = []
    chord_types = []
    if cmpx == 1:
        chord_types.extend(CHORD_TYPES_1)
    elif cmpx == 2:
        chord_types.extend(CHORD_TYPES_1)
        chord_types.extend(CHORD_TYPES_2)
    else:
        chord_types.extend(CHORD_TYPES_1)
        chord_types.extend(CHORD_TYPES_2)
        chord_types.extend(CHORD_TYPES_3)
    for c in range(0, int(args.length)):
        chord_list.append(random.choice(chord_types))
    return chord_list

# scale_set generates the final random scale set
def scale_set(n, cmpx):
    scale_list = []
    scale_types = []
    if cmpx == 1:
        scale_types.extend(SCALE_TYPES_1)
    elif cmpx == 2:
        scale_types.extend(SCALE_TYPES_1)
        scale_types.extend(SCALE_TYPES_2)
    else:
        scale_types.extend(SCALE_TYPES_1)
        scale_types.extend(SCALE_TYPES_2)
        scale_types.extend(SCALE_TYPES_3)
    for s in range(0, n):
        scale_list.append(random.choice(scale_types))
    return scale_list

# chords_json returns a jsonString based on the dictionary generated by the chords + tones 
def chords_json(ch, tn):
    tones_chords_dict = {i: [tn[i], ch[i]] for i in range(len(tn))}
    jsonString = json.dumps(tones_chords_dict)
    return jsonString

# scales_json returns a jsonString based on the dictionary generated by the scales + tones 
def scales_json(sc, tn):
    tones_scales_dict = {i: [tn[i], sc[i]] for i in range(len(tn))}
    jsonString = json.dumps(tones_scales_dict)
    return jsonString

# chords_text prints the generated chords set
def chords_text(ch, tn):
    print("\033[1m" + "Printing chord chart..." + "\033[0m")
    print(__LINE_SEPARATOR)
    for i in range(0, args.length):
         print(tn[i], ch[i])
    print(__LINE_SEPARATOR)

# scales_text prints the generated scales set
def scales_text(sc, tn):
    print("\033[1m" + "Printing scale chart..." + "\033[0m")
    print(__LINE_SEPARATOR)
    for i in range(0, args.length):
         print(tn[i], sc[i])
    print(__LINE_SEPARATOR)

# Main function
def main():
    # Print chord sequence in plain text
    if args.mode == 'chord':
        chords_list = chord_set(args.length, args.complexity)
        tones_list = tone_set(args.length)
        if args.output == 'text':
            chords_text(chords_list, tones_list)
        else:
            json_out = chords_json(chords_list, tones_list)
            print(json_out)

    # Print scale sequence in plain text
    if args.mode == 'scale':
        scales_list = scale_set(args.length, args.complexity)
        tones_list = tone_set(args.length)
        if args.output == 'text':
            chords_text(scales_list, tones_list)
        else:
            json_out = chords_json(scales_list, tones_list)
            print(json_out)

if __name__ == "__main__":
    main()
