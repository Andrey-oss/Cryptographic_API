# Developer - t.me/Andreyoss

rot13_cipher_encrypt = "abcdefghijklmnopqrstuvwxyz"
rot13_cipher_decrypt = "zyxwvutsrqponmlkjihgfedcba"

# For tests

static_binary_enc = 123
static_binary_dec = 1111011
binary_enc = "ABC"
binary_dec = "010000010100001001000011"
reverse_dec = "CBA"
reverse_enc = "ABC"
rot13_enc = "hello"
rot13_dec = "uryyb"

class encrypt:
    @staticmethod
    def rot13(txt):
        rot13_output = "".join([rot13_cipher_encrypt[(rot13_cipher_encrypt.find(c)+13)%26] for c in txt.lower()])
        return rot13_output
    @staticmethod
    def reverse(txt):
        reverse_output = txt[::-1]
        return reverse_output
    @staticmethod
    def static_binary(txt):
        try:
           static_binary_output = bin(txt)[2:]
        except Exception:
           raise TypeError("Must be entered Integer not String!")
        return static_binary_output
    @staticmethod
    def binary(txt):
        binary_output = ''.join(format(ord(i[0]), '08b') for i in txt)
        return binary_output

class decrypt:
    @staticmethod
    def reverse(txt):
        reverse_output = txt[::-1]
        return reverse_output
    @staticmethod
    def rot13(txt):
        rot13_output = "".join([rot13_cipher_decrypt[(rot13_cipher_decrypt.find(c)+13)%26] for c in txt.lower()])
        return rot13_output
    @staticmethod
    def static_binary(txt):
        try:
           static_binary_output = int(str(txt), 2)
        except Exception:
           raise TypeError("Integer must be only 0 or 1!")
        return static_binary_output
    @staticmethod
    def binary(txt):
        binary_output = ''.join(chr(int(txt[i*8:i*8+8],2)) for i in range(len(txt)//8))
        return binary_output

class tests:
    @staticmethod
    def static_binary_encrypt():
        print ("Input data: "+str(static_binary_enc))
        print ("Output data: "+str(encrypt.static_binary(static_binary_enc)))
    @staticmethod
    def static_binary_decrypt():
        print ("Input data: "+str(static_binary_dec))
        print ("Output data: "+str(decrypt.static_binary(static_binary_dec)))
    @staticmethod
    def binary_encrypt():
        print ("Input data: "+str(binary_enc))
        print ("Output data: "+str(encrypt.binary(binary_enc)))
    @staticmethod
    def binary_decrypt():
        print ("Input data: "+str(binary_dec))
        print ("Output data: "+str(decrypt.binary(binary_dec)))
    @staticmethod
    def reverse_encrypt():
        print ("Input data: "+str(reverse_enc))
        print ("Output data: "+str(encrypt.reverse(reverse_enc)))
    @staticmethod
    def reverse_decrypt():
        print ("Input data: "+str(reverse_dec))
        print ("Output data: "+str(decrypt.reverse(reverse_dec)))
    @staticmethod
    def rot13_encrypt():
        print ("Input data: "+str(rot13_enc))
        print ("Output data: "+str(encrypt.rot13(rot13_enc)))
    @staticmethod
    def rot13_decrypt():
        print ("Input data: "+str(rot13_dec))
        print ("Output data: "+str(decrypt.rot13(rot13_dec)))

# DOCUMENTATION
#
# 1. How to start working with it library
#
# Just copy and paste this module to your project and import it
# > import cryptographic_api
# >
#
# 2. How to use it
#
# > print (cryptographic_api.encrypt/decrypt.rot13/binary/static_binary/reverse(SOME_TEXT))
# Example for encrypt:
# > print (cryptographic_api.encrypt.rot13('hello'))
# uryyb
#
# > Example for decrypt:
# > print (cryptographic_api.decrypt.rot13('uryyb'))
# hello
# Also you can test how cipher algorithms work
# > print (cryptographic_api.tests.binary_encrypt())
# Input data: ABC
# Output data: 010000010100001001000011
#
# 3. What about exceptions
#
# > print (cryptographic_api.decrypt.binary('qwerty'))
# TypeError(Integer must be only 0 or 1!)
#
# This error can be displayed if you entered wrong value (in the example is symbols from alphabet) 
