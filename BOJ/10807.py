count = int(input())
num = list(map(int, input().split()))
find = int(input())
counting = 0

for i in range(count):
    if find == num[i]:
        counting+=1
        
print(f'{counting}')
