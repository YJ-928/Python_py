def fibonacciGenerator(n):
    if n <= 1:
        return n
    return fibonacciGenerator(n - 1) + fibonacciGenerator(n - 2)

print("Welcome to King-YJ's Fibonacci Sequence Generator.")
n = int(input("Enter a number till which you want to generate fibonacci series:\t"))
print("Your Fibonacci Sequence is as follows:")

fibonacciSeries = []

for i in range(0,n):
    temp = fibonacciGenerator(i)
    print(temp)
    fibonacciSeries.append(temp)

print("Your Fibonacci Series in a Array/List form:")
print(fibonacciSeries)