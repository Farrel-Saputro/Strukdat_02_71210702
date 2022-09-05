import timeit

def iterak_fibo(n):
    a,b = 0,1
    for i in range (n):
        a,b = b, a+b
    return a

for i in range(1, 101):
    #iteraktif fibonacci
    start = timeit.default_timer()
    end = timeit.default_timer()
    print(f"Fibonacci Data-{i} Iteraktif adalah {iterak_fibo(i)} : {end-start} detik")

print()

def rekur_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rekur_fibo(n-1) + rekur_fibo(n-2)

for i in range(1, 101):
    #rekursif fibonacci
    start = timeit.default_timer()
    end = timeit.default_timer()
    print(f"Fibonacci Data-{i} Rekursif adalah {rekur_fibo(i)} : {end-start} detik")