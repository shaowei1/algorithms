import os
from binascii import hexlify

import numpy as np
import random
import typing
import struct


def generate_list(n: int = 7, s: int = 100) -> typing.List[int]:
    """
    生成一个长度为n，总和为s的list
    :param n: 
    :param s: 
    :return: 
    """
    if n is 1:
        return [s]
    if n is 0:
        return []
    else:
        partial = random.randint(0, s)
        remaining = s - partial
        left_number = int(n / 2)
        right_number = n - left_number
        return generate_list(n=left_number, s=partial) + generate_list(n=right_number, s=remaining)


def generate_source_file(filename: str = 'source.txt', size: int = 1000):
    """
    生成一个占 size byte 的文件(1 byte = 8bits)
    :param filename:
    :param size:
    :return:
    """
    if os.path.exists(filename):
        os.remove(filename)
    library = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    random_factor = random.randint(1, 5) * 100
    probability = list()

    for key in generate_list(n=len(library), s=random_factor):
        probability.append(key / random_factor)
    print(probability)
    source = np.random.choice(library, size=size, replace=True, p=probability)
    for key in source:
        # r、rb、r+、rb+、w、wb、w+、wb+、a、ab、a+、ab+
        open(filename, 'a').write(key)
    source_size = os.path.getsize(filename)
    print(source_size)


def compress(source: str = 'source.txt', target: str = 'compress.bnr'):
    if not os.path.exists(source):
        print('please run generate_source_file for the first')

    mapping = dict()
    with open(source) as f:
        while True:
            value = f.read(1)
            if not value:
                break
            if value in mapping:
                mapping[value] += 1
            else:
                mapping[value] = 1
    print(f'mapping: {mapping}')

    inversion_mapping = dict()
    for key, value in mapping.items():
        if key in inversion_mapping:
            inversion_mapping[value].append(key)
        else:
            inversion_mapping[value] = [key]

    num_sorted = list()
    for index, key in enumerate(inversion_mapping.keys()):
        if index is 0:
            num_sorted.append(key)
        else:
            whether_insert = False
            for inner, value in enumerate(num_sorted):
                if num_sorted[inner] <= key:
                    num_sorted.insert(inner, key)
                    whether_insert = True
                    break
            if not whether_insert:
                num_sorted.append(key)
    # 对已经排好序的字符进行编码
    encoding = dict()
    count = 0
    for key in num_sorted:
        for value in inversion_mapping.get(key):
            encoding[value] = f"{count * '0'}1"
            count += 1
    print(f'encoding: {encoding}')

    expect_length = sum((value * len(encoding.get(key)) for key, value in mapping.items()))

    if os.path.exists(target):
        os.remove(target)
    fb = open(target, 'ab')
    key_jar = ''
    decoding = {value: key for key, value in encoding.items()}
    for key, value in decoding.items():
        key_jar += key + value
    key_jar += '|'
    length = len(key_jar)
    bytes_number = length + length % 8

    e = struct.pack(f'{bytes_number}s', key_jar.encode())
    fb.write(e)
    bits = ''
    bits_length = 8 * 8
    with open(source) as f:
        while True:
            value = f.read(1)
            if not value:
                break
            bits += encoding.get(value)
            if len(bits) >= bits_length:
                write_bytes(fb, bits[:bits_length])
                bits = bits[bits_length:]
    print(f'left length of bits: {len(bits)}: bits: {bits}')
    write_bytes(fb, bits)
    fb.close()
    source_size = os.path.getsize(source)
    target_size = os.path.getsize(target)
    print(f'source size: {source_size}')
    print(f'target size: {target_size}')
    print(f'expect size: {(expect_length + bits_length - len(bits)) / 8 + length}')
    print(f'compress radio: {source_size // target_size} : 1')


def write_bytes(fb, bits: str = '10111111111111111011110'):
    """
    struct 模块可以要发送的数据长度转换成固定长度的字节
    :param fb:
    :param bits:     bits = "10111111111111111011110"  # example string. It's always 23 bits
    :return:
    """
    # base 进制
    # fb.write(struct.pack('i', int(bits[::-1], 2))) # int  31
    fb.write(struct.pack('Q', int(bits[::-1], base=2)))  # Q -> unsigned long long 8 bits 64
    # fb.write(struct.pack('q', int(bits[::-1], base=2)))  # q -> long long 8 bits 63
    # fb.write(struct.pack('L', int(bits[::-1], base=2)))  # L -> unsigned long 4 bits    32


def uncompress(filename, extra_filename='extra.txt'):
    if not os.path.exists(filename):
        print(f'{filename} is not exist')
        return
    if os.path.exists(extra_filename):
        os.remove(extra_filename)

    decoding = None
    fb = open(f'{extra_filename}', 'a')
    key = ''
    tmb_b = b''
    with open(filename, 'rb') as f:
        while True:
            value = f.read(8)
            if not value:
                break
            if decoding is None:
                tmb_b += value

                if b"|" in value:
                    decoding = dict()
                    key_pem, value = tmb_b.split(b"|", 1)
                    key_jar = struct.unpack(f'{len(key_pem)}s', key_pem)[0].decode()
                    code = ''
                    for i in key_jar:
                        if i == '0' or i == '1':
                            code += i
                        else:
                            decoding[code] = i
                            code = ''

            elif decoding is not None:
                print(f'decoding: {decoding}')
                if len(value) != 8:
                    value += f.read(8 - len(value))
                print(len(value))
                fmt = {
                    4: 'I',
                    8: 'Q',
                }
                data = struct.unpack(fmt.get(len(value)), value)
                key += bin(data[0])[::-1].split('b')[0]
                length = 1
                while True:
                    if key[:length] in decoding:
                        fb.write(decoding.get(key[:length]))
                        key = key[length:]
                        length = 1
                    else:
                        if length >= len(key):
                            break
                        length += 1

    fb.close()
    extra_size = os.path.getsize(extra_filename)
    print(f'extra_size: {extra_size}')
    print(open('source.txt').read())
    print(open(f'{extra_filename}').read())


if __name__ == '__main__':
    # generate_source_file()
    compress()
    uncompress(filename='compress.bnr')
    pass
