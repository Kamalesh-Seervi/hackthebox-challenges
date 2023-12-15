def decrypt(msg):
    pt = []
    for char in msg:
        char= char-18
        char=179*char%256
        pt.append(char)
    return bytes(pt)

with open("msg.enc") as f:
    ct=bytes.fromhex(f.read())
print(decrypt(ct))