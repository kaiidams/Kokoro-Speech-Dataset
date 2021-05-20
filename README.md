# Kokoro Speech Dataset

Kokoro Speech Dataset is a public domain Japanese speech dataset.
It contains 43,253 short audio clips of a single speaker reading 14 novel books.
The format of the metadata is similar to that of
[LJ Speech](https://keithito.com/LJ-Speech-Dataset/) so that the dataset is compatible
with modern speech synthesis systems.

The texts are from
[Aozora Bunko](https://www.aozora.gr.jp/),
which is in the public domain. The audio clips
are from
[LibriVox project](https://librivox.org/),
which is also in the public domain.
Readings are estimated by 
[MeCab](https://taku910.github.io/mecab/)
and
[UniDic Lite](https://pypi.org/project/unidic-lite/)
from kanji-kana mixture text.
Readings are romanized
which are similar to the format used by
[Julius](https://github.com/julius-speech/julius).

The audio clips were split and transcripts were aligned automatically by
[Voice100](https://github.com/kaiidams/voice100).

## Sample data

[Listen](https://kaiidams.github.io/Kokoro-Speech-Dataset/samples.html)
from your browser or download
[randomly sampled 100 clips](https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/1.0/kokoro-speech-v1_0-sample.zip).

## File Format

Metadata is provided in `metadata.csv`. This file consists of one record per line,
delimited by the pipe character (0x7c). The fields are:

- ID: this is the name of the corresponding .wav file
- Transcription: Kanji-kana mixture text spoken by the reader (UTF-8)
- Reading: Romanized text spoken by the reader (UTF-8)

Each audio file is a single-channel 16-bit PCM WAV with a sample rate of 22050 Hz.

## Statistics

The dataset is provided in different sizes, `xlarge`, `large`, `small`, `tiny`.
`large`, `small` and `tiny` don't share same clips.
`xlarge` contains all available clips, including `large`, `small` and `tiny`.

```
X Large:
Total clips: 43253
Min duration: 3.007 secs
Max duration: 14.988 secs
Mean duration: 4.993 secs
Total duration: 59:59:40

Large:
Total clips: 22910
Min duration: 3.007 secs
Max duration: 14.988 secs
Mean duration: 4.984 secs
Total duration: 31:42:54

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
included in this repository, but the metadata is included.

To make .wav files of the dataset, run 

```
$ bash download.sh
```

to download the metadata from the project page. Then run

```
$ pip3 install torchaudio
$ python3 extract.py --size tiny
```

This prints a shell script example to download MP3 audio files
from archive.org and extract them if you haven't done it already.

After doing so, run the command again

```
$ python3 extract.py --size tiny
```

to get files for `tiny` under `./output` directory.

You can give another size name to the `--size` option to get
dataset of the size.

## Pretrained Tacotron model

- [Audio Samples](https://kaiidams.github.io/Kokoro-Speech-Dataset/tacotron.html)
- [Pretrained model](https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/1.0/tacotron-kokoro-20210324.zip)

Pretrained [Tacotron](https://github.com/keithito/tacotron)
model trained with Kokoro Speech Dataset
and audio samples are available.
The model was trained for 21K steps with `small`.
According to the above repo,
"Speech started to become intelligible around 20K steps" with
LJ Speech Dataset.
Audio samples read the first few sentences from Gon Gitsune
which is not included in `small`.

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
- [生まれいずる悩み (Umareizuru Nayami)](https://librivox.org/umareizuru-nayami-by-takeo-arishima/) 2:43:12
    [Online text](http://www.aozora.gr.jp/cards/000025/files/1111_20600.html)
- [硝子戸の中 (Garasudono uchi)](https://librivox.org/garasudono-uchi-by-natsume-soseki/) 2:39:53
    [Online text](http://www.aozora.gr.jp/cards/000148/files/760_14940.html)
- [永日小品 (Eijitsu Syohin)](https://librivox.org/eijitsu-syohin-by-soseki-natsume/) 2:33:54
    [Online text](http://www.aozora.gr.jp/cards/000148/files/758_14936.html)
- [蒲団 (Futon)](https://librivox.org/futon-by-katai-tayama/) 2:28:58
    [Online text](http://www.aozora.gr.jp/cards/000214/files/1669_8259.html)
- [高野聖 (Kouyahijiri)](https://librivox.org/kouyahijiri-by-kyoka-izumi/) 2:06:23
    [Online text](http://www.aozora.gr.jp/cards/000050/files/521_20583.html)
- [ごん狐 (Gon gitsune)](https://librivox.org/gongitsune-by-nankichi-niimi/) 0:15:42
    [Online text](http://www.aozora.gr.jp/cards/000121/files/628_14895.html)
- [コーカサスの禿鷹 (Caucasus no Hagetaka)](https://librivox.org/caucasus-no-hagetaka-by-yoshio-toyoshima/) 0:13:04
    [Online text](http://www.aozora.gr.jp/cards/000906/files/42633_22951.html)

## Similar project

This project was also inspired by [CSS10](https://github.com/Kyubyong/css10), which
contains audio clips of various languages from LibriVox.

## Changelog

- v1.1 Added more books
- v1.0 Current release

## Credits

All texts are from [Aozora Bunko](https://www.aozora.gr.jp/).
Recordings by [ekzemplaro](https://librivox.org/reader/7044) from LibriVox.
Alignment and annotation by [Katsuya Iida](mail:katsuya.iida@gmail.com).

## License

This dataset is in the public domain in the USA (and most likely other countries as well).
There are no restrictions on its use. For more information, please see: 
[librivox.org/pages/public-domain](https://librivox.org/pages/public-domain).