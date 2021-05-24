# Oscar Yu
# May 24th, 2021

def uniquePaths(self, m: int, n: int) -> int:
    def factorial(n):
        fact = 1
        for i in range(n, 1, -1):
            fact *= i
        return fact
    return int(factorial(m + n - 2)/(factorial(m-1) * factorial(n-1)))

print(uniquePaths(0, 3, 7))