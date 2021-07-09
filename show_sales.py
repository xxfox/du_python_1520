import csv


def show_proseed(start=0, end=0):
    start = int(start)
    end = int(end)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        proceeds = csv.reader(f)
        for row in proceeds:
            if end > 0:
                if proceeds.line_num >= start and proceeds.line_num <= end:
                    print(''.join(row))
            elif proceeds.line_num > start:
                print(''.join(row))
            elif start == 0 and end == 0:
                print(''.join(row))


if __name__ == '__main__':
    import sys
    show_proseed(*sys.argv[1:])

