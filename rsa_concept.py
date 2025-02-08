from Crypto.Util.number import *

e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083
p = 416064700201658306196320137931  # you can get the factor number of n fro this web site 'Sage math cell'.
q = 590872612825179551336102196593

phi_n = (p - 1) * (q - 1)

d = pow(e, -1, phi_n)

m = pow(c, d, n)

plaintext = long_to_bytes(m)

print("Decrypted bytes:", plaintext)
