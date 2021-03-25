x = 4
print("nilai x =", x, " , binary", format(x,'08b'))

y = 11
print("nilai y =", y, ", binary", format(y,'08b'))

a = x | y
print("nilai a =", a, ", binary", format(a,'08b'))

b = x >> y
print("nilai b =", b, " , binary", format(b,'08b'))

c = x ^ y
print("nilai c =", c, ", binary", format(c,'08b'))

d = ~ x
print("nilai d =", d, ", binary", format(d,'08b'))

e = y & x
print("nilai e =", e, " , binary", format(e,'08b'))