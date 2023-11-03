import hashlib
from pwn import *
import re



def main():
	
    
    conn = remote('jupiter.challenges.picoctf.org', 15130)
        
    try:
        # conn.recvline() is going to receive a line from the server and 
        # store it on the variable serverOutput
        serverOutput = conn.recv().decode().splitlines()[2]
        print(serverOutput)
        serverOutput = serverOutput.split()[3:-3]
        print(serverOutput)
        buf = ""
        for num in serverOutput:
            print(int(num,2),end=" ")
            buf += str(chr(int(num,2)))
        buf += "\n"
        print(buf)
        conn.send(buf.encode())
        out = conn.recv(1024).decode().splitlines()[0].split()[4:-3]
        buf = ""
        for num in out:
            print(int(num,8),end=" ")
            buf += str(chr(int(num,8)))
        buf += "\n"
        conn.send(buf.encode())
        print(out)
        out = conn.recv(1024).decode().splitlines()[0].split()[4]
        print(out)
        buf = bytearray.fromhex(out).decode()
        buf += "\n"
        print(buf)
        conn.send(buf.encode())
        print(out)
        out = conn.recv(1024).decode()
        print(out)
        
        
        
        # # If the variable serverOutput has the string Incorrect, it means
        # # that the generateMD5Hash is wrong, therefore I print out (to 
        # # myself) fix the code!! XD and I break the loop, line 30.
        # if 'Incorrect.' in serverOutput.decode():
        #     print("Wrong hash. Fix the code!! ")
        #     break
        # # If the variable serverOutput has the string Answer, it means
        # # we have to send an answer to the server, the hashing of the 
        # # string keyword, in this case the challenge is in the 2nd 
        # # position of the variable challenge (initiated before)
        # elif 'Answer:' in serverOutput.decode():
        #     conn.send((generateMD5Hash(challenge[1]) + '\n').encode())
        # # If the variable serverOutput has the string Answer, it means
        # # If the variable serverOutput has the string picoCTF{, it means
        # # we have found the flag!! We have the solution, and what I do is 
        # # simply get it from the serverOutput variable and print it out 
        # # to the user
        # elif 'picoCTF{' in serverOutput.decode():
        #     flag = re.findall('picoCTF{.*}', serverOutput.decode())
        #     print("The flag is: " + flag[0])
        #     break
        # # If the variable serverOutput has the string ' it means
        # # we have the challenge message to hash later, what I do is
        # # I simply store it in the variable challenge, to be called
        # # later in the iteration of the loop, once the word Answer is 
        # # in the serverOutput (line 35)
        # elif "'" in serverOutput.decode():
        #     challenge = serverOutput.decode().split("'")
        # else:
        #     continue
    except EOFError as e:
        print(e)

main()