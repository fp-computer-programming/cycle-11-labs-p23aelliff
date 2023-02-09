#author ate (2/9/23)

def hex_hash(code):
    return sum([sum([int(i) for i in hex(ord(c)) if i.isdigit()]) for c in code for i in c])
    