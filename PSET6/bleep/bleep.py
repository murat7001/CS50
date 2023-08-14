from cs50 import get_string
from sys import argv
import sys


sys.argv
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage:python bleep.py dictionary")
    exit(1)

else:
    banned = sys.argv[1]


words = set()
with open(banned, "r") as file:
    for line in file:
        words.add(line.rstrip("\n"))

word = get_string("what words?")
temp_str = word.split(' ')

for i in range(0, len(temp_str)):
    # print(i)
    # print(temp_str[i] in words)
    a = temp_str[i].lower()
    # print(temp_str[i])
    if (a in words):
        print("*" * len(temp_str[i]), "", end="")
    else:
        print(temp_str[i], "", end="")


print()


# https://yuanann.pixnet.net/blog/post/23211833
# https://www.youtube.com/watch?v=RAPPAA0E46U
# https://www.youtube.com/watch?v=C4OkV6DrVRs
# https://lettice0913.pixnet.net/blog/post/25892480