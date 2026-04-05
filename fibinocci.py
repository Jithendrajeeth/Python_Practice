n = int(input("Enter n: "))

a, b = 0, 1

for _ in range(n):
    a, b = b, a + b

print("Nth Fibonacci:", a)