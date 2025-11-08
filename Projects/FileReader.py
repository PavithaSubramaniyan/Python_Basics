import hashlib

def hasfile(filename1, filename2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(filename1, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)
    with open(filename2, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)
    return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hasfile("geeks.txt","geekgs.txt")

if msg1 != msg2:
    print("These files are not identical")
else:
    print("These files are identical")

