# 🔐 Cryptographic_API

**Version**: v1.2  
**Developer**: [@Andreyoss on Telegram](https://t.me/Andreyoss)

A simple Python-based library that provides a wide variety of encoding and decoding (encryption/decryption) algorithms for basic string and integer transformations.

---

## 🚀 Features

- ROT13 cipher
- String reversal
- Static binary (int ↔ binary)
- Binary encoding (str ↔ bin)
- Random case converter
- ASCII encoding/decoding
- Static octal & hex conversions
- Atbash cipher
- Caesar cipher (basic & unstable)
- Normal hex view (`xxd`-style)

Each feature is available for both encryption and decryption where applicable.

---

## 🛠 Requirements

- Python 3.x

No external dependencies required.

---

## 📦 Usage

Import or run the file directly to access the methods via:

```python
from cryptographic_api import encrypt, decrypt
```

### Example

```python
encrypt.rot13("hello")         # Output: 'uryyb'
decrypt.rot13("uryyb")         # Output: 'hello'

encrypt.static_binary(123)     # Output: '1111011'
decrypt.static_binary('1111011') # Output: 123

encrypt.reverse("ABC")         # Output: 'CBA'
decrypt.reverse("CBA")         # Output: 'ABC'

encrypt.ascii("hi")            # Output: '104 105'
decrypt.ascii("104 105")       # Output: 'hi'
```

---

## 🧪 Built-in Tests

Run automated encoding/decoding tests:

```python
tests.static_binary_encrypt()
tests.static_binary_decrypt()
tests.binary_encrypt()
tests.binary_decrypt()
tests.reverse_encrypt()
tests.reverse_decrypt()
tests.rot13_encrypt()
tests.rot13_decrypt()
tests.random_case_encrypt()
tests.random_case_decrypt()
tests.ascii_encrypt()
tests.ascii_decrypt()
tests.static_hex_encrypt()
tests.static_hex_decrypt()
tests.static_octal_encrypt()
tests.static_octal_decrypt()
tests.normal_hex_encrypt()
tests.normal_hex_decrypt()
```

Each test prints input/output data for verification.

---

## ⚠️ Warnings

- **Caesar cipher** is unstable and should not be used in production.
- Random case transformation is non-reversible by design.
- Some converters only work with integer inputs; exceptions are raised otherwise.

---

## Note

No third-party libraries were used in the code; everything was done using algorithms. If there are any problems, write to issues

## 📄 License

This project is licensed under the MIT License

---
