def fibonnacci(n):
    if n==0 or n==1:
         return 1
    return fibonnacci(n-1)+fibonnacci(n-2)

n=int(input('Entero: '))
print(fibonnacci(n))