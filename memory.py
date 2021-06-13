def eatmemory():
    eating_memory = [x for x in range(10**6)]
    for i in range(10):
       eating_memory.append([x for x in range(10**6)])
       y = 1 # not eating memory
