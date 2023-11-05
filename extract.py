import os
import sys
import json
import torchaudio
import torch
import argparse


def err_print(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def read_params_list(data_dir, size):
    index_file = os.path.join(data_dir, 'index.json')
    if not os.path.exists(index_file):
        err_print("`data/index.json' is not found. Please download it from the project page.")
        sys.exit(1)

    with open(os.path.join(data_dir, 'index.json')) as f:
        params_list = json.load(f)

    return [
        params
        for params in params_list
        if (size == 'xlarge') or (size in params['sizes'].split())
    ]


def check_data_directory(data_dir, params_list):
    isok = True
    for params in params_list:
        id_ = params['id']
        audio_dir = os.path.join(data_dir, f'{id_}')
        if not os.path.isdir(audio_dir):
            err_print(f"`{audio_dir}' is missing.")
            isok = False
    if isok:
        err_print("All audio directories exist.")
    return isok


def dump_script(data_dir, params_list):
    err_print('Run these commands to download archives.')
    err_print()

    print(f'cd {data_dir}')

    for params in params_list:
        archive_url = params['archive_url']
        print(f'curl -LO {archive_url}')

    for params in params_list:
        id_ = params['id']
        archive_url = params['archive_url']
        archive_file = os.path.basename(archive_url)
        print(f"unzip {archive_file} -d {id_}")


def extract_wav_files(data_dir, params_list, clip_format, sample_rate, output_dir):

    clip_dir = 'wavs'
    clip_ext = clip_format

    os.makedirs(os.path.join(output_dir, clip_dir), exist_ok=True)
    max_int16 = torch.iinfo(torch.int16).max

    for params in params_list:
        id_ = params['id']
        metadata_file = os.path.join('data', f'{id_}.metadata.txt')
        audio_dir = os.path.join('data', f'{id_}')
        with open(metadata_file, 'rt') as metadata_f:
            current_file = None
            current_audio = None
            for line in metadata_f:
                parts = line.rstrip('\r\n').split('|')
                id_, audio_file, audio_start, audio_end, _, _ = parts
                audio_start, audio_end = int(audio_start), int(audio_end)
                if current_file != audio_file:
                    file = os.path.join(audio_dir, audio_file)
                    err_print(f'\rReading {file}', end='')
                    y, sr = torchaudio.load(file)
                    assert len(y.shape) == 2 and y.shape[0] == 1
                    assert y.dtype == torch.float32
                    assert sr == sample_rate
                    y = (y * max_int16 / torch.max(torch.abs(y))).to(torch.int16)
                    current_file = audio_file
                    current_audio = y
                output_file = os.path.join(output_dir, clip_dir, f'{id_}.{clip_ext}')
                y = current_audio[:, audio_start:audio_end]
                torchaudio.save(output_file, y, sample_rate)


def write_metafile(data_dir, params_list, output_dir):

    metadata_file = os.path.join(output_dir, 'metadata.csv')
    with open(metadata_file, 'wt') as metadata_f:
        for params in params_list:
            id_ = params['id']
            metadata_file = os.path.join('data', f'{id_}.metadata.txt')
            with open(metadata_file, 'rt') as transcript_f:
                for line in transcript_f:
                    parts = line.rstrip('\r\n').split('|')
                    id_, _, _, _, text, voca = parts
                    metadata_f.write(f'{id_}|{text}|{voca}\n')


def main(args):

    params_list = read_params_list(args.data_dir, args.size)
    assert params_list

    if not check_data_directory(args.data_dir, params_list):
        dump_script(args.data_dir, params_list)
    else:
        extract_wav_files(args.data_dir, params_list, args.format, args.sample_rate, args.output_dir)
        write_metafile(args.data_dir, params_list, args.output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', default='data', help='Data directory')
    parser.add_argument('--output-dir', default='output', help='Output directory')
    parser.add_argument(
        '--size', default='tiny', choices=['tiny', 'small', 'large', 'xlarge'],
        help='Size name to extract')
    parser.add_argument(
        '--format', default='wav', choices=['wav', 'flac', 'mp3', 'ogg'],
        help='Format of clips')
    parser.add_argument('--sample-rate', type=int, default=22050, help='Expected sampling rate')

    args = parser.parse_args()
    main(args)
