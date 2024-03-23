n = 10  
fibo = [0, 1]  

while len(fibo) < n:
    next_num = fibo[-1] + fib_series[-2]  
    fibo.append(next_num) 

print("Fibonacci Series up to", n, "terms:", fibo)
