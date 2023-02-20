import sys


try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except (IndexError, ValueError):
    print(f'Usage: {sys.argv[0]} HOST PORT', file=sys.stderr)
    exit(1)


def main():
    pass


if __name__ == '__main__':
    main()
