class Note:
    time = 0

    def __init__(self, t, msg, player):
        Note.time += msg.time
        self.time = Note.time
        self.t = t
        self.msg = msg
        self.player = player
    pass # __init__()

    def proc(self):
        if self.msg.type == 'note_on':
            self.player.note_on(self.msg.note, self.msg.velocity)
        elif self.msg.type == 'note_off':
            self.player.note_off(self.msg.note, self.msg.velocity)
        else:
            pass #TODO
    pass # proc()
pass # class Note
