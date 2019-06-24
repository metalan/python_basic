def queues():
    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")  # llega Terry
    queue.append("Graham")  # llega Graham
    queue.popleft()  # el primero en llegar ahora se va