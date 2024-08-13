import sys
input = sys.stdin.readline


class Deque:
    def __init__(self):
        self.deque = []
    
    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        return self.deque.pop(0) if self.deque else -1

    def pop_back(self):
        return self.deque.pop() if self.deque else -1

    def size(self):
        return len(self.deque)

    def empty(self):
        return 1 if len(self.deque) == 0 else 0

    def front(self):
        return self.deque[0] if self.deque else -1

    def back(self):
        return self.deque[-1] if self.deque else -1
    
n = int(input())
deque = Deque()

for _ in range(n):
    command = list(input().rstrip().split())
    if len(command) == 2:
        if command[0] == 'push_back':
            deque.push_back(command[1])
        elif command[0] == 'push_front':
            deque.push_front(command[1])
    else:
        if command[0] == 'pop_front':
            print(deque.pop_front())
        elif command[0] == 'pop_back':
            print(deque.pop_back())
        elif command[0] == 'size':
            print(deque.size())
        elif command[0] == 'empty':
            print(deque.empty())
        elif command[0] == 'front':
            print(deque.front())
        elif command[0] == 'back':
            print(deque.back())
