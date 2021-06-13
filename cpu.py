import hashlib
import time
def eatcpu():
    cool_string: str = b'a' * 1000
    i = 0
    while i < 1000:
        print('cpu loop')
        hasher = hashlib.md5()
        hasher.update(cool_string)
        x = 1 + 2 # not very cpu intensive
        digest = hasher.hexdigest()
        time.sleep(2)
