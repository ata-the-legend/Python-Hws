
#Q2

def celcius_to_farenheit(celcius: int | float) -> float:
    """
    It converts Celsius to Fahrenheit

    args:
        celcius (int | float): Temperature in degrees celcius 

    returns:
        float: Temperature in degrees farenheit 
    """
    return celcius * 1.8 + 32

def main():
    """
    main function for Q2
    """
    temp_list = [0, 100, -32, 32, 24.5, 21.2]
    print(list(map(celcius_to_farenheit, temp_list)))

if __name__ == '__main__':
    main()