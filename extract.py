import os
import torchaudio

output_dir = "./output"
expected_sample_rate = 22050
os.makedirs(output_dir, exist_ok=True)

data = {
    'botchan-by-soseki-natsume-2': 'botchan_1310_librivox_64kb_mp3',  
    'gan-by-ogai-mori': 'gan_1311_librivox_64kb_mp3',  
    'gongitsune-by-nankichi-niimi': 'gongitsune_um_librivox_64kb_mp3',  
    'inakakyoshi-by-katai-tayama': 'inakakyoshi_1311_librivox_64kb_mp3',  
    'kokoro-by-soseki-natsume': 'kokoro_natsume_um_librivox_64kb_mp3',  
    'kusamakura-by-soseki-natsume': 'kusamakura_1311_librivox_64kb_mp3',  
    'meian-by-soseki-natsume': 'meian_1403_librivox_64kb_mp3',  
    'nowaki-by-soseki-natsume': 'nowaki_um_librivox_64kb_mp3',  
}

for k, v in data.items():
    source_file = f'data/{k}.source.txt'
    audio_dir = f'data/{v}'
    with open(source_file, 'rt') as source_f:
        current_file = None
        current_audio = None
        for line in source_f:
            parts = line.rstrip('\r\n').split('|')
            id_, audio_file, audio_start, audio_end = parts
            audio_start, audio_end = int(audio_start), int(audio_end)
            if current_file != audio_file:
                file = os.path.join(audio_dir, audio_file)
                print(f'Reading {file}')
                y, sr = torchaudio.load(file)
                assert len(y.shape) == 2 and y.shape[0] == 1
                assert sr == expected_sample_rate
                current_file = audio_file
                current_audio = y
            output_file = os.path.join(output_dir, f'{id_}.wav')
            print(f'Writing {output_file}')
            y = current_audio[:, audio_start:audio_end]
            torchaudio.save(output_file, y, expected_sample_rate)

all_transcript_file = os.path.join(output_dir, 'transcripts.txt')
with open(all_transcript_file, 'wt') as all_transcript_f:
    for k, v in data.items():
        transcript_file = f'data/{k}.transcript.txt'
        with open(transcript_file, 'rt') as transcript_f:
            for line in transcript_f:
                all_transcript_f.write(line)

