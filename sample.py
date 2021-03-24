import random
import shutil

def main(args):
    samples = []
    metadata_file = os.path.join(output_dir, 'metadata.csv')
    with open(metadata_file, 'rt') as f:
        for line in f:
            samples.append(line)

    sampled_lines = random.sample(samples, k=num_samples)
    sampled_lines = sorted(sampled_lines)

    os.makedirs(os.path.join(sample_dir, 'wavs'), exist_ok=False)
    with open(os.path.join(sample_dir, 'metadata.csv'), 'wt') as f:
        for line in sampled_lines:
            f.write(line)
            id_, _, _, _ = line.rstrip('\r\n').split('|')
            wav_src_file = os.path.join(output_dir, 'wavs', f'{id_}.wav')
            wav_dst_file = os.path.join(sample_dir, 'wavs', f'{id_}.wav')
            shutil.copyfile(wav_src_file, wav_dst_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', default='output', help='Output directory')
    parser.add_argument('--sample-dir', default='sample', help='Sample directory')
    parser.add_argument('--num-samples', type=int, default=100, help='Number of samples')

    args = parser.parse_args()
    main(args)
