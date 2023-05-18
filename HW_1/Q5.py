
#Q5

laptop_list = [(7,9), (1,5), (5,6), (20,30)]#, (3,4)]

flag = 0
for price_1, quality_1 in laptop_list:
    for price_2, quality_2 in laptop_list:
        if (price_1 > price_2 and quality_1 < quality_2) or (price_1 < price_2 and quality_1 > quality_2):
            flag = 1
            break  
    if flag:
        break      

if flag:
    print('Found')
else:
    print('Not Found')




