# desc: convert ord string to chr string
# input: "Never gonna give you up"
# usage:
# - python3 ord2chr.py 
# - python3 ord2chr.py adam
# - python3 ord2chr.py "adam" ","

import sys

def chr_to_ord(s, sep=" "):
    ords = []
    for c in s:
        ords.append(str(ord(c)))
    ords = sep.join(ords)
    return ords

if __name__ == "__main__":
    ords = ""
    try: 
        match len(sys.argv):
            case 3:
                ords = chr_to_ord(sys.argv[1], sys.argv[2])
            case 2:
                ords = chr_to_ord(sys.argv[1])
            case _:
                while True: 
                    s = input("enter string: ")
                    ords = chr_to_ord(s)
                    print(ords)
        print(ords)
        
    except Exception as e:
        print(e)
        exit()