#1 part
import hashlib
for n in range(20_000_000):
    s = "bgvyzdsv" + str(n)
    res = hashlib.md5(s.encode())
    if res.hexdigest().startswith("00000"):
        print(res.hexdigest(), n)
        break

#2 part
for n in range(20_000_000):
    s = "bgvyzdsv" + str(n)
    res = hashlib.md5(s.encode())
    if res.hexdigest().startswith("000000"):
        print(res.hexdigest(), n)
        break