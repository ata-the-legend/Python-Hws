
#Q4

def fact(n: int) -> int:
    """
    The recursive function of factorial

    Args:
        n (int): Number that its factorial will be calculated
    returns:
        int: factorial of n
    """
    if n == 0:
        return 1
    return n * fact(n-1)

def neper_maclaurin(x: int | float, n: int) -> float:
    """
    Calculates neper based exponential function maclaurin series

    e**x = 1 + x/1! + x**2/2! + x**3/3! + ...

    Args:
        x (int | float): Power argument
        n (int): Number of terms in maclaurin series
    returns:
        float: Approximate answer of neper based exponential function
    """
    result = 0
    denominator = 1
    numerator = 1
    for i in range(n):
        if i == 0:
            result += 1
            continue
        denominator *= i
        #denominator = fact(i) # --> maximum recursion depth exceeded --> its not even necessary :(
        numerator = x ** i
        result += numerator / denominator

    return f'{result:.3f}' #'%.3f' %result

def main():
    """
    main function for Q4
    """
    print(neper_maclaurin(2, 1000))

if __name__ == '__main__':
    main()
