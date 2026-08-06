# lets create some random list
programming_languages = ['JavaScript', 'Python', 'C++', 'C#', 'php']
le_nested_list = ['Martha', 24, ['C++', 'Python']]

# and a tuple
my_senior_employee = ('Bob', 29, '29 Github Street')

# now lets have some fun with it
print(programming_languages.count('JavaScript')) # 1
print(programming_languages[1]) # Python
programming_languages[0] = 'HTML'
print(programming_languages) # HTML, Python, C++, C#, php
del programming_languages[0]
print(programming_languages[0]) # Python

# lets work with these nested lists
print('C++' in le_nested_list)
print('C++' in le_nested_list[2])
print(le_nested_list[2][1]) # Python
del le_nested_list[2]
print(le_nested_list) # Martha, 24

# lets create a new if statement
# del programming_languages[3] # if confused why this is 3, refer to line 12
if ('php' in programming_languages):
    print('The list programming_languages does have the word \'php\' in it.')
else:
    print('why did you delete php from the list')

# wow lets try this
developer_number_one = ['John', 67, 'Python']
name, age, language = developer_number_one
print(name)
print(age)
print(language)


