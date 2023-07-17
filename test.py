performance = {"1": 1,"13": 4,"9": 2,"3": -1,"69": 5}
surviving = []
while len(surviving) < 3:
    a = max(performance, key=performance.get)
    surviving.append(a)
    performance.pop(a)
print(surviving)
