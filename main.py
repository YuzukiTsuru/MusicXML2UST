import re

import xmltodict

from StaticAssets import *


def handle_ust(lenth, lyc, noten, _id):
    if _id < 10:
        note_id = '[#000' + str(_id) + ']'
    elif 100 > _id > 9:
        note_id = '[#00' + str(_id) + ']'
    elif 1000 > _id > 99:
        note_id = '[#0' + str(_id) + ']'
    elif 10000 > _id > 999:
        note_id = '[#' + str(_id) + ']'
    else:
        raise Exception('不会吧不会吧不会真的有人一个ust弄出10000个音符吧')

    return "\n" + note_id + "\nLength=" + str(lenth) + "\nLyric=" + str(lyc) + "\nNoteNum=" + str(
        noten) + "\nIntensity=100" \
                 "\nModulation=0 "


def handle_pitch(pit):
    pitches = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    accs = {'': 0, '#': 1, 'b': -1}
    pattern = r'([CDEFGAB]{1})([#b]?)(-?\d{1})'
    _note, _accidental, _octave = re.match(pattern, pit).group(1, 2, 3)
    result = (int(_octave) + 1) * 12 + pitches[_note] + accs[_accidental]
    return result


if __name__ == '__main__':
    score = xmltodict.parse(open('test/Simple.xml').read())['score-partwise']['part']['measure']
    tempo = 120

    ust = VERSION + SETTING

    _id = 0

    for i in score:
        # width -> Length
        if '@width' in i:
            length = i['@width']
        else:
            length = 1

        # tempo -> Tempo
        if 'direction' in i:
            if 'sound' in i['direction']:
                tempo = i['direction']['sound']['@tempo']

        ust = ust + "\nTempo=" + str(tempo)

        # Get sub notes
        for note in i['note']:

            # pitch -> NoteNum
            if 'pitch' in note:
                pitch_name = note['pitch']['step'] + note['pitch']['octave']
                pitch = handle_pitch(pitch_name)
            else:
                pitch = 24

            # lyric -> Lyric
            if 'lyric' in note:
                text = note['lyric']['text']['#text']
            else:
                text = 'R'

            ust = ust + handle_ust(length, text, pitch, _id)

            _id = _id + 1
    ust = ust + TRACKEND
    print(ust)

    file = open('test/Simple.ust', mode='w')
    file.write(ust)
