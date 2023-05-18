
#Q3
"""
In particular, you may run into pitfalls if you use assertions for:

    Processing and validating data
    Handling errors
    Running operations with side effects
"""


def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    You shouldn't use assert statements to verify the user's input or any other 
    input data from external sources. That's because production code typically 
    disables assertions, which will remove all the verification.

    Args:
        price (int): _description_
        discount (float, optional): _description_. Defaults to 0.0.

    Raises:
        in: _description_

    Returns:
        int: _description_
    """
    final_price = int(price * (1 - discount))
    assert 0 < final_price <= price, "This AssertaionErrror wont raise in python optimized mode"
    if 0 < final_price <= price:
        return final_price
    return "Discount expects a value between 0 and 1"  # for user
    #raise ValueError("Discount expects a value between 0 and 1")  # for code

def main():
    """
    This is the main func of Q3
    """
    print(apply_discount(100, 0.2))

if __name__ == '__main__':
    main()
    





