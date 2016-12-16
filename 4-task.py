import binascii
import CompactFIPS202 as keccak

s = "HELLO WorlD"
hash = keccak.SHA3_512(bytearray(s.encode('utf-8')))
hex = binascii.hexlify(hash)
print hex
