def factorial(n: int) -> int:
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    return abs(a * b) // gcd(a, b)
