#
import binascii
import CompactFIPS202 as keccak

def get_hash(string):
    hash = keccak.SHA3_512(bytearray(string.encode('utf-8')))
    hex = binascii.hexlify(hash)
    return hex

D = {}
user1 = 'Josef Allen'
user2 = 'Sergiy Prytyla'
user3 = 'Chegevara'

D[get_hash(user1)] = user1
D[get_hash(user2)] = user2
D[get_hash(user3)] = user3

for k,v in D.items():
    print k,':',v
