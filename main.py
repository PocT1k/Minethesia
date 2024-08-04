# UTF-8 Будет здесь!

import mido
import time
import pygame.midi

from note import *


def play_midi(file_path):
    # pygame.init()
    pygame.midi.init()
    mid = mido.MidiFile(file_path)
    cTracks = len(mid.tracks)
    notes = []
    players = []
    metaMessages = ['track_name', 'time_signature', 'key_signature', 'set_tempo', 'midi_port', 'end_of_track']
    noteMessages = ['note_on', 'note_off', 'control_change', 'program_change', 'pitchwheel']
    print(file_path)
    print(f'Количество треков: {cTracks}')

    # Создание проигрывателей TODO - пока всего 1 на всех
    player1 = pygame.midi.Output(0)
    player1.set_instrument(0)
    for p in range (0, cTracks):
        players.append(player1)

    # Парсинг треков и добавление в массив
    for t, track in enumerate(mid.tracks):
        # track_name = track.name.encode('latin1').decode('utf-8')
        # print(f'Track {t}: {track_name}')
        Note.time = 0
        player = players[t]

        for msg in track:
            # print(f'\t{msg}')
            notes.append(Note(t, msg, player))
        pass # for msg
    pass # for track

    # Сортировка массива с нотами по времени
    notes.sort(key=lambda note: note.time)

    # Проигрывание файла
    timePast = 0
    lenNotes = len(notes)
    for i, n in enumerate(notes):
        # if (i < lenNotes - 100):
        #     timePast = n.time
        #     continue
        print(n.time)
        time.sleep((n.time - timePast) * 0.001 * 0.6)
        timePast = n.time
        n.proc()
    pass # for note
    print(f'END')
    time.sleep(0.3)

    # Отключение
    for p in range (0, cTracks):
        players[p].close()
    pygame.midi.quit()
    # pygame.quit()
pass # func play_midi()

# Открываем MIDI файл
folder = 'D:\\Backups and Saves\\midi\\'
# name = 'Газманов - Эскадрон'
name = 'Песняры - Вологда2'
# name = 'Травы, травы'
# name = 'Я буду долго гнать велосипед'
# name = 'Опять от меня сбежала последняя электричка'
# name = 'Прекрасное далёко (вариант)' #TODO - пауза в начале, ошибка с названием
# name = 'Пугачёва - Куда уходит детство'
path = folder + name + '.mid'
play_midi(path)
