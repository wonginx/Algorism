# 약수 구하기

# 입력받은 숫자 N의 모든 약수를 출력하시오.

# 입력예제                  출력예제
# 100              1 2 4 5 10 20 25 50 100

N = int(input( 'N >>'))
result = []

for i in range(1,N+1):
    if N%i == 0:
        result.append(i)
print(result)        