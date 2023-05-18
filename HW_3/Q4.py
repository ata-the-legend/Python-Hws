
#Q4
import time
import datetime
import jdatetime


def age_in_sec(birthdate: time.struct_time) -> float:
    """
    Calculates the elapsed time of a date in seconds.

    Args:
        birthdate (time.struct_time): Date considered as the origin of time

    Returns:
        float: The elapsed time of asked date in seconds
    """
    # year, month, day = map(int, birthdate.split('/'))
    # print(year, month, day)
    local_time = time.time()
    # print(local_time)

    birth_time = datetime.datetime(birthdate.tm_year, birthdate.tm_mon, birthdate.tm_mday).timestamp()
    # print(birth_time)

    return local_time - birth_time


def until_next_birthday(birthdate: time.struct_time) -> str:
    """
    Calculates the left time until next birthday.

    Args:
        birthdate (time.struct_time): The person's date of birth

    Returns:
        str: The left time until next birthday
    """
    now = datetime.datetime.now()
    birth_next = datetime.datetime(now.year, birthdate[1], birthdate[2])

    local_time = time.time()
    if birth_next.timestamp() < local_time: 
        birth_next = datetime.datetime(now.year +1, birthdate[1], birthdate[2])

    # print(now)
    # print(birth_next)
    # help(datetime.timedelta)

    difference = birth_next - now
    return f'There are {difference.days} days or {difference.days *24*60} minutes untill your next birthday.'


def convert_to_jalali(date: time.struct_time) -> str:
    """
    Convert gregorian to jalali

    Args:
        date (time.struct_time): gregorian date  

    Returns:
        str: jalali date
    """
    #help(jdatetime)
    return str(jdatetime.date.fromgregorian(date=datetime.datetime(date[0], date[1], date[2])))



def main():
    """
    The main func for HW3/Q4
    """
    birthdate = input('Please enter your birthdate: (year/month/date) ')
    print(10*'-')
    birthdate = time.strptime(birthdate, '%Y/%m/%d')
    
    sec_age = age_in_sec(birthdate)
    print(f'You are {sec_age} seconds old.')
    print(10*'-')

    next_birthday = until_next_birthday(birthdate)
    print(next_birthday)
    print(10*'-')

    jalali_birthdate = convert_to_jalali(birthdate)
    print(f'Your birthdate in jalali calender is {jalali_birthdate}.')
    print(20*'-' + '\n')


if __name__ == '__main__':
    main()




