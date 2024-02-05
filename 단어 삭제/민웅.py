import sys
input = sys.stdin.readline


all_word = list(input().strip())

bomb = list(input().strip())
bl = len(bomb)
stack = []

for i in range(len(all_word)):
    stack.append(all_word[i])
    tmp = len(stack)
    if tmp >= bl and stack[-1] == bomb[-1]:
        if stack[tmp-bl:] == bomb:
            stack = stack[:tmp-bl]
    

print(*stack, sep='')