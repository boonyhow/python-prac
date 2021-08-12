list = []

def isPalindrome(n):
    reversed = int(str(n)[::-1])
    if reversed == n:
        list.append(n)

def isPrime(n):
    rangeOfNumbers = [True for i in range(n+1)]
    rangeOfNumbers[0] = False
    rangeOfNumbers[1] = False
    x = 2
    while x * x <= n:
        if rangeOfNumbers[x] == True:
            for i in range(x * 2, n + 1, x):
                rangeOfNumbers[i] = False
        x += 1
    for i in range(n+1):
        if rangeOfNumbers[i] == True:
            isPalindrome(i)

isPrime(100000)
print(list)