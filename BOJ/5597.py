## 처음 풀 때
count = 0
student = []
while count!=28:
    s = int(input())
    student.append(s)
    count+=1
    
num = [1,0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,0,0]
for i in range(28):
    num[student[i]] += 1
    
for i in range(31):
    if num[i] == 0:
        print(i)
        
## 다시 풀 때
student = [i for i in range(1, 31)]
for _ in range(28):
    num = int(input())
    student.remove(num)
    
print(min(student))
print(max(student))
