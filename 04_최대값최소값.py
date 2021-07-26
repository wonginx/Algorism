# 최대값, 최소값 구하기

# 입력받은 정수 값들 중 최대값과 최소값 순서대로 출력하시오.
# 단, 파이썬 내장 함수 max, min 및 기타 numpy, pandas 등의 라이브러리는 쓸 수 없다

# 입력예제                  출력예제
# 1 2 100 3 30              100 1


n = [int(x) for x in input('n >>').split()]
# n = list(map(int, input().split()))
n.sort()
print('최소값 : ' ,n[0])
print('최대값 : ' ,n[-1])

