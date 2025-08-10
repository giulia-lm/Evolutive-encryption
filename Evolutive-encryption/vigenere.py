class Vigenere:
    def __init__(self, plain_text, key):
        self.plain_text = plain_text
        self.key = key
        self.ciphertext = self.encrypt()

    def encrypt(self):
        ciphertext = ''

        ascii_text = [ord(letter) for letter in self.plain_text]
        ascii_key = [ord(letter) for letter in self.key]

        for i in range(len(ascii_text)):
          value = (ascii_text[i]+ ascii_key[i % len(ascii_key)]) % 26
          ciphertext += chr(value + 65)
        return ciphertext

    def dencrypt(self):
        plain_text = ''

        ascii_ciphertext = [ord(letter) for letter in self.ciphertext]
        ascii_key = [ord(letter) for letter in self.key]

        for i in range(len(ascii_ciphertext)):
          value = (ascii_ciphertext[i] - ascii_key[i % len(ascii_key)]) % 26
          plain_text += chr(value + 65)

        self.plain_text = plain_text