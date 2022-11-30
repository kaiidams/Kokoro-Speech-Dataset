import os
import argparse
import random
import shutil

def main(args):
    samples = []
    metadata_file = os.path.join(args.output_dir, 'metadata.csv')
    with open(metadata_file, 'rt') as f:
        for line in f:
            samples.append(line)

    sampled_lines = random.sample(samples, k=args.num_samples)
    sampled_lines = sorted(sampled_lines)

    os.makedirs(os.path.join(args.sample_dir, 'wavs'), exist_ok=False)
    with open(os.path.join(args.sample_dir, 'metadata.csv'), 'wt') as f:
        for line in sampled_lines:
            f.write(line)
            id_, _, _ = line.rstrip('\r\n').split('|')
            wav_src_file = os.path.join(args.output_dir, 'wavs', f'{id_}.{args.format}')
            wav_dst_file = os.path.join(args.sample_dir, 'wavs', f'{id_}.{args.format}')
            shutil.copyfile(wav_src_file, wav_dst_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default='output', help='Output directory')
    parser.add_argument('--sample-dir', default='sample', help='Sample directory')
    parser.add_argument('--num-samples', type=int, default=10, help='Number of samples')
    parser.add_argument('--format', default='wav', choices=['wav', 'flac', 'mp3', 'ogg'],
        help='Format of clips')

    args = parser.parse_args()
    main(args)
