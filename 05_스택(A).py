# stack = [] # global 숫자,문자 값은 전역변수화 시켜야 된다 / 리스트는 그냥 사용은 가능
def run_with_cmd_stack(stack, stack_size, cmd_list):
    cmd_type = cmd_list[0]
    
    if cmd_type == "push":
        _, num =  cmd_list
        # num = int(cmd_list[1])
        # num = cmd_list[-1]
        stack.append(int(num))
        stack_size += 1
    elif cmd_type == "pop":
        if stack_size > 0 :
            print(stack.pop())
        else:
            print(-1)

    elif cmd_type == "size":
        print(stack_size)

    elif cmd_type == "empty":
        if len(stack) > 0:
            print(0)
        else :
            print(1)
        
    elif cmd_type == "top":
        if len((stack)) > 0:
            print(stack[-1])
        else:
            print(-1)

        
    return stack

n = int(input())

stack = []

for _ in range(n):

    # "push 2".split(" ") # > ["push", "2"]
    # "size".split(" ") # > ["size"]

    cmd_list = input().split(" ")
    stack = run_with_cmd_stack(stack, cmd_list)

    print(stack)