import random

array_2d = [[round(random.random()) for _ in range(10)] for i in range(10)]

for rows in range(5):
    for cols in range(5):
        print("[", array_2d[rows][cols], " ", array_2d[rows][cols+1], "]")
        print("[", array_2d[rows+1][cols], " ", array_2d[rows+1][cols+1], "]")
        print("\r\n\r\n")