import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


SRC_FOLDER = './datasets/imagenet-1k/val'
DST_FOLDER = './datasets/imagenet-1k/val'


def process_func(path):
    idx, path = path
    if not path.endswith('.JPEG'):
        return
    name = os.path.basename(path)
    src = os.path.join(SRC_FOLDER, name)
    fold = name.split('_')[-1].replace('.JPEG', '')
    fold = os.path.join(DST_FOLDER, fold)
    dst = os.path.join(fold, name)
    os.makedirs(fold, exist_ok=True)
    # os.rename(src, os.path.join(fold, name))
    os.system(f'mv {src} {dst}')


def mp_process(func, lines, num_workers=64):
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        new_lines = list(tqdm(executor.map(func, enumerate(lines)), total=len(lines)))
    new_lines = [line for line in new_lines if line is not None]
    return new_lines


files = os.listdir(SRC_FOLDER)

# process_func((0, files[0]))

mp_process(process_func, files)
