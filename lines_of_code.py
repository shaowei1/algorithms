import os

if __name__ == '__main__':
    total = 0
    for root, dirs, files in os.walk('../algorithms'):
        for fname in files:
            if fname == 'heap_sort.py':
                continue
            fpath = os.path.join(root, fname)
            with open(fpath) as f:
                total += len(f.readlines())

    print(total)