import re

import xmltodict
import json


def handle_pitch(pit):
    pitches = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    accs = {'': 0, '#': 1, 'b': -1}
    pattern = r'([CDEFGAB]{1})([#b]?)(-?\d{1})'
    _note, _accidental, _octave = re.match(pattern, pit).group(1, 2, 3)
    result = (int(_octave) + 1) * 12 + pitches[_note] + accs[_accidental]
    return result


if __name__ == '__main__':
    score = xmltodict.parse(open('test/Simple.xml').read())
    score = score['score-partwise']['part']['measure']
    for i in score:
        if '@width' in i:
            length = i['@width']
        else:
            length = 1
        for note in i['note']:

            if 'pitch' in note:
                pitch_name = note['pitch']['step'] + note['pitch']['octave']
                pitch = handle_pitch(pitch_name)
            else:
                pitch = 24

            if 'lyric' in note:
                text = note['lyric']['text']['#text']
            else:
                text = 'R'

            print(str(pitch) + text + length)
