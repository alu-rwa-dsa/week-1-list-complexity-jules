import time

first_point = time.time()
n = 0
while True:
    print("Hello")
    n = n + 1
    if n == 10000:
        break

last_point = time.time()
time_n = last_point- first_point
print("Time taken is: ")
print(time_n)