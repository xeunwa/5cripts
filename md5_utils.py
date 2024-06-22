import hashlib 
import itertools 

def generate_md5(word):
    md5_hash = hashlib.md5()
    md5_hash.update(word.encode('utf-8'))
    return md5_hash.hexdigest()

def create_md5_table(payload, file='md5.txt'):
    """
    Generate md5 rainbow table with the format MD5:raw_string 
    """
    with open(file, 'w') as f:
        for s in payload:
            md5_hash = generate_md5(s)
            f.write(f"{md5_hash}:{s}\n" )

def read_md5_table(file='md5.txt', sep=':'):
    """
    Read md5 rainbow table format MD5:raw_string.
    """ 
    table = {}
    with open(file, 'r') as f:
        for x in f.readlines():
            md5_hash, s = x.strip().split(sep)
            table[md5_hash] = s
    return table

def example():
    # sample 4 char generator
    wordlist = [''.join(chars) for chars in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4)]
    create_md5_table(wordlist)
    rainbow_table = read_md5_table()
    # string to md5
    print(generate_md5("533D"))
    # reverse lookup
    print(rainbow_table["d1f22a6d8d592222c973c9ce53defff8"])

