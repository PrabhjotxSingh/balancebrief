text_file = open("api/sources/test.txt", "r+")
ret = []
for x in range(3):
    temp = text_file.readline().replace("\n", '')
    ret.append(temp)
text_file.readline()
text =  text_file.read().rstrip()


print(ret)
print(text)