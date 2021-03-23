# Kokoro Speech Dataset

Kokoro Speech Dataset is a public domain Japanese speech dataset.
It contains around 34,958 short audio clips of a single speaker reading 9 novel books.
The format of the metadata is very similar to
[LJ Speech](https://keithito.com/LJ-Speech-Dataset/) so that the dataset is compatible
with modern speech synthesis systems.

The texts are from 
[Aozora Bunko](https://www.aozora.gr.jp/),
which are the public domain. The audio clips
are from
[LibriVox project](https://librivox.org/),
which are also in the public domain.
Readings are estimated by 
[MeCab](https://taku910.github.io/mecab/)
and
[UniDic Lite](https://pypi.org/project/unidic-lite/)
from Kanji-Kana mixture writing system.
Readings are in Romanized-like writing system
which is similar to the writing system used by
[Julius](https://github.com/julius-speech/julius).

The audio clips were split and transcripts were aligned automatically by
[Voice100](https://github.com/kaiidams/voice100).
100 samples were verified by a native speaker
[Katsuya Iida](katsuya.iida@gmail.com).

## Sample data

- Download
[Randomly sampled 100 clips](https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/0.1/kokoro-sample-20210321.zip).

## File Format

Metadata is provided in transcripts.txt. This file consists of one record per line,
delimited by the pipe character (0x7c). The fields are:

- ID: this is the name of the corresponding .wav file
- Transcription: Kanji-kana mixture text spoken by the reader (UTF-8)
- Reading: Romanized text spoken by the reader (UTF-8)

Each audio file is a single-channel 16-bit PCM WAV with a sample rate of 22050 Hz.

## Statistics

```
Large:
Total clips: 34958
Min duration: 3.007 secs
Max duration: 14.745 secs
Mean duration: 4.978 secs
Total duration: 48:20:24

Small:
Total clips: 8812
Min duration: 3.007 secs
Max duration: 14.431 secs
Mean duration: 4.951 secs
Total duration: 12:07:12

Tiny:
Total clips: 285
Min duration: 3.019 secs
Max duration: 9.462 secs
Mean duration: 4.871 secs
Total duration: 00:23:08
```

## How to get the data

Because of its large data size of the dataset, audio files are not
included in this repository, but the transcripts and audio split
points are included.

To get all WAV files of the dataset, run 

```
$ download.sh
```

to download the audio files from archive.org and extract them. Run

```
$ pip install torchaudio
$ python extract.py --split tiny
```

to get all files for tiny set under `./output` directory. RUn

```
$ pip install torchaudio
$ python extract.py --split full
```

to get all files for full set under `./output` directory.

## Books

The dataset contains recordings from these books read by
[ekzemplaro](https://librivox.org/reader/7044)

- [明暗 (Meian)](https://librivox.org/meian-by-soseki-natsume/) 16:39:29 
    [Online text](http://www.aozora.gr.jp/cards/000148/files/782_14969.html)
- [こころ (Kokoro)](https://librivox.org/kokoro-by-soseki-natsume/) 08:46:41
    [Online text](http://www.aozora.gr.jp/cards/000148/files/773_14560.html)
- [田舎教師 (Inaka Kyoshi)](https://librivox.org/inakakyoshi-by-katai-tayama/) 08:13:26
    [Online text](http://www.aozora.gr.jp/cards/000214/files/1668_26031.html)
- [野分 (Nowaki)](https://librivox.org/nowaki-by-soseki-natsume/) 4:40:49
    [Online text](http://www.aozora.gr.jp/cards/000148/files/791_14959.html)
- [草枕 (Kusamakura)](https://librivox.org/kusamakura-by-soseki-natsume/) 04:27:35
    [Online text](http://www.aozora.gr.jp/cards/000148/files/776_14941.html)
- [坊っちゃん (Botchan)](https://librivox.org/botchan-by-soseki-natsume-2/) 04:26:27
    [Online text](http://www.aozora.gr.jp/cards/000148/files/752_14964.html)
- [雁 (Gan)](https://librivox.org/gan-by-ogai-mori/) 03:41:31
    [Online text](http://www.aozora.gr.jp/cards/000129/files/45224_19919.html)
- [ごん狐 (Gon gitsune)](https://librivox.org/gongitsune-by-nankichi-niimi/) 0:15:42
    [Online text](http://www.aozora.gr.jp/cards/000121/files/628_14895.html)
- [コーカサスの禿鷹 (Caucasus no Hagetaka)](https://librivox.org/caucasus-no-hagetaka-by-yoshio-toyoshima/) 0:13:04
    [Online text](http://www.aozora.gr.jp/cards/000906/files/42633_22951.html)

## Changelog

- v0.2 Current release

## License

This dataset is in the public domain in the USA (and most likely other countries as well).
There are no restrictions on its use. For more information, please see: librivox.org/pages/public-domain.