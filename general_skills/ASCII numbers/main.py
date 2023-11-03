data = open("data.txt","r").read().split()
for i in data:
    print(chr(int(i,16)),end="")