import itertools
import hashlib

s = 'yzbqklnj'
for idx in itertools.count():
    check = s + str(idx)
    sha = hashlib.md5(check.encode()).hexdigest()
    if sha.startswith("00000"):
        print(idx, sha)
        break
