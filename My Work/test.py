my_tuple = (2, 4, 6)
my_list = [10, 20, 30, 40]
length = len(my_tuple)
for index in range(0, length):
  my_list[index] = my_list[index] + my_tuple[index]
print(my_list)
