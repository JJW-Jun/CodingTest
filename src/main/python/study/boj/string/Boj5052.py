def solution(phone_number):
    phone_number.sort()
    for i in range(len(phone_number)):
        if (phone_number[i+1].startswith(phone_number[i])):
            return False
    return True


ans = []
for i in range(int(input().rstrip())):
    lst = [input() for _ in range(int(input()))]
    if (solution(lst)):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)