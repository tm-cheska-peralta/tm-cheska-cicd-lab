import argparse
import os

def print_nums(num_a, num_b):
    print(f'num_a: {num_a}')
    print(f'num_b: {num_b}')
    print(f'sum: {num_a + num_b}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_a', type=float)
    parser.add_argument('--num_b', type=float)

    args = parser.parse_args()

    print_nums(args.num_a, args.num_b)