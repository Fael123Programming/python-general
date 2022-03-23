from collections import deque

if __name__ == "__main__":
    # Deque is the best option to implement a queue.
    queue = deque()
    queue.append("str1")
    queue.append("str2")
    queue.append("str3")
    print(queue)
    queue.popleft()
    queue.popleft()
    print(queue)