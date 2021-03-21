import numpy as np

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

s = []
for k, v in data.items():
    source_file = f'data/{k}.source.txt'
    audio_dir = f'data/{v}'
    with open(source_file, 'rt') as source_f:
        for line in source_f:
            parts = line.rstrip('\r\n').split('|')
            id_, audio_file, audio_start, audio_end = parts
            audio_start, audio_end = int(audio_start), int(audio_end)
            s.append(audio_end - audio_start)

s = np.array(s, dtype=np.float64) / 22050.0
print(f'Min: {np.min(s):.3f}')
print(f'Max: {np.max(s):.3f}')
print(f'Mean: {np.mean(s):.3f}')
print(f'Std: {np.std(s):.3f}')
print(f'Total: {np.sum(s):.3f}')