import getpass
import base64

# ask for username - will be displayed when typed
uname = input("Enter your username : ")

# ask for password - will not be displayed when typed
p = getpass.getpass(prompt="Enter your password: ")

# contruct credential with *.* as separator between username and password
creds = uname + "*.*" + p

# Encrypt given set of credentials
def encryptcredential (pwd) :
    rvalue = base64.b64encode (pwd.encode())
    return rvalue

# Decrypt a give set of credentials
def decryptcredential (pwd) :
    rvalue = base64.b64decode(pwd)
    rvalue=rvalue.decode ()
    return rvalue

encryptedcreds = encryptcredential (creds)
print ("Simpe creds: " + creds)
print ("Encrypted creds: " + str(encryptedcreds))
print ("Decrypted creds: " + decryptcredential(encryptedcreds))
