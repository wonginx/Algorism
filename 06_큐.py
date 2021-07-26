n = int(input('n >>'))
list_i = []

for _ in range(n):
    s = input()
    if s[:4] == "push":
        s,i = s.split()
        i = int(i)
        list_i.append(i)

    elif s == 'front':
        print(list_i[0])
    
    elif s == 'back':
        print(list_i[-1])

    elif s == 'size':
        print(len(list_i))

    elif s == 'empty':
        if len(list_i) > 0:
            print('0')
        else:
            print('1')
    
    elif s == 'pop':
        if len(list_i) > 0:
            print(list_i[0])
            del list_i[0]
        else:
            print('-1')

    
