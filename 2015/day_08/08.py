if __name__ == "__main__":

    filename = "08-input.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
    f.close()

    code_len = 0
    string_len = 0

    #p1
    for l in lines:
        chars = list(l)
        code_len += len(l)
        chars.pop(0)
        chars.pop()
        while (chars):
            c = chars.pop(0)
            string_len += 1

            #p1
            if c == "\\":
                c = chars.pop(0)
                if c == "x":
                    chars.pop(0)
                    chars.pop(0) 
    print(code_len - string_len)

    #p2
    encoded_len = 0
    for l in lines:
        encoded = '"'
        chars = list(l)
        while (chars):
            c = chars.pop(0)
            if c == '\\':
                encoded += '\\\\'
            elif c == '"':
                encoded += '\\"'
            else:
                encoded += c 
        encoded += '"'
        encoded_len += len(encoded)
    print(encoded_len - code_len)

