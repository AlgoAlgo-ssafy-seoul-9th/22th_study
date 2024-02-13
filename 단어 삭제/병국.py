word = input()
delete = input()
len_delete = len(delete)
# print(word)

# while True:
#     if delete in word:
answer = ''
for i in range(len(word)):
    answer += word[i]
    if delete in answer:
        i -= len_delete
        answer = answer[:len(answer)-len_delete]
        # print(answer)
print(answer)
    # print(word[i])