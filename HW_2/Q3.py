
#Q3

def last_sum_of_digits(num: int) -> int:
    """
    It keeps adding the digits of input integer until sum become single digit.

    Args:
        num (int): The number that wanted to add its digits

    returns:
        int: Single digit sum
    """
    sum_result = sum([int(i) for i in str(num)])
    if sum_result < 10:
        return sum_result
    return last_sum_of_digits(sum_result)


def main():
    """
    main function for Q3
    """
    print('ex: 123456 -->', last_sum_of_digits(123456))
    print(last_sum_of_digits(int(input('Enter a number: '))))


if __name__ == '__main__':
    main()

