#UTF-8 Будет здесь!
#How Synthesia, but Minethesia

import mido
import pygame
import pygame.midi
import time


def play_midi(file_path): #Воспроизведение MIDI файла
    # Инициализация Pygame и MIDI
    pygame.init()
    pygame.midi.init()
    # Открываем MIDI выход
    player = pygame.midi.Output(0)  # Выберите нужный MIDI-выход (0 - первый)
    player.set_instrument(0)
    # Загружаем MIDI файл
    mid = mido.MidiFile(file_path)

    metaMessages = ['time_signature', 'key_signature', 'set_tempo', 'midi_port', 'end_of_track']
    notMetaMessages = ['control_change', 'program_change']

    # Проходим по всем сообщениям в треках
    for t, track in enumerate(mid.tracks, start=1):
        print(f'Track{t}: {track.name}')
        for msg in track:
            time.sleep(msg.time * 0.001 * 1.2)  # Ждем время, указанное в сообщении

            if msg.type == 'note_on':
                player.note_on(msg.note, msg.velocity)
            elif msg.type == 'note_off':
                player.note_off(msg.note, msg.velocity)
            else:
                if (msg.type not in (metaMessages + notMetaMessages)):
                    print(f'\t{msg}')

    # Закрываем MIDI выход
    player.close()
    pygame.midi.quit()
    pygame.quit()

# Открываем MIDI файл
folder = 'D:\\Backups and Saves\\midi\\'
name = 'Беловежская пуща (труба).mid'
path = folder + name
play_midi(path)
