# new page created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

#function to encrypt the message
def encrypt(request):
    plaintext = request.GET.get('text', 'default')
    cyphertext = '' #the cyphertext to be returned, inititally assigned to an empty string
    if(len(plaintext)): 
        for plaintext_char in plaintext:#itertating over all characters in the plaintext passed
            if plaintext_char.isalpha(): 
                n = ord('z') + ord('a') #if the character is an alphabtet, find the ascii sum
                if plaintext_char.isupper():
                    n = ord('Z') + ord('A') #if character is uppercase, then modify the sum
                new_char_pos = n - ord(plaintext_char) #find the new character
                cyphertext+=chr(new_char_pos)
            else:
                cyphertext+=plaintext_char #if character is not an alphabet, append it without any change
        params ={'encrypted_text': cyphertext}
    return render(request,'index.html', params) #The encrypted text is returned


#function to decrypt the message
def decrypt(request):
    cyphertext = request.GET.get('text', 'default')
    plaintext = '' #the plaintext to be returned, inititally assigned to an empty string
    if(len(cyphertext)):
        for cyphertext_char in cyphertext: #itertating over all characters in the cyphertext passed
            if cyphertext_char.isalpha():
                n = ord('z') + ord('a') #if the character is an alphabtet, find the ascii sum
                if cyphertext_char.isupper():
                    n = ord('Z') + ord('A') #if character is uppercase, then modify the sum
                new_char_pos = n - ord(cyphertext_char) #find the new character
                plaintext+=chr(new_char_pos)
            else:
                plaintext+=cyphertext_char #if character is not an alphabet, append it without any change
        params ={'decrypted_text': plaintext}
    return render(request,'index.html', params) #The decrypted text is returned