# 2. 휴식을 위하여

# 날씨 좋은 휴일,
# 공사 현장은 공원에서 오직 한군데이고, 그 위치를 (a, b)라고 합니다. 공사현장에서
# R만큼의 거리 미만은 소음이 크기 떄문에 독서에 적합하지 않습니다.

# 또한 공원에는 휴식과 독서에 적합한 그늘이 N개 존재합니다. 각각의 그늘 위치는 (x_i, y_i)
# 입니다.(i번째)

# 이상의 정보에서 각 그늘이 독서에 적합한지
# (공사 현장에서 R 이상 떨어진 그늘인지) 판별

# a b R #공사 현장의 x 좌표 (a), y 좌표 (b) , 공사장 소음거리 R

# 입력예제
# 20 10 10  / N = 3 / 25 10 = noisy / 20 15 = noisy / 70 70 = silent
# 50 50 100  / N = 4 / 0 0 = noisy / 0 100 = noisy / 100 0 = noisy

a = int(input('a 값 >> '))
b = int(input('b 값 >> '))
R = int(input('R 값 >> '))
N = int(input('N 값 >> '))

# (a,b) 에서 거리 R 값 미만 = noisy / R 값 초과 = silent
# x, y 가 공사 현장에서 R 이상 떨어져있다는 조건
for i in range(N):
    # x = int(input('그늘 x 값 >> '))
    # y = int(input('그늘 y 값 >> '))
    x, y = input().split()
    x = int(x)
    y = int(y)

    silent =  ((x-a)**2 + (y-b)**2 >= R**2)
    if silent:
        print('silent')
    else:
        print('noisy')
