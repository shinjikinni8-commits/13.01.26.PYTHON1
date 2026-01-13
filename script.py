name = "Ann"
age = 16
city = "Odessa"
role = "student"
college = "IT Step college"

print('My name is ', name, '. I am ', age, '. I am from', city, ' and my role is', role, ', I study in the', college,'.')
print('My name is ' + name + '. I am ' + str(age) + '. I am from ' + str(city) + ' and my role is ' + str(role) + ', I study in the ' + str(college) + '.')
print('My name is {} . I am {} . I am from {} and my role is {}, I study int the {}.'.format(name, age, city, role, college))
print(f'My name is {name}. I am {age}. I am from {city} and my role is {role}, I study int the {college}.')
