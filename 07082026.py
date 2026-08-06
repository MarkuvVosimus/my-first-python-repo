# use append, extend, insert, remove, sort, clear, pop
# set le values
programming_languages = ['C++', 'Python', 'C#', 'php']
numbers = [1, 2, 3, 4, 5]
more_numbers = [10, 11, 12, 13, 14, 15]
employee_1 = ['Bob', 29, '29 Github Street']
employee_2 = ['Alice', 34, '2026 Visual Studio Way']

# appending
numbers.append([6,7,8])
print(numbers) # [1, 2, 3, 4, 5, [6, 7, 8]]
numbers.remove(5)
print(numbers)  # [1, 2, 3, 4, [6, 7, 8]] # found out that remove does NOT work on nested lists

# lets insert
programming_languages.insert(2, 'HTML')
print(programming_languages) # ['C++', 'Python', 'HTML', 'C#', 'php']

# lets extend
more_numbers.extend((16, 17))
print(more_numbers)
numbers_20 = [18, 19, 20, 21, 22]
more_numbers.extend(numbers_20)
print(more_numbers)

# inserting
numbers_20.insert(2, 19.5)
print(numbers_20)
more_numbers.insert(0, [9, 8])
print(more_numbers)

# sorting
sort_list_1 = [92, 34, 58, 12, 9, 433, 2]
sort_list_2 = [4, 948, 279, 3033, 110, 523]
sorted_list_1 = sorted(sort_list_1)
print(sorted_list_1) # down to top sort
sorted_list_1.reverse()
print(sorted_list_1) # top to down sort

# pop
number_list = [1, 2, 3, 4]
number_list.pop(2)
print(number_list) # 1, 2, 4

# indexing
index = programming_languages.index('Python')
print(index) # 1

# tuples
developer = ('Jessica')
print(tuple(developer)) # J e s s i c a

if 'C#' in programming_languages:
    print('C# is in programming_languages') # this will print
else:
    print('C# is not in programming_languages')

new_dev = ('Jessica', 'Senior Dev')
name, *rest = new_dev
print(name)
print(*rest)

