
#Q5


def binary_search(item: int | None = None, *args: int, low: int = 0 ,high: int | None = None) -> int:
    """
    this is an efficient algorithm for finding an item from a sorted list of items. 
    It works by repeatedly dividing in half the portion of the list that could contain the item, 
    until you've narrowed down the possible locations to just one.

    Args:
        item (int | None) = None : Item that wants to be searched.
        *args (int) : sorted list items.
        low (int) = 0 : Low index of the search area.
        high (int | None) = None: High index of the search area.
        
    returns:
        int: The index of searched item or None if it wasnt in the list.
    """
    if high == None:
        high = len(args) - 1
    mid = (low + high)//2
    val = args[mid]
    #print(low, mid, high, val)

    if high < low:
        return None
    elif val == item:
        return mid
    elif val < item:
        return binary_search(item, *args, low = mid + 1, high= high)
    else:
        return binary_search(item, *args, low= low, high = mid - 1)


def main():
    """
    main function for Q5
    """
    print(binary_search(3, 1, 2, 3, 5, 7, 9, 11, 13))

if __name__ == '__main__':
    main()


# def binary_search(item = None, *args):
#     low = 0
#     high = len(args) - 1
#     while low <= high:            
#         mid = (low + high)//2
#         val = args[mid]
#         if val == item:
#             return mid
#         elif val < item:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None