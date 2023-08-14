from cs50 import get_string
import sys
if len(sys.argv) !=2:
    print("Usage: ./vigenere keyword ")
    sys.exit(1)

key = sys.argv[1].upper()
if not key.isalpha():
    print("Usage: ./vigenere keyword ")
    sys.exit(1)

print(key)

text = get_string("plaintext: ")
print("ciphertext: ", end="")
x = len(key)
a=-1
for harf in text:
    a= a+1
    if not harf.isalpha():
        print(harf,end="")
        a =a-1
        continue

    minus=0
    if harf.isupper():
        minus = 65
    else:
        minus = 97
    sayi= ord(key[a % x])-65
    ch = ord(harf) - minus
    new_harf = (ch+sayi)%26

    print(chr(new_harf + minus),end="")
print()