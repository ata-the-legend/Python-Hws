
#Q1

def is_postal_code(test_code: str) -> bool:
    """
    It checks if the input is a valid postal code.
    Right format is 5 digits + '-' + 5 digits.

    Args:
        test_code (str): The variable should be tested.
    
    returns:
        bool: True if the code is valid.
    """
    if len(test_code) != 11:
        return 0
    if test_code[5] == '-':
        nums = [True for item in test_code.split('-') if item.isdigit() and len(item) == 5]
        print(nums)
        if nums == [True, True]:
            return True
    return False

def main():
    """
    main function for Q1
    """
    my_list = ['', 'Hello', '12345-95863', '-5569-65354', '3586 -66566', '35685-36568']
    valid_postal_codes = [item for item in my_list if is_postal_code(item)] 
    print(valid_postal_codes)

if __name__ == '__main__':
    main()