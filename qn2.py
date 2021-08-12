def isPalindrome(n):
    if type(n) != int:
        return False
    reversed = int(str(n)[::-1])
    if reversed == n:
        return True

def isPrime(n):
    if n > 2:
        for i in range(2, n):
            if (n % i == 0):
                return None
        return n
    else:
        return None 

def digitRemover(n):
    length = len(str(n))
    if length > 1:
        for i in range(length):
            arrayed = [j for j in str(n)]
            arrayed.pop(i)
            if isPalindrome(isPrime(int(''.join(arrayed)))) == True:
                return True
    return False

n = int(input("Lower Bound: "))
m = int(input("Upper Bound: "))

for i in range(n, m):
    if digitRemover(i) == True:
        print(i)

