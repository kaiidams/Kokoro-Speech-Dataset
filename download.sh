#!/bin/bash

mkdir ./data
cd ./data
curl -LO https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/1.2/kokoro-speech-v1_2.zip
unzip kokoro-speech-v1_2.zip
