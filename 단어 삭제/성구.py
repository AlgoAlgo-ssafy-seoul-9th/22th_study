import sys
input = sys.stdin.readline



string = list(input().strip())
delete = input().strip()

i = 0
while i < len(string):
    if string[i] == delete[0]:
        tmp = string[i:]
        for j in range(1, len(delete)):
            if tmp[j] != delete[j]:
                i += 1
                break
        else:
            string = string[:i]+string[i+len(delete):]
            i = max(0, i -len(delete)-1)
    else:
        i += 1
print("".join(string))

'''
import sys
input = sys.stdin.readline


s = input().strip()
p = input().strip()

while p in s:
    s = s.replace(p, "")
print(s)
'''