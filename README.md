# Kokoro Speech Dataset

Kokoro Speech Dataset is a public domain Japanese speech dataset.
It contains around 36,860 short audio clips of a single speaker reading 8 novel books.
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
    [Online text](https://librivox.org/gongitsune-by-nankichi-niimi/)

## Changelog

- v1.0 Current release

## License

This dataset is in the public domain in the USA (and most likely other countries as well).
There are no restrictions on its use. For more information, please see: librivox.org/pages/public-domain.