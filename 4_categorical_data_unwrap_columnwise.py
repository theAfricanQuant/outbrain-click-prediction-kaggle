# run with pypy

from tqdm import tqdm
import csv

train_file = 'tmp/categorical_joined_train.csv'
test_file = 'tmp/categorical_joined_test.csv'


def copy_columnwise(filename, result_dir):
    with open(filename) as f:
        reader = csv.DictReader(f)
        files = {f: open(f'{result_dir}/{f}.txt', 'w') for f in reader.fieldnames}
        for row in tqdm(reader):
            for k, v in row.items():
                files[k].write(v + '\n')

        for f in files.values():
            f.flush()
            f.close()

print('copy train...')
copy_columnwise(train_file, 'tmp/categorical/train')

print('copy test...')
copy_columnwise(test_file, 'tmp/categorical/test')
