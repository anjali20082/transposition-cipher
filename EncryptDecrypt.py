import math
import hashlib

key="45132"

# Encryption 
def encryptMessage(msg): 


    print("The plain text message to be encrypted is: ",msg)

    # appending hash using MD5
    msgUtf8 = msg.encode("utf-8")
    hash = hashlib.md5(msgUtf8)
    hexa = hash.hexdigest()
    print("The hash of the plain text message is: ",hexa)
    msg_with_hash = msg + hexa
    print("The message concatenated with hash which is to be encrypted is:  ",msg_with_hash)

    msg_len_original = float(len(msg))
    msg_len = float(len(msg_with_hash)) 
     
  
    # calculate number of rows and columns of the transposition matrix 
    columnMatrix = len(key) 
    rowMatrix = int(math.ceil(msg_len / columnMatrix))
    stringMatrix = [['*'] * columnMatrix for i in range(rowMatrix)]
  
   # writing the message string row wise
    k = 0
    for i in range(rowMatrix):
      for j in range(columnMatrix):
        if( k!=(len(msg_with_hash))):
          stringMatrix[i][j] = msg_with_hash[k]
          k = k + 1

    cipher = ""
    #reading the transposition matrix to get the cipher string column wise
    for i in sorted(list(key)):
      iter = key.index(i)
      for j in range(rowMatrix):
        cipher = cipher + stringMatrix[j][iter] 

    return cipher 


    # Decryption 
def decryptMessage(cipher,msg_len_or): 
    
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 
  
    # calculate columns and rows of the transposition matrix 
    columnMatrix = len(key) 
    rowMatrix = int(math.ceil(len(cipher) / columnMatrix)) 
    cipherMatrix = [[''] * columnMatrix for i in range(rowMatrix)]
  

  # writing the cipher columnwise
    k = 0
    for i in sorted(list(key)):
      iter = key.index(i)
      for j in range(rowMatrix):
        if( k!=(len(cipher))):
          cipherMatrix[j][iter] = cipher[k]
          k = k + 1

  # reading the cipher row wise
    plainTextHash = ""
    for i in range(rowMatrix):
      for j in range(columnMatrix):
        if(cipherMatrix[i][j] == "*"):
          break
        plainTextHash = plainTextHash + cipherMatrix[i][j]
    
        
   # getting the plain text and hash out of decrypted cipher string 
    string1 = ""
    string2 = ""

    for i in range(msg_len_or):
      string1 = string1 + plainTextHash[i]
    print("The plain text after decryption is: ",string1)

    for i in range(msg_len_or,len(plainTextHash)):
      string2 = string2 + plainTextHash[i]
    print("The hash received in the concatenated string after decryption is: ",string2)

   # checking if plain text string is matching 
    msgUtf8 = string1.encode("utf-8")
    hash = hashlib.md5(msgUtf8)
    hexa = hash.hexdigest()
     
    print("The hash of the decrypted plain text is: ",hexa) 

    if(hexa==string2):
      print("The hash of plain text after decryption matches to the hash given in the decrypted text. Hence the correct plain text is received")

    return plainTextHash
  

msg = ["hihello","Wearediscoveredsaveyourself", "Hellohowareyou",  "Iamfinehowareyou", "Letsgoforawalk", "Whereisthepark", "Alotofworkispending"]
for i in (msg):
  print("\n")
  cipher = encryptMessage(i) 
  print("The Encrypted Message is:  ",cipher) 
  
  decrypteMsg = decryptMessage(cipher,len(i))
  
  
