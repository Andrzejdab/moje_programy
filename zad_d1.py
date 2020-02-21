"""
Program dekodujący kod znaleziony w Saragossie.
"""
class Kod:

    def __init__(self,kod):
        self.kod = kod

    def change_binary_hex(self):
        tablica_dec = []
        tablica_hex = []
        tablica_bin = self.kod.split(" ")

        for i in tablica_bin:
            tablica_dec.append(int(i, 2))

        for i in tablica_dec:
            h = hex(i)
            if len(h) == 3:
                h = "0" + h[2:]
            else:
                h = h[2:]
            tablica_hex.append(h)

        kod_h = ''.join(tablica_hex)
        return kod_h.encode("utf-8")

kod_b = "11111 10111 00111 00110 01110 01111 00100 11001 01010 11000 10011 01100 00100 01101 11000 11101 00100 01011 00111 11100 10110 00101 00100 11000 11110 00001 01010 00100 10000 10100 00001 00100 10010 00011 10001 10101 00100 01001 11000 11010 00100 00011 10010 10000 00001 01010 01100 00011 10000 00110 11110 00001 00100 00111 01110 10001 01110 00110 00001 00100 00101 00110 00001 00100 10110 10101 10000 10100 11000 01100 00011 00100 01111 10000 11000 00100 10001 01010 11000 11001 00110 10010 00100 01100 00110 00001 01110 10100 00100 10001 00011 10110 10101 10000 00011 00100 11000 00100 01100 00011 11010 01010 11000 01001 00001"
kod = Kod(kod_b)
code = kod.change_binary_hex()


from io import BytesIO
from baudot import decode_to_str, codecs, handlers

with BytesIO(code) as code_stream:
    reader = handlers.HexBytesReader(code_stream)
    print(decode_to_str(reader, codecs.ITA2_US))





