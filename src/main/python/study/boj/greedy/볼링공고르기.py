n, m = map(int, input().split())
data = list(map(int, input().split()))
count =0
for i in range(len(data)) :
    for j in range(i+1, len(data)) :
        if data[i] != data[j] :
            count +=1
print(count)



array = [0] * 11

for x in data:
    array[x] += 1

cnt = 0
for i in range(1, m + 1):
    n -= array[i]
    cnt += array[i] * n

print(cnt)