import sys
input = sys.stdin.readline

wordsList = input().strip()
word = input().strip()
l = len(word)   # 2
i = 0

while i + l <= len(wordsList):
    if wordsList[i:i+l] == word:
        wordsList = wordsList[:i] + wordsList[i+l:]
        i = 0
    else:
        i += 1
print(wordsList)