alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode_function(message, key ):
    key=int(key)
    encrypted_message=""
    for i in range(len(message)):
        index=alphabet.index(message[i])
        index =(index + key)%len(alphabet)
        if(index>25):
            index= index-25
            encrypted_message += alphabet[index]
            index=0
        else:
            encrypted_message +=alphabet[index]
            index=0
    print(f"encrypted message: {encrypted_message}")
def decode_function(message,key):
    decrypted_message=""
    for i in message:
       originalkey= alphabet.index(i)-int(key)
       originalkey %=len(alphabet)
       decrypted_message +=alphabet[originalkey]
    print(decrypted_message)



direction=input("Type 'encode' to encrypt, type 'decode' to decode the message ")
message=input("Type your message").lower()
key=input("Enter key to shift alphabets")
if(direction=="encode"):
    encode_function(message,key)

else:
    decode_function(message,key)




#def decode_function(message,key)