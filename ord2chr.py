# desc: convert ord string to chr string
# sample input: 78 101 118 101 114 32 103 111 110 110 97 32 103 105 118 101 32 121 111 117 32 117 112
# usage:
# - python3 ord2chr.py 
# - python3 ord2chr.py "107 115 111 110 "
# - python3 ord2chr.py "107,115,111,110" ","

import sys

def ord_to_chr(s, sep=' '):
    ords = s.strip().split(sep)
    chars = ""
    for s in ords:
        chars += chr(int(s))
    return chars

if __name__ == "__main__":
    chars = ""
    try: 
        match len(sys.argv):
            case 3:
                chars = ord_to_chr(sys.argv[1], sys.argv[2])
            case 2:
                chars = ord_to_chr(sys.argv[1])
            case _:
                while True: 
                    s = input("enter ord string: ")
                    chars = ord_to_chr(s)
                    print(chars)
        print(chars)
        
    except Exception as e:
        print(e)
        exit()