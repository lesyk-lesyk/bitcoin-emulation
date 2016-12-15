# Basics of Elliptic Curve Cryptography implementation on Python
import collections


def inv(n, q):
    """div on PN modulo a/b mod q as a * inv(b, q) mod q
    >>> assert n * inv(n, q) % q == 1
    """
    for i in range(q):
        if (n * i) % q == 1:
            return i
        pass
    assert False, "unreached"
    pass


def sqrt(n, q):
    """sqrt on PN modulo: returns two numbers or exception if not exist
    >>> assert (sqrt(n, q)[0] ** 2) % q == n
    >>> assert (sqrt(n, q)[1] ** 2) % q == n
    """
    assert n < q
    for i in range(1, q):
        if i * i % q == n:
            return (i, q - i)
        pass
    raise Exception("not found")


Coord = collections.namedtuple("Coord", ["x", "y"])


class EC(object):
    """System of Elliptic Curve"""

    def __init__(self, a, b, q):
        """elliptic curve as: (y**2 = x**3 + a * x + b) mod q
        - a, b: params of curve formula
        - q: prime number
        """
        assert 0 < a and a < q and 0 < b and b < q and q > 2
        assert (4 * (a ** 3) + 27 * (b ** 2)) % q != 0
        self.a = a
        self.b = b
        self.q = q
        # just as unique ZERO value representation for "add": (not on curve)
        self.zero = Coord(0, 0)
        pass

    def is_valid(self, p):
        if p == self.zero: return True
        l = (p.y ** 2) % self.q
        r = ((p.x ** 3) + self.a * p.x + self.b) % self.q
        return l == r

    def at(self, x):
        """find points on curve at x
        - x: int < q
        - returns: ((x, y), (x,-y)) or not found exception
        >>> a, ma = ec.at(x)
        >>> assert a.x == ma.x and a.x == x
        >>> assert a.x == ma.x and a.x == x
        >>> assert ec.neg(a) == ma
        >>> assert ec.is_valid(a) and ec.is_valid(ma)
        """
        assert x < self.q
        ysq = (x ** 3 + self.a * x + self.b) % self.q
        y, my = sqrt(ysq, self.q)
        return Coord(x, y), Coord(x, my)

    def neg(self, p):
        """negate p
        >>> assert ec.is_valid(ec.neg(p))
        """
        return Coord(p.x, -p.y % self.q)

    def add(self, p1, p2):
        """<add> of elliptic curve: negate of 3rd cross point of (p1,p2) line
        >>> d = ec.add(a, b)
        >>> assert ec.is_valid(d)
        >>> assert ec.add(d, ec.neg(b)) == a
        >>> assert ec.add(a, ec.neg(a)) == ec.zero
        >>> assert ec.add(a, b) == ec.add(b, a)
        >>> assert ec.add(a, ec.add(b, c)) == ec.add(ec.add(a, b), c)
        """
        if p1 == self.zero: return p2
        if p2 == self.zero: return p1
        if p1.x == p2.x and (p1.y != p2.y or p1.y == 0):
            # p1 + -p1 == 0
            return self.zero
        if p1.x == p2.x:
            # p1 + p1: use tangent line of p1 as (p1,p1) line
            l = (3 * p1.x * p1.x + self.a) * inv(2 * p1.y, self.q) % self.q
            pass
        else:
            l = (p2.y - p1.y) * inv(p2.x - p1.x, self.q) % self.q
            pass
        x = (l * l - p1.x - p2.x) % self.q
        y = (l * (p1.x - x) - p1.y) % self.q
        return Coord(x, y)

    def mul(self, p, n):
        """n times <mul> of elliptic curve
        >>> m = ec.mul(p, n)
        >>> assert ec.is_valid(m)
        >>> assert ec.mul(p, 0) == ec.zero
        """
        r = self.zero
        m2 = p
        # O(log2(n)) add
        while 0 < n:
            if n & 1 == 1:
                r = self.add(r, m2)
                pass
            n, m2 = n >> 1, self.add(m2, m2)
            pass
        # [ref] O(n) add
        # for i in range(n):
        #    r = self.add(r, p)
        #    pass
        return r

    def order(self, g):
        """order of point g
        >>> o = ec.order(g)
        >>> assert ec.is_valid(a) and ec.mul(a, o) == ec.zero
        >>> assert o <= ec.q
        """
        assert self.is_valid(g) and g != self.zero
        for i in range(1, self.q + 1):
            if self.mul(g, i) == self.zero:
                return i
            pass
        raise Exception("Invalid order")

    pass

class DiffieHellman(object):
    """Elliptic Curve Diffie Hellman (Key Agreement)
    - ec: elliptic curve
    - g: a point on ec
    """

    def __init__(self, ec, g):
        self.ec = ec
        self.g = g
        self.n = ec.order(g)
        pass

    def gen(self, priv):
        """generate pub key"""
        assert 0 < priv and priv < self.n
        return self.ec.mul(self.g, priv)

    def secret(self, priv, pub):
        """calc shared secret key for the pair
        - priv: my private key as int
        - pub: partner pub key as a point on ec
        - returns: shared secret as a point on ec
        """
        assert self.ec.is_valid(pub)
        assert self.ec.mul(pub, self.n) == self.ec.zero
        return self.ec.mul(pub, priv)

    pass


if __name__ == "__main__":
    # shared elliptic curve system of examples
    ec = EC(1, 18, 19)
    g, _ = ec.at(7)
    print(g)

    # ECDH usage
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

    pass