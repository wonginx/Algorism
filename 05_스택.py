n = int(input())
stack = []
push_cnt = 0

for i in range(n):
    s = input()

    if s[:4] == 'push':
        s,num = s.split()
        num = int(num)
    

    if s == 'push':
        stack.append(num)
        push_cnt += 1
    elif s == 'pop':
        try:
            print(stack[push_cnt-1])
            stack.pop(push_cnt-1)
            push_cnt -= 1
        except:
            print("-1")
    elif s == 'size':
        print(push_cnt)
    elif s == 'empty':
        if push_cnt == 0:
            print("1")
        else:
            print("0")
    elif s == 'top':
        try:
            print(stack[push_cnt-1])
        except:
            print("-1")