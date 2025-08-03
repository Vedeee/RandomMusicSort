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

## RMS
RMS - a simple program designed to sort your audio files in alphabetical or random order by format you input

## Supported formats
RMS is supports a small number of formats such as MP3, FLAC, OGG, WAV, WV, DSF. It is planned to set up support for more popular audio formats in the near future.


| Extension | Support | Discription                                                      |
| --------- | ------- | ---------------------------------------------------------------- |
| MP3       | 🟢      | Fully support                                                    |
| Flac      | 🟢      | Fully support                                                    |
| Ogg       | 🟢      | Fully support                                                    |
| Wav       | 🟡      | Fully supports sort in name, partially supports sort in metadata |
| Wv        | 🟡      | Fully supports sort in name, partially supports sort in metadata |
| Dsf       | 🟡      | Fully supports sort in name, partially supports sort in metadata |

Formats marked with 🟡 incompletely support sort in metadata. The data is written to a file, but Windows Explorer does not display it. However, this can be fixed by programs such as AIMP (tag editor)
## Random
RMS has a random audio file sorting feature. When this function is selected, the tracks will be numbered randomly each time the program is called.
## Variants of sort

### In name
This type of sorting involves changing the file name alphabetically (in standard mode) or randomly (by selecting the appropriate function)
### In metafata
This type of sorting involves changing the metadata of the file by changing the track number in alphabetical order (in standard mode) or in random order (by selecting the appropriate function)
## Clear
