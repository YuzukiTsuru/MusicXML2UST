from MusicXMLPaser.MusicXMLPaser import MusicXMLDocument, Tempo
import json


def main():
    score_parser = MusicXMLDocument('test/01.xml')
    for tempo in score_parser.get_tempos():
        tempos = tempo.qpm
        print(tempos)

    for part in score_parser.parts:
        for measure in part.measures:
            for note in measure.notes:
                print(note.get_note())


if __name__ == '__main__':
    main()
