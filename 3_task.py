from ec import *

ec = EC(1, 18, 19)
g, _ = ec.at(7)
print(g)


dh = DiffieHellman(ec, g)
print(ec.order(g))
#1 Acice
apriv = 11
apub = dh.gen(apriv)
print(apub)
#2 Bob
bpriv = 3
bpub = dh.gen(bpriv)
print(bpub)
#3 Carol
cpriv = 7
cpub = dh.gen(cpriv)
print(cpub)
#4 Dave
dpriv = 5
dpub = dh.gen(dpriv)
print(dpub)

# Alice -> Bob -> Carol ->Dave
bob_temp = dh.secret(bpriv, apub)  # bob use Alice public key (a) and send to carol (ab)
carol_temp = dh.secret(cpriv, bob_temp) #Alive use public (ab) , calcucate (abc) and send to dave
dave_temp = dh.secret(dpriv, carol_temp) #dave use (abc) and calcucate (abcd)
print("====================")
print(dave_temp)

#  Bob -> Carol ->Dave -> Alice
carol_temp = dh.secret(cpriv, bpub)  # Carol use Bob public key (b) and send to Dave(bc)
dave_temp = dh.secret(dpriv, carol_temp)  # Dave use public (bc) , calcucate (bcd) and send to Alice
alice_temp = dh.secret(apriv, dave_temp)  # Alice use (bcd) and calcucate (abcd)
print("====================")
print(alice_temp)

#  Carol ->Dave -> Alice ->Bob
dave_temp = dh.secret(dpriv, cpub)  # Dave use public (c) , calcucate (cd) and send to Alice
alice_temp = dh.secret(apriv, dave_temp)  # Alice use (cd) and calcucate (acd)
bob_temp = dh.secret(bpriv, alice_temp)  # Bob use acd public key (acd) and calculate (abcd)
print("====================")
print(bob_temp)

#  Dave -> Alice ->Bob-> Carol
alice_temp = dh.secret(apriv, dpub)  # Alice use (d) and calcucate (ad) , send to Bob
bob_temp = dh.secret(bpriv, alice_temp)  # Bob use (ad) public key  and calculate (abd), send to Carol
carol_temp = dh.secret(cpriv, bob_temp)  # Carol use public (abd) ,and calcucate (abcd)
print("====================")
print(carol_temp)
