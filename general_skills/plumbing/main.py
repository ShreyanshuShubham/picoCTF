import pwn

# jupiter.challenges.picoctf.org 14291
conn = pwn.remote("jupiter.challenges.picoctf.org",14291)

while True:
    try:
        data = conn.recvline().decode()
        if data.startswith("pico"):
            print(data)
            break
    except:
        pass