# CryptoChaos
Simple encryption/decryption algorithms based on chaotic maps.

Try
```
pip install cryptochaos
```
Then, import by
```
from cryptochaos import logistic
```
To encrypt, try
```
encrypted_text = logistic.logistic_encrypt(plain_text, r)
```
where plain_text is some string, and r is a float such that 3.6 < r < 4.0.

To decrypt, try
```
decrypted_text = logistic.logistic_decrypt(encrypted_text, r)
```
