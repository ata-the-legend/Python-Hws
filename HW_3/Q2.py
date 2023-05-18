
#Q2

import math

def division(numerator: float, denominator: float) -> float:
    """
    Divides two numbers

    Args:
        numerator (float): divided
        denominator (float): Divisor

    Returns:
        float: num / den
    """
    return float(numerator) / float(denominator)


def main():
    """
    This is the main func of Q2
    """
    numerator = input('Enter numerator: ')
    denominator = input('Enter denominator: ')
    try:
        print(division(numerator, denominator))
    except ValueError:
        print('Entered numbers are not valid!')
    except ZeroDivisionError:
        print(math.inf)
        

if __name__ == '__main__':
    main()
