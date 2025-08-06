# Developer - https://t.me/Andreyoss
# Version v1.2

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
ascii_dec = "104 105"
hex_enc = "777"
hex_dec = "3019"
static_octal_enc = "123"
static_octal_dec = "173"

def tests_io(t_input, t_output, pr):
    if pr.lower() == "p":
        print("Input data:", t_input)
        print("Output data:", t_output)

    elif pr.lower() == "r":
        return f"Input data: {t_input}\nOutput data: {t_output}"

    else:
        print("Wrong end value! Please enter P(print)/R(return)")

class encrypt:
    @staticmethod
    def rot13(txt):
        output = "".join([rot13_cipher[(rot13_cipher.find(c)+13)%26] for c in txt.lower()])
        return output

    @staticmethod
    def reverse(txt):
        output = txt[::-1]
        return output

    @staticmethod
    def static_binary(txt):
        try:
           output = bin(txt)[2:]
        except Exception:
           raise TypeError("Integer required, not string!")
        return output

    @staticmethod
    def binary(txt):
        output = ''.join(format(ord(i), '08b') for i in txt)
        return output

    @staticmethod
    def random_case(txt):
        output = ''.join(choice((str.upper, str.lower))(c) for c in txt)
        return output

    @staticmethod
    def ascii(txt):
        output = ' '.join(str(ord(x)) for x in txt)
        return output

    @staticmethod
    def static_octal(txt):
        try:
            int(txt)
        except Exception:
            raise TypeError("Integer required, not string!")
        else:
            try:
                output = ''.join(oct(int(txt)).lstrip("0o").rstrip("L"))
            except Exception:
                raise TypeError("Integer required, not string!")
        return output

    @staticmethod
    def static_hex(txt):
        try:
            int(txt)
        except Exception:
            raise TypeError("Integer required, not string!")
        else:
            try:
                output = ''.join(hex(int(txt)).lstrip("0x").rstrip("L"))
            except Exception:
                raise TypeError("Integer required, not string!")
        return output

    @staticmethod
    def atbash(txt):
        alphabet = ord('z') + ord('a')
        output = ''.join([chr(alphabet - ord(s)) for s in txt])
        return output

    @staticmethod
    def normal_hex(txt):
        output = ' '.join("{:02x}".format(ord(c)) for c in txt)
        return output

    @staticmethod
    # Unstable cipher!
    def caesar(txt):
        output = ""
        txt = str(txt)
        for i in range(len(txt)):
            char = txt[i]
            if (char.isupper()):
                output += chr((ord(char) + 25-65) % 26 + 65)
            else:
                output += chr((ord(char) + 25 - 97) % 26 + 97)
        return output
    # Unstable cipher!

class decrypt:
    @staticmethod
    def reverse(txt):
        output = txt[::-1]
        return output

    @staticmethod
    def rot13(txt):
        output = "".join([rot13_cipher[(rot13_cipher.find(c)+13)%26] for c in txt.lower()])
        return output

    @staticmethod
    def static_binary(txt):
        try:
           output = int(str(txt), 2)
        except Exception:
           raise ValueError("Integer must be only 0 or 1!")
        return output

    @staticmethod
    def binary(txt):
        output = ''.join(chr(int(str(txt)[i*8:i*8+8],2)) for i in range(len(str(txt))//8))
        return output

    @staticmethod
    def random_case(txt):
        output = ''.join(choice((str.upper, str.lower))(c) for c in txt)
        return output

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

    @staticmethod
    def normal_hex(txt):
        bits = ""
        txt = txt.replace(' ', '')
        for x in range(0, len(txt), 2):
            bits += chr(int(txt[x:x+2], 16))
        return bits

    @staticmethod
    def static_hex(txt):
        output = int(txt, base=16)
        return output

    @staticmethod
    def static_octal(txt):
        output = int(''.join(str(txt)), 8)
        return output

    @staticmethod
    def atbash(txt):
        alphabet = ord('z') + ord('a')
        output = ''.join([chr(alphabet - ord(s)) for s in txt])
        return output

    @staticmethod
    def caesar(txt, shift):
        output = [ord(x)    if x != " " else -1  for x in txt]
        output = [o - shift    if o != -1  else -1  for o in output]
        output = ''.join(chr(i) if i != -1 else ' ' for i in output)
        return output

class tests:
    @staticmethod
    def static_binary_encrypt():
        tests_io(static_binary_enc, encrypt.static_binary(static_binary_enc), 'p')

    @staticmethod
    def static_binary_decrypt():
        tests_io(static_binary_dec, decrypt.static_binary(static_binary_dec), 'p')
    
    @staticmethod
    def binary_encrypt():
        tests_io(binary_enc, encrypt.binary(binary_enc), 'p')
    
    @staticmethod
    def binary_decrypt():
        tests_io(binary_dec, decrypt.binary(binary_dec), 'p')
    
    @staticmethod
    def reverse_encrypt():
        tests_io(reverse_enc, encrypt.reverse(reverse_enc), 'p')
    
    @staticmethod
    def reverse_decrypt():
        tests_io(reverse_dec, decrypt.reverse(reverse_dec), 'p')
    
    @staticmethod
    def rot13_encrypt():
        tests_io(rot13_enc, encrypt.rot13(rot13_enc), 'p')
    
    @staticmethod
    def rot13_decrypt():
        tests_io(rot13_dec, decrypt.rot13(rot13_dec), 'p')
    
    @staticmethod
    def random_case_encrypt():
        tests_io(random_case_enc, encrypt.random_case(random_case_enc), 'p')
    
    @staticmethod
    def random_case_decrypt():
        tests_io(random_case_dec, decrypt.random_case(random_case_dec), 'p')
    
    @staticmethod
    def ascii_encrypt():
        tests_io(ascii_enc, encrypt.ascii(ascii_enc), 'p')
    
    @staticmethod
    def ascii_decrypt():
        tests_io(ascii_dec, decrypt.ascii(ascii_dec), 'p')
    
    @staticmethod
    def static_hex_encrypt():
        tests_io(hex_enc, encrypt.static_hex(hex_enc), 'p')
    
    @staticmethod
    def static_hex_decrypt():
        tests_io(hex_dec, decrypt.static_hex(hex_dec), 'p')
    
    @staticmethod
    def static_octal_encrypt():
        tests_io(static_octal_enc, encrypt.static_octal(static_octal_enc), 'p')
    
    @staticmethod
    def static_octal_decrypt():
        tests_io(static_octal_dec, decrypt.static_octal(static_octal_dec), 'p')
    
    @staticmethod
    def normal_hex_encrypt():
        tests_io(hex_enc, encrypt.normal_hex(hex_enc), 'p')
    
    @staticmethod
    def normal_hex_decrypt():
        tests_io(hex_dec, decrypt.normal_hex(hex_dec), 'p')
