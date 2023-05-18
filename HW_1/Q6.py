
#Q6

low_lim = int(input('Enter lower limit:'))
high_lim = int(input('Enter higher limit:'))

avvals = []
for num in range(2,high_lim): 
    for avval in avvals:
        if num % avval == 0:
            break
    else:
        avvals.append(num)


print([i for i in avvals if i > low_lim])

