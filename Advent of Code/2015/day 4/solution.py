#!/usr/bin/env python3
import hashlib

string = "iwrupvqb"

i = 1

while True:
    m = hashlib.md5() # returns a 128 bit hash
    temp = (string + str(i)).encode() # encodes the string in utf-8
    m.update(temp) # updates the hash with the string
    if m.hexdigest().startswith("00000"): # part 2: startswith("000000")
        print(i)
        break
    i += 1
