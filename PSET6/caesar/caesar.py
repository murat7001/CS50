from cs50 import get_string
import sys
if len(sys.argv) !=2:
    print("Usage: pyhton caesar.py k ")
    sys.exit(1)
sayi = int(sys.argv[1])

text = get_string("plaintext: ")
print("ciphertext: ", end="")
for harf in text:
    if not harf.isalpha():
        print(harf,end="")
        continue

    minus=0
    if harf.isupper():
        minus = 65
    else:
        minus = 97
    ch = ord(harf) - minus
    new_harf = (ch+sayi)%26
    print(chr(new_harf + minus),end="")
print()