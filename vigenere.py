import string
def encrypt_decrypt(a,b,c):
    x = 'abcdefghijklmnopqrstuvwxyz'
    encrypt_plain = ' '
    key_index = 0
    for  i in a:
        if i == ' ':
            encrypt_plain += ' '
        elif not i.isalpha():
            encrypt_plain += i
        else:
            key_char =  b[key_index % len(b)]
            key_index += 1
            #The above 2 lines worked like below example.
            #key_index % len(key) is 0 % 6 = 0, so key_char = 'p'
            # when b = 'python'.
            # This 2 lines define which character of the key should be 
            # choosed correctly. when b = python the dunction works like 
            # key index is 0 and the lenth of python is 6 so 0/6 has 
            # the remainder 0 so it chooses the 0 index letter which is P
            
            order = x.index(key_char)
            # The above line find the index number of the selected character
            index = x.index(i)
            # if index == -1:
            #     encrypt_plain += i
            # else:
            new_index = (index + (order*c)) % len(x) 
            encrypt_plain += x[new_index]
            
    return encrypt_plain

print()   
print('Welcome To Vigenere Cipher Program')    
print()  

a = 'You want to encrypt or decrypt?'    
print(a.title()) 
print()  
b = str(input('Encrypt/Decrypt:\n')).lower()  
  
if b == 'encrypt':
    print('Encryptiopn mode is activated')
    print()
    k = input('Give your Text: ').lower()
    y = input('Give Your key: ').lower()
    d = 1
    print(f'Your Encryption is finished.\nHere is your message: {encrypt_decrypt(k,y,d)}')
else:
    print('Decryptiopn mode is activated')
    print()
    k = input('Give your Text: ').lower()
    y = input('Give Your key: ').lower()
    d = -1
    print(f'Your Decryption is finished.\nHere is your message: {encrypt_decrypt(k,y,d)}')
