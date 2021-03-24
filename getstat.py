import numpy as np
import argparse
import os
import json

def read_params_list(data_dir, split):
    with open(os.path.join(data_dir, 'index.json')) as f:
        params_list = json.load(f)

    return [
        params
        for params in params_list
        if (split == 'large') or (split in params['sizes'].split())
    ]

def main(args):
    params_list = read_params_list(args.data_dir, args.size)

    audio_lens = []
    for params in params_list:
        id_ = params['id']
        metadata_file = os.path.join(args.data_dir, f'{id_}.metadata.txt')
        with open(metadata_file, 'rt') as metadata_f:
            for line in metadata_f:
                parts = line.rstrip('\r\n').split('|')
                id_, audio_file, audio_start, audio_end, _, _ = parts
                audio_start, audio_end = int(audio_start), int(audio_end)
                audio_lens.append(audio_end - audio_start)

    audio_lens = np.array(audio_lens, dtype=np.float64) / args.sample_rate
    print(f'Total clips: {len(audio_lens):d}')
    print(f'Min duration: {np.min(audio_lens):.3f} secs')
    print(f'Max duration: {np.max(audio_lens):.3f} secs')
    print(f'Mean duration: {np.mean(audio_lens):.3f} secs')
    audio_total_len = int(np.sum(audio_lens))
    h = audio_total_len // 3600
    m = (audio_total_len % 3600) // 60
    s = (audio_total_len % 3600) % 60
    print(f'Total duration: {h:02d}:{m:02d}:{s:02d}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', default='data', help='Data directory')
    parser.add_argument('--size', default='tiny', choices=['tiny', 'small', 'large'],
        help='Size name to get stat')
    parser.add_argument('--sample-rate', type=int, default=22050, help='Expected sampling rate')

    args = parser.parse_args()
    main(args)
