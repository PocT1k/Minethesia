# UTF-8 Будет здесь!

import mido
import time
import pygame.midi

from note import *
from func import *


def play_midi(file_path):
    pygame.midi.init()
    mid = mido.MidiFile(file_path)
    cTracks = len(mid.tracks)
    notes = []
    players = []
    print(mid.filename)
    print(f'Тип: {mid.type}')
    print(f'Длинна в тактах: {mid.length}')
    print(f'Количество треков: {cTracks}')

    # Создание проигрывателей TODO - пока всего 1 на всех
    player1 = pygame.midi.Output(0)
    player1.set_instrument(0)
    for p in range (0, cTracks):
        players.append(player1)

    # Парсинг треков и добавление в массив
    for t, track in enumerate(mid.tracks):
        track_name = decodStr(track.name)
        print(f'Track {t}: {"Track " + str(t+1) + " (no name)" if track_name == "" else track_name}')
        Note.time = 0
        player = players[t]

        for msg in track:
            notes.append(Note(t, msg, player))
        pass # for msg
    pass # for track

    # Сортировка массива с нотами по времени
    notes.sort(key=lambda note: note.time)
    lenNotes = len(notes)

    # Проигрывание файла
    timePast = 0.0
    timeStart = 0.0
    for i, n in enumerate(notes):
        # if (i < lenNotes - 500): # Переход к концу
        #     timePast = n.time
        #     continue
        if n.time < timeStart: # Начало с точки
            timePast = n.time
            continue

        timeNow = n.time
        print(f'{timeNow} t:{n.t} {n.msg}')
        if timeNow: time.sleep(timeNow - timePast)
        timePast = timeNow
        # exit(0)
        n.proc()
    pass # for note
    print(f'END')
    time.sleep(0.3)

    # Отключение
    for p in range (0, cTracks):
        players[p].close()
    pygame.midi.quit()
pass # funck play_midi()

# Открываем MIDI файл
folder = 'F:\\Backups and Saves\\midi\\'
# name = 'Газманов - Эскадрон'
# name = 'Песняры - Вологда1'
# name = 'Песняры - Вологда2'
# name = 'Травы, травы'
# name = 'Я буду долго гнать велосипед'
# name = 'На дальней станции сойду'
# name = 'Опять от меня сбежала последняя электричка'
# name = 'Прекрасное далёко (вариант)' #TODO - пауза в начале
# name = 'Пугачёва - Куда уходит детство'
# name = 'Чёрный ворон конв'
# name = 'Сергей Беликов - Снится мне деревня'
# name = 'Как молод мы были'
name = 'Ласковый Май - Седая ночь'
path = folder + name + '.mid'
play_midi(path)
