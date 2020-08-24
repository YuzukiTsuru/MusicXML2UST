from MusicXMLPaser.MusicXMLPaser import MusicXMLDocument
from USTPaser.USTPaser import USTPaser


def main():
    tempos = 120
    score_parser = MusicXMLDocument('test/01.xml')
    for tempo in score_parser.get_tempos():
        tempos = tempo.qpm
        print(tempos)

    xml_data = []
    i = 0
    for part in score_parser.parts:
        for measure in part.measures:
            for note in measure.notes:
                xml_data.insert(i, note.get_note())
                i += i

    print(USTPaser(xml_data, tempos).get_ust())


if __name__ == '__main__':
    main()
