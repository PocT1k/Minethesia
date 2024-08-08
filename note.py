class Note:
    time = 0.0
    bpm = 120.0
    '''set_tempo'''
    tempo = 500000
    '''time_signature'''
    numerator = 4
    denominator = 4
    clocks_per_click = 24
    notated_32nd_notes_per_beat = 8
    '''key_signature'''
    key = 'F'
    # metaMessages = ['track_name', 'time_signature', 'key_signature', 'set_tempo', 'midi_port', 'end_of_track']
    # noteMessages = ['note_on', 'note_off', 'control_change', 'program_change', 'pitchwheel']
    metaMessages = ['set_tempo']
    noteMessages = ['note_on', 'note_off']

    def __init__(self, t, msg, player):
        Note.time += msg.time * (1000.0 / Note.tempo / Note.denominator)
        self.time = Note.time
        self.t = t
        self.msg = msg
        self.player = player

        if msg.is_meta:
            if msg.type == 'set_tempo':
                Note.tempo = msg.tempo
                Note.bpm = 60 * (1000000.0 / Note.tempo)
            elif msg.type == 'time_signature':
                Note.numerator = msg.numerator
                Note.denominator = msg.denominator
                Note.clocks_per_click = msg.clocks_per_click
                Note.notated_32nd_notes_per_beat = msg.notated_32nd_notes_per_beat
            else:
                pass #TODO
        pass # if is_meta
    pass # __init__()

    def proc(self):
        print(f'{self.time} t:{self.t} {self.msg}')
        if self.msg.type == 'note_on':
            self.player.note_on(self.msg.note, self.msg.velocity)
        elif self.msg.type == 'note_off':
            self.player.note_off(self.msg.note, self.msg.velocity)
        else:
            pass #TODO
    pass # proc()
pass # class Note
