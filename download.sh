#!/bin/bash

mkdir ./data
cd ./data
curl -LO https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/1.3/kokoro-speech-v1_3.zip
unzip kokoro-speech-v1_3.zip
