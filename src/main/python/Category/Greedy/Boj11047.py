import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

answer = 0
for i in lst:
    if (K // i == 0):
        continue
        # lst.remove(lst[0])
    else:
        a = (K // i)
        answer += a
        K %= i
print(answer)


# 풀이2
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

answer = 0
while (len(lst) != 0):
    if (K // lst[0] == 0):
        lst.remove(lst[0])
    else:
        a = (K // lst[0])
        answer += a
        K %= lst[0]

print(answer)