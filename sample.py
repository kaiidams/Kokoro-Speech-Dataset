import random
import shutil

num_samples = 100
output_dir = 'output'
sample_dir = 'sample'

samples = []
metadata_file = os.path.join(output_dir, 'metadata.csv')
with open(metadata_file, 'rt') as f:
    for line in f:
        samples.append(line)

sampled_lines = random.sample(samples, k=num_samples)
sampled_lines = sorted(sampled_lines)

os.makedirs(sample_dir, exist_ok=False)
with open(os.path.join(sample_dir, 'metadata.csv'), 'wt') as f:
    for line in sampled_lines:
        f.write(line)
        id_, _, _, _ = line.rstrip('\r\n').split('|')
        wav_src_file = os.path.join(output_dir, f'{id_}.wav')
        wav_dst_file = os.path.join(sample_dir, f'{id_}.wav')
        shutil.copyfile(wav_src_file, wav_dst_file)
