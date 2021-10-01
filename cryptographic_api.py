# Developer - https://t.me/Andreyoss
# Version v1.1

from random import choice

rot13_cipher = "abcdefghijklmnopqrstuvwxyz"

# For tests

static_binary_enc = 123
static_binary_dec = 1111011
binary_enc = "ABC"
binary_dec = "010000010100001001000011"
reverse_dec = "CBA"
reverse_enc = "ABC"
rot13_enc = "hello"
rot13_dec = "uryyb"
random_case_enc = "hello"
random_case_dec = "HeLlo"
ascii_enc = "hi"

class encrypt:
    @staticmethod
    def rot13(txt):
        return "".join([rot13_cipher[(rot13_cipher.find(c)+13)%26] for c in txt.lower()])
    @staticmethod
    def reverse(txt):
        return txt[::-1]
    @staticmethod
    def static_binary(txt):
        try:
           static_binary_output = bin(txt)[2:]
        except Exception:
           raise TypeError("Integer required, not string!")
        return static_binary_output
    @staticmethod
    def binary(txt):
        return ''.join(format(ord(i[0]), '08b') for i in txt)
    @staticmethod
    def random_case(txt):
        return ''.join(choice((str.upper, str.lower))(c) for c in txt)
    @staticmethod
    def ascii(txt):
        # WARNING! SHIT CODE!!!
        return str([ord(x) for x in txt]).replace('[', '').replace(']', '').replace(',', '')

class decrypt:
    @staticmethod
    def reverse(txt):
        return txt[::-1]
    @staticmethod
    def rot13(txt):
        return "".join([rot13_cipher[(rot13_cipher.find(c)+13)%26] for c in txt.lower()])
    @staticmethod
    def static_binary(txt):
        try:
           static_binary_output = int(str(txt), 2)
        except Exception:
           raise TypeError("Integer must be only 0 or 1!")
        return static_binary_output
    @staticmethod
    def binary(txt):
        return ''.join(chr(int(txt[i*8:i*8+8],2)) for i in range(len(txt)//8))
    @staticmethod
    def random_case(txt):
        return ''.join(choice((str.upper, str.lower))(c) for c in txt) # Cuz Idk how to decrypt this "shit_cipher" so I just copy N paste from encrypt to decrypt section
    @staticmethod
    def ascii(txt):
        output = ""
        try:
            txt = list(map(int, txt.split()))
        except Exception:
            raise TypeError("Integer required, not string!")
        else:
            for i in txt:
                output = output + chr(i)
            return output

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
    @staticmethod
    def random_case_encrypt():
        print ("Input data: "+str(random_case_enc))
        print ("Output data: "+str(encrypt.random_case(random_case_enc)))
    @staticmethod
    def random_case_decrypt():
        print ("Input data: "+str(random_case_dec))
        print ("Output data: "+str(decrypt.random_case(random_case_dec)))
    @staticmethod
    def ascii_encrypt():
        print ("Input data: "+str(ascii_enc))
        print ("Output data: "+str(encrypt.ascii(ascii_enc)))
    @staticmethod
    def ascii_decrypt():
        print ("Input data: "+str(ascii_enc))
        print ("Output data: "+str(encrypt.ascii(ascii_enc)))

# DOCUMENTATION
#
# 1. How to start working with library
#
# Just fork this module and import it
# > import cryptographic_api
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
# 4. How to start encrypted text
#
# > exec(cryptographic_api.decrypt.binary("01110000011100100110100101101110011101000010000000101000001001110110100001100101011011000110110001101111001000000111011101101111011100100110110001100100001000010010011100101001")) # print ("hello world!")
# hello world!
#
# This error can be displayed if you entered wrong value (in the example is symbols from alphabet)
#
# TODO:
#
# First layer (necessary)
# 1. Add advanced hash algorithms (like as AES/MD5/DES and etc) - (IMPOSSIBLE)
# 2. Fix some "awful" code moments + (Fixed)
# 3. Rewrite our code from scratch for code beautifality - (cuz I am a very lazy ass :( )
# 4. Add cipher sections for ciphers like rot13/reverse and binary/static_binary +- (After this code will be trashed, btw I try do it anyway :) )
# 5. Add some new encryption/cipher algorithms + (Added: random case, ascii)
#
# Second layer (not necessary however must be added)
#
# 1. Write simple and advanced client for testing our library
# 2. Add for developers exception handler (not in program, only template)
# 3. Add cipher recognition (Idk why I must add it, maybe it will be useful for devs)
#
# Third layer (useless)
#
# 1. Add locales (languages) on exceptions and add auto-detect system locale for putting lang in exceptions
# 2. Do autodownloader (template) for this library (if library missing, autodownloader download it)
# 3. Publish it on PyPI
# 4. Add "execute" section for code executing from encrypted text
# 5. Change encryption algorithms output to one-line code (IDK WHY I SHOULD DO IT :D) + (LMAO, I did it)
