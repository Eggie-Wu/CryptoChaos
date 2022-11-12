import random
from unittest import TestCase
from src.cryptochaos import logistic

class TestLogistics(TestCase):
    def test_logistics(self):
        plain_text="abcdefghijklmn"
        for i in range(10):
            r=random.uniform(3.6,4.0)
            cipher_text=logistic.logistic_encrypt(plain_text,r)
            self.assertEqual(plain_text,logistic.logistic_decrypt(cipher_text,r))