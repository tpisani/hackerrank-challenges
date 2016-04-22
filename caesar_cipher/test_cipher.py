
from unittest import TestCase

from . import cipher


class CaesarCipherTests(TestCase):

    def test_encrypt_1(self):
        S = cipher.encrypt("middle-Outz", 2)
        self.assertEqual("okffng-Qwvb", S)

    def test_encrypt_2(self):
        S = cipher.encrypt("abc-xyz", 3)
        self.assertEqual("def-abc", S)

    def test_encrypt_3(self):
        S = cipher.encrypt("www.abc.xy", 87)
        self.assertEqual("fff.jkl.gh", S)

    def test_encrypt_4(self):
        S = cipher.encrypt("crack-me", 101)
        self.assertEqual("zoxzh-jb", S)
