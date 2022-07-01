number_string = '0'
sum = 0
while number_string != 'stop':
  number = int(number_string)
  sum = sum + number
  number_string = input('Enter a postive integer >')
print(sum)
