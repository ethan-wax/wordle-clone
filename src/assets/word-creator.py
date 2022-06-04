file = open('/usr/share/dict/words', 'r')
arr = file.readlines()
file.close()

arr = list(
    filter(lambda x: len(x.strip()) == 5, arr)
)

file = open('words.txt', 'w')
for i in range(len(arr)):
    arr[i] = arr[i].strip()
file.write(str(arr))
file.close()