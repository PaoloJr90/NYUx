n = int(input("Please enter a positive integer greater than 1:"))

#define the recursion function (n-1 is with respect to position not arithmetic)
def recur_fibo(n):
        if n <= 1:
                return n
        else:
                return(recur_fibo(n-1) + recur_fibo(n-2))

#execute recursion function (recur_fibo)
for i in range(1, n+1):                                                
        print(recur_fibo(i))
