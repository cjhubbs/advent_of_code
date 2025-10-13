def see_say_split(s):
    substrings = []
    prev_char = s[0]
    substr = s[0]
    for idx in range(1,len(s)):
        if s[idx] == prev_char:
            substr += s[idx]
        else:
            substrings.append(substr)
            substr = s[idx]
            prev_char = s[idx]
    substrings.append(substr)
    return substrings

def see_say(items):
    new_str = ""
    for i in items:
        new_str += str(len(i))
        new_str += i[0]
    return new_str

if __name__ == "__main__":
    input = "1321131112"
    iterations = 50
    for i in range(iterations):
        input = see_say(see_say_split(input))
    print(len(input))
