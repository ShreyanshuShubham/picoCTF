
with open("lyrics_2.txt","r") as f:
    data = f.read().splitlines()
    print(data)
    buf = ""
    for i in data:
        buf += str(chr(int(i)))
    print("picoCTF{",buf,"}",sep="")