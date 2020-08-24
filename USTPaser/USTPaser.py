class USTPaser(object):

    def __init__(self, musicXML, tempo):
        self.ust_data = self.paser_xml(musicXML, tempo)
        self.tempo = tempo
        self.VERSION = "[#VERSION]\nUST Version1.2"

        self.SETTING = "\n[#SETTING]" \
                       "\nTracks=1" \
                       "\nProjectName=" \
                       "\nVoiceDir=%VOICE%" \
                       "\nOutFile=" \
                       "\nCacheDir=New Project.cache" \
                       "\nTool1=wavtool.exe" \
                       "\nTool2=resampler.exe" \
                       "\nMode2=True"

        self.TRACKEND = "\n[#TRACKEND]"

    def paser_xml(self, musicxml, tempo):
        ust_note = ''
        _id = 0

        for note in musicxml:
            note_id = self.handle_id(_id)
            length = int(int(note[0]) * tempo)
            if note[1] is True:
                pitch = 24
            else:
                pitch = note[1]
            lyric = note[2]
            ust_note += "\n" + note_id + "\nLength=" \
                        + str(length) + "\nLyric=" + str(lyric) \
                        + "\nNoteNum=" + str(pitch) + "\nIntensity=100\nModulation=0"
            _id = _id + 1
        return ust_note

    @staticmethod
    def handle_id(_id):
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
        return note_id

    def get_ust(self):
        return self.VERSION + self.SETTING + "\nTempo=" + str(self.tempo) + self.ust_data + self.TRACKEND
