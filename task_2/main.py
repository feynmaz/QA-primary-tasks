import sys
import hashlib
import os
from functools import partial


BLOCK_SIZE = 4096


def get_hash(file, hash_type):
    hash = get_hash_object_of_type(hash_type)

    with open(file, 'rb') as f:
        for block in iter(partial(f.read, BLOCK_SIZE), b''):
            hash.update(block)

    return hash


def get_hash_object_of_type(type):
    if type == 'md5':
        return hashlib.md5()
    elif type == 'sha1':
        return hashlib.sha1()
    elif type == 'sha256':
        return hashlib.sha256()
    else:
        raise ValueError('Алгоритм хеширования указан некорректно')


def compare_hash(calculated_hash, entered_hash):
    if calculated_hash == entered_hash:
        return 'OK'
    else:
        return 'FAIL'


input_file = sys.argv[1]
files_dir = sys.argv[2]

lines = open(input_file, 'r').readlines()

for line in lines:
    instructions = line.replace('\n', '').split(' ')
    file = os.path.join(files_dir, instructions[0])
    if os.path.exists(file):
        hash = get_hash(file, instructions[1])
        result = compare_hash(hash.hexdigest(), instructions[2])
    else:
        result = 'NOT FOUND'

    print(result)
