import hashlib 

def findit(input, lim):
    idx = 0
    hash = "      "
    while hash[0:lim] != "0"*lim:
        idx += 1
        hash = hashlib.md5(str(input + str(idx)).encode('utf-8')).hexdigest()
    return idx, hash

if __name__ == "__main__":
    input = "bgvyzdsv"

    #p1
    idx, hash = findit(input,5)
    print(idx)
    print(hash)

    #p2
    idx, hash = findit(input,6)
    print(idx)
    print(hash)
