#key="45132"
import math
import hashlib
from itertools import permutations

def BruteForceDecrypt(cipher,length_original,key): 
    
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
    print(plainTextHash)
        
   # getting the plain text and hash out of decrypted cipher string 
    string1 = ""
    string2 = ""

    for i in range(length_original):
      string1 = string1 + plainTextHash[i]
    print("The plain text after decryption is: ",string1)

    for i in range(length_original,len(plainTextHash)):
      string2 = string2 + plainTextHash[i]
    print("The hash received in the concatenated string after decryption is: ",string2)

   # checking if plain text string is matching 
    msgUtf8 = string1.encode("utf-8")
    hash = hashlib.md5(msgUtf8)
    hexa = hash.hexdigest()
     
    print("The hash of the decrypted plain text is: ",hexa) 

    if(hexa==string2):
      print("The hash of plain text after decryption matches to the hash given in the decrypted text. Hence the correct plain text is received")

    return string1
  
# making a dictionary of plain text and corresponding cipher texts as key value pairs
ptext_ctext_pairs = {'Wearediscoveredsaveyourself': 'asrvr8047724eodyefb6a95*rcees1ff7f1aWdvsol7d9ed3eieauf7378d1', 
        'Hellohowareyou': 'lwoffa3ee*or5dc081a*lauf075a7*Hhe92743e5eoy5a5897*', 
        'Iamfinehowareyou': 'mhed9b640aiwof2e32f*foy1e2f4e*Inau8ddc73aerc4118fd',
        'Letsgoforawalk': 'tole3f4ef*ga0572400*srked4ef1*Lowcbd003cefa5c9347*',
        'Whereisthepark': 'etr62a2e1*ee65264c2*rhk706702*Wipd668e83hsab670c2*',
         'Alotofworkispending' : 'oopn02ddd6*oknca40a6b*treg7fb3ea*Afid65e2e29lwsia89792*'}

found = 0
index = 0
appendKey = ['3','4','5','6','7','8']   # for making different combination of keys
initialKey = '12'    # taking initial  key for permutations
while(found != 1):
  print("\n")
  p = permutations(initialKey,len(initialKey))
  
  for k in p:
    key = "".join(k)
    print("Using key: ",key)
    for i in ptext_ctext_pairs.keys():
      decryptMsg = BruteForceDecrypt(ptext_ctext_pairs[i], len(i), key)    # finding the decrypted message for a cipher
      Flag = 1
      if (decryptMsg != i):     # checking if decrypted message is equal to corresponding plain text
        Flag = 0
        break
    print("\n")
    if(Flag == 1):
      print("Key Found : ", key)   # Output the key found
      found = 1
      break
  initialKey = initialKey + appendKey[index]
  index = index + 1
