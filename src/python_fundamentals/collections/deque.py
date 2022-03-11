from collections import deque

if __name__ == "__main__":
    deque = deque()
    deque.append("Jorge")
    deque.append("Camila")
    deque.appendleft("Mario")
    print(deque)
    deque.appendleft("Rafael")
    deque.pop()
    deque.appendleft("Manuel")
    print(deque)
    deque.popleft()
    print(deque)
    