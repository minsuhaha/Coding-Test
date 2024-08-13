import sys
input = sys.stdin.readline

n = int(input())
deque = []
for _ in range(n):
    command = list(input().rstrip().split())
    if len(command) == 2:
        if command[0] == 'push_back':
            deque.append(command[1])
        elif command[0] == 'push_front':
            deque.insert(0, command[1])
    else:
        if command[0] == 'pop_front':
            print(deque.pop(0) if deque else -1)
        elif command[0] == 'pop_back':
            print(deque.pop() if deque else -1)
        elif command[0] == 'size':
            print(len(deque))
        elif command[0] == 'empty':
            print(0 if deque else 1)
        elif command[0] == 'front':
            print(deque[0] if deque else -1)
        elif command[0] == 'back':
            print(deque[-1] if deque else -1)