# -*- coding:utf-8 -*-

import sys
from operator import itemgetter
from itertools import groupby

def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = read_input(sys.stdin)
    for key,kviter in groupby(data,itemgetter(0)):


if __name__ == '__main__':
    main()