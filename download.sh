#!/bin/bash

mkdir ./data
cd ./data

curl -LO https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/0.1/kokoro-20210321.zip
curl -LO http://www.archive.org/download//meian_1403_librivox/meian_1403_librivox_64kb_mp3.zip
curl -LO http://www.archive.org/download//kokoro_natsume_um_librivox/kokoro_natsume_um_librivox_64kb_mp3.zip
curl -LO http://www.archive.org/download//inakakyoshi_1311_librivox/inakakyoshi_1311_librivox_64kb_mp3.zip
curl -LO http://www.archive.org/download//kusamakura_1311_librivox/kusamakura_1311_librivox_64kb_mp3.zip
curl -LO http://www.archive.org/download//botchan_1310_librivox/botchan_1310_librivox_64kb_mp3.zip
curl -LO http://www.archive.org/download/nowaki_um_librivox/nowaki_um_librivox_64kb_mp3.zip
curl -LO http://www.archive.org/download//gan_1311_librivox/gan_1311_librivox_64kb_mp3.zip
curl -LO http://archive.org/download/gongitsune_um_librivox/gongitsune_um_librivox_64kb_mp3.zip

unzip kokoro-20210321.zip
unzip meian_1403_librivox_64kb_mp3.zip -d meian_1403_librivox_64kb_mp3
unzip kokoro_natsume_um_librivox_64kb_mp3.zip -d kokoro_natsume_um_librivox_64kb_mp3
unzip inakakyoshi_1311_librivox_64kb_mp3.zip -d inakakyoshi_1311_librivox_64kb_mp3
unzip kusamakura_1311_librivox_64kb_mp3.zip -d kusamakura_1311_librivox_64kb_mp3
unzip botchan_1310_librivox_64kb_mp3.zip -d botchan_1310_librivox_64kb_mp3
unzip nowaki_um_librivox_64kb_mp3.zip -d nowaki_um_librivox_64kb_mp3
unzip gan_1311_librivox_64kb_mp3.zip -d gan_1311_librivox_64kb_mp3
unzip gongitsune_um_librivox_64kb_mp3.zip -d gongitsune_um_librivox_64kb_mp3
