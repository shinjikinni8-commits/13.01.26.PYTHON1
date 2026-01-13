print("Hello World!")
name = input("Enter ur name: ")
print("Hello! My name's " + name)
name = 'Ann'
age = 16
height = 1.65
is_student = True

print(name, age, height, is_student)
print(name + ' ' + str(age) + ' ' + str(height) + ' ' + str(is_student))
print('{} {} {} {}'.format(name, age, height, is_student))
print(f'{name} {age} {height} {is_student}')

print('My name is ', name, '. I am ', age, '. My height is', height, ' and my status is', is_student, ' (student).')
print('My name is ' + name + '. I am ' + str(age) + '. My height is' + str(height) + 'and my status is' + str(is_student) + ' (student).')
print('My name is {} . I am {} . My height is {} and my status is {} (student).'.format(name, age, height, is_student))
print(f'My name is {name}. I am {age}. My height is {height} and my status is {is_student} (student).')
