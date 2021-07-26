# 숫자 N 입력받기
N = int(input('N : '))
# N으로 나누웠을때 나머지와 몫이 같은
# 모든 자연수의 합 구하기
# 2 = 3
# 3 = 12
# 4 = 30
result = 0
for i in range(1,N):
    result += (i + (N*i))
print('정답 : ' , result)
