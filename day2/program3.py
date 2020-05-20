n=int(input())
for i in range(n):
    print(" " * i + "*" + " " * 2*(n-1-i) + "*")
for i in range(n):
    print(" " * (n-1-i) + "*" + " " * 2*i + "*")
