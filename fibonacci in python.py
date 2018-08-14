#Fibonacci numbers in python
def fib(n):
    a, b = 0, 1
    while b<n:
        print(b, end=' ')
        print()

    def fib2(n):
        result=[]
        a,b=0,1
        while b<n:
            result.append(b)
            a,b=b,a+b
            return result


def fibo():
    print("Fibonacci series is: ",fib[100])
