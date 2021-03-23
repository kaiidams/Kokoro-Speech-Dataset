#!/bin/bash

mkdir ./data
cd ./data
curl -LO https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/0.2/kokoro-speech-v0.2.zip
unzip kokoro-speech-v0.2.zip
