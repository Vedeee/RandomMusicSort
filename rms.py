import os
import random
import mutagen
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.wavpack import WavPack
from mutagen.wave import WAVE
from mutagen.dsf import DSF
from mutagen.id3 import TRCK
from mutagen.easyid3 import EasyID3
import glob

def Get_track_list(): # Выбор директории пользователя
    while True:
        folder_path = input("Введите путь к папке: ")
        if os.path.exists(folder_path):
            return folder_path
        else:
            print(f"Папки {folder_path} не существует. Попробуйте снова")

def Choice_music_format(folder_path): # Выбор формата(расширения) аудио файлов
    c = 0
    while True:
        format = input("Введите формат аудио файлов: ")
        for file in os.listdir(folder_path):
            if file.endswith('.'+format):
                c +=1
        if c >= 1:
            return format
        else:
            print("Отсутсвуют файлы с указанным расширением. Попробуйте снова")

def Choice_sort(): # Выбор формата сортировки
    print("1. В название")
    print("2. В метаданные")
    while True:
        sort_var = input("Выберите вариант сортировки: ")
        if sort_var.isdigit():
            sort_var = int(sort_var)
            if sort_var == 1 or sort_var == 2:
                return sort_var
            else:
                print("Некорректный ввод. Попробуйте еще раз.")
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

def Choice_Is_Random():
    print("1. Да")
    print("2. Нет")
    while True:
        is_random = input("Рандомизировать сортировку? ")
        if is_random.isdigit():
            is_random = int(is_random)
            if is_random == 1:
                return True
            elif is_random == 2:
                return False
            else:
                print("Некорректный ввод. Попробуйте еще раз.")
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

def Sort_by_name(folder_path, format, random_var): # Cортировка по изменению имени файла
    iteration = 1
    a = []
    for i in os.scandir(folder_path):
        if i.name.find(f'.{format.lower()}')+1:
            a.append(i)
        else:
            continue
    if random_var == True:
        random.shuffle(a)
    for j in a:
        old_name = j.path
        if iteration <= 9:
            new_name = os.path.join(folder_path, '0' + str(iteration) + '. ' + j.name)
        else:
            new_name = os.path.join(folder_path, str(iteration) + '. ' + j.name)
        os.rename(old_name, new_name)
        print(old_name)
        print(new_name)
        iteration += 1

def Sort_in_metadata(folder_path, format, random_var): # Сортировка по изменению метаданных (номер трека)
    filez = glob.glob(folder_path + "/*." + format)
    if random_var == True:
        random.shuffle(filez)
    for i in range(len(filez)):
        tracknum = i+1
        song = filez[i]
        match format:
            case "mp3":
                file = MP3(song, ID3 = EasyID3)
                file['tracknumber'] = str(tracknum)
            case "flac":
                file = FLAC(song)
                file['tracknumber'] = str(tracknum)
            case "wv":
                file = WavPack(song)
                file['Track'] = str(tracknum)
            case "ogg":
                file = mutagen.File(song)
                file['tracknumber'] = str(tracknum)
            case 'wav':
                file = WAVE(song)
                file.tags.setall('TRCK', [TRCK(encoding=3, text=str(tracknum))])
            case 'dsf':
                file = DSF(song)
                file.tags.setall('TRCK', [TRCK(encoding=3, text=str(tracknum))])
        file.save()

def Clear_previous_sort(folder_path, sort_var, format): # Отчистка от предыдущих сортировок
    print("1. Да")
    print("2. Нет")
    while True:
        is_clear = input("Хотите очистить? ")
        if is_clear.isdigit():
            is_clear = int(is_clear)
            if is_clear == 1:
                a = []
                match sort_var:
                    case 1:
                        for i in os.scandir(folder_path):
                            if i.name.find(f'.{format.lower()}') + 1:
                                a.append(i)
                            else:
                                continue
                        for j in a:
                            old_name = j.path
                            index = j.name.index(' ', 0, )
                            new_name = os.path.join(folder_path, j.name[index + 1:])
                            os.rename(old_name, new_name)
                        break
                    case 2:
                        filez = glob.glob(folder_path + "/*."+format)
                        for i in range(len(filez)):
                            tracknum = ''
                            song = filez[i]
                            match format:
                                case "mp3":
                                    file = MP3(song, ID3=EasyID3)
                                    file['tracknumber'] = str(tracknum)
                                case "flac":
                                    file = FLAC(song)
                                    file['tracknumber'] = str(tracknum)
                                case "wv":
                                    file = WavPack(song)
                                    file['Track'] = str(tracknum)
                                case "ogg":
                                    file = mutagen.File(song)
                                    file['tracknumber'] = str(tracknum)
                                case 'wav':
                                    file = WAVE(song)
                                    file.tags.setall('TRCK', [TRCK(encoding=3, text=str(tracknum))])
                                case 'dsf':
                                    file = DSF(song)
                                    file.tags.setall('TRCK', [TRCK(encoding=3, text=str(tracknum))])
                            file.save()
                        break
            elif is_clear == 2:
                print("Ну ок")
            else:
                print("Некорректный ввод. Попробуйте еще раз.")
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__": # Main
    folder_path = Get_track_list()
    format = Choice_music_format(folder_path)
    sort_var = Choice_sort() #
    random_var = Choice_Is_Random() #
    match sort_var:
        case 1:
            Sort_by_name(folder_path, format, random_var) #
        case 2:
            Sort_in_metadata(folder_path, format, random_var) #
    Clear_previous_sort(folder_path, sort_var, format) #
