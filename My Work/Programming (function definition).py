'''
def stats():
    Output the list that the global idenfifier
    my_list is bound to and the mean and
    the population standard deviation of the
    numbers in the list, rounded to two decimal
    places.

[2, 4, 6, 8, 10, 12]
mean is 7.0
population standard deviation is 3.42
'''

my_list = [2, 4, 6, 8, 10, 12]
def stats():
    n = len(my_list)
    mean = sum(my_list) / n

    tmp_sum = 0
    for num in my_list: 
        tmp_sum += ((num - mean) ** 2)
    pop_std = (tmp_sum / n) ** 0.5

    print(my_list)
    print(f'mean is {mean:.2f}')
    print(f'population standard deviation is {pop_std:.2f}')

stats()