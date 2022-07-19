'''
def largest_two(target_list):
    # Output the argument list, the largest
    # element in the list and the second largest
    # element in the list

The largest and second largest elements in the list ['computer', 'science', 'university', 'alberta', 'edmonton'] are university and science

The largest and second largest elements in the list [4, 2, 8, 7, 8] are 8 and 8
'''

def largest_two(target_list):
    tmp_list = target_list.copy()
    largest1 = max(tmp_list)
    tmp_list.remove(largest1)
    largest2 = max(tmp_list)
    print(f'The largest and second largest elements in the list {target_list} are {largest1} and {largest2}')

largest_two([4, 2, 8, 7, 8])