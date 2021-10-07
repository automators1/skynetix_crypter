import random

alfa=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
delimiters=["+","-","/","*"]


def crypter(text):
    crypted=""
    flag=0
    for letter in text:
        r=random.randrange(0,4)
        if r==0:
            delimiter="+"
        elif r==1:
            delimiter="-"
        elif r==2:
            delimiter="/"
        elif r==3:
            delimiter="*"

        if letter=="\n":
            crypted+=f"[{random.randrange(0,9)}{delimiter}{random.randrange(0,9)}]"
            flag=0
        elif letter==" ":
            crypted+=f"({random.randrange(0,9)}{delimiter}{random.randrange(0,9)})"
            flag=0
        else:
            crypted+=str(alfa.index(letter.upper()))+delimiter
            flag=1
    if flag==1:
        print(crypted[:-1])
        file=open("data/output","w")
        file.write(crypted[:-1])
        file.close()
    else:
        print(crypted)
        file=open("data/output","w")
        file.write(crypted)
        file.close()





def decrypter(text):
    skips=0
    decrypted=""
    token=""
    for letter in text:

        if skips>0:
            skips-=1
            continue
        
        if letter in delimiters:
            decrypted+=str(alfa[int(token)])
            token=""
        elif letter=="(":
            skips=4
            decrypted+=" "
        elif letter=="[":
            skips=4
            decrypted+="\n"
        else:
            token+=letter

    
    
    print(decrypted.lower())
    file=open("data/input","w")
    file.write(decrypted.lower())
    file.close()


        






inp=input("Crypt or Decrypt? c/d")

if inp=="c" or inp=="crypter":
    file=open("data/input","r")
    text=file.read()
    file.close()
    crypter(text)
else:
    file=open("data/output","r")
    text=file.read()
    file.close()
    decrypter(text)


