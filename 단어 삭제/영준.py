txt = input()
pat = input()
M = len(pat)

st = [0] * len(txt)
top = -1
cnt = 0
for x in txt:
    top += 1
    st[top] = x
    cnt = 0
    while top>=cnt and st[top-cnt] == pat[M-1-cnt]:
        cnt += 1
    if cnt == M:
        top -= M

print(''.join(st[:top+1]))
