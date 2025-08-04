# Localization
en / [ru](README.ru.md)

# Table of Contents
- [RMS](#rms)
- [Supported formats](#supported-formats)
- [Random](#random)
- [Variants of sort](#variants-of-sort)
	- [In name](#in-name)
	- [In metafata](#in-metadata)
- [Clear](#clear)
- [Using](#using)

## RMS
RMS - a simple program designed to sort your audio files in alphabetical or random order by format you input

## Supported formats
RMS supports a small number of formats such as MP3, FLAC, OGG, WAV, WV, DSF. It is planned to add support for more audio formats in the near future.

| Extension | Support | Discription                                                      |
| --------- | ------- | ---------------------------------------------------------------- |
| MP3       | 🟢      | Fully support                                                    |
| Flac      | 🟢      | Fully support                                                    |
| Ogg       | 🟢      | Fully support                                                    |
| Wav       | 🟡      | Fully supports sort in name, partially supports sort in metadata |
| Wv        | 🟡      | Fully supports sort in name, partially supports sort in metadata |
| Dsf       | 🟡      | Fully supports sort in name, partially supports sort in metadata |

Formats marked with 🟡 do not fully support sorting in metadata. The data is written to a file, but Windows Explorer does not display it. However, this can be fixed using third-party programs such as AIMP (built-in tag editor).
## Random
RMS has a random audio file sorting feature. When this function is selected, the tracks will be numbered randomly each time the program is called.
## Variants of sort

### In name
This type of sorting involves changing the file name alphabetically (in standard mode) or randomly (by selecting the appropriate function)
### In metafata
This type of sorting involves changing the metadata of the file by changing the track number in alphabetical order (in standard mode) or in random order (by selecting the appropriate function)
## Clear
After sorting, you can clear the changed fields of the file (name and/or metadata)

## Using
Now RMS supports only russian language, it is planned to add English language support in the near future.

1. First you need is execute rms.py from terminal:
   ``` python
   python rms.py
   ```
2. Then you have to enter path to the folder with your audio files:
   ```python
   Введите путь к папке: Path\to\your\folder
```
3. Further, you have to enter format (extension) of audio files:
   ```python
   Введите формат аудио файлов: mp3
```
4. Futher, you have to choice the variant of sort (1 - in name, 2 - in metadata):
   ```python
   1. В название
   2. В метаданные
	Выберите вариант сортировки: 1
```
5. Futher, you can turn on/off random sort (1 - yes, 2 - no):
   ```python
   1. Да
   2. Нет
	Рандомизировать сортировку? 2
```
6. And finally, you can choice clear your sort (1 - yes, 2 - no):
   ```python
   1. Да
   2. Нет
	Хотите очистить? 1
```
1. First you need is execute rms.py from terminal
``` python
python rms.py
```
