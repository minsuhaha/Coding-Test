import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def check(t_str):
    if len(s) == len(t_str):
        if s == t_str:
            print(1)
            sys.exit()

    if len(s) > len(t_str):
        return 
    
    # t 문자열 맨 뒤가 A일 경우 제거 
    if t_str[-1] == 'A':
        check(t_str[:-1])

    if t_str[0] == 'B':
        check(t_str[1:][::-1])

check(t)
print(0)
