def hansu(n):
    count = 0
    for i in range(1, n+1):
        n_list = list(map(int, str(i))) # 숫자를 자릿수대로 분리
        if i < 100:
            count+=1
        elif (n_list[0] - n_list[1]) == (n_list[1] - n_list[2]):
            count+=1
    return count   
        
num = int(input())
print(hansu(num))
