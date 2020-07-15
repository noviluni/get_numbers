import pandas as pd


def sort_csv(path):
    df = pd.read_csv(path)
    df.sort_values(by=['number'], ascending=True).to_csv(path, index=False)


def check_missing_numbers(path, max_number, min_number=0):
    df = pd.read_csv(path)
    print('Checking missing numbers...')
    for number in range(int(min_number), int(max_number) + 1):
        if number not in df.number.values:
            print(f'- The number {number} is missing.')
    print('Checking completes')
