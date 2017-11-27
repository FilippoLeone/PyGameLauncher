from simplecrypt import encrypt, decrypt
#import codecs
#file_key = open("UserID.battle","r")
with open("UserID.battle","r") as file_key:
    password = file_key.read()
    #file_key.close()
    print(password)
    string="666"
    key = encrypt(password,string)
    #file = open("coins","w")
    with open("coins","wb") as file:
        file.write(key)
    #    file.close()
        quit()
