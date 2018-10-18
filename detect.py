"""
detect.py

Reads input from command line and calls plagiarism detection script

Manav Goel
"""
import sys
from plagiarism_detection import PlagDetect


def main():
    try:
        global my_check

        if len(sys.argv) == 4:
            my_check = PlagDetect(sys.argv[1], sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 5:
            my_check = PlagDetect(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))

        print(str(my_check.plag_percent()) + '%')

    except Exception as e:
        print(e)
        print('usage: python detect.py syn_file file_1 file_2 [tuple_len]')
        print(' synfile: file containing list of synonyms')
        print(' file_1: input file 1')
        print(' file_2: input file 2')
        print(' [tuple_len]: (optional arg) tuple size, must be greater than 0 and less than size of both files')


if __name__ == '__main__':
    main()
