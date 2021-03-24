#!/bin/bash

mkdir ./data
cd ./data
curl -LO https://github.com/kaiidams/Kokoro-Speech-Dataset/releases/download/1.0/kokoro-speech-v1_0.zip
unzip kokoro-speech-v1_0.zip
