import sys
from hello import PrintHello

def main(lines):

    for i, v in enumerate(lines):
        print_hello = PrintHello(v)
        print_hello.print_sentence()

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
