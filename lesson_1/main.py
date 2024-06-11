import pandas
import numpy


print()
print('создание DataFrame из словоря списков ')
name = ['Tima', 'Mika', 'Dan', 'Rus', 'Zhan']
year = [1991, 1988, 1992, 1993, 1990]

names_dict = {'name': name,
               'year': year}

print(names_dict)
print()

names_dataFrame_1 = pandas.DataFrame(names_dict)
print(names_dataFrame_1.index)
print(names_dataFrame_1)
print()

names_dataFrame_1.index = ['a', 'b', 'c', 'd', 'e']
print(names_dataFrame_1.index)
print(names_dataFrame_1)
print()

print('создание DataFrame из списка словарей')
names_dataFrame_2 = pandas.DataFrame([
    {
        'name': 'Tima',
        'year': 1991
    },
    {
        'name': 'Mika',
        'year': 1988
    }
], columns=['year', 'name'])
print(names_dataFrame_2)

names_dataFrame_1.to_csv('names_1.csv', index=False)
names_dataFrame_1.to_csv('names_2.csv', index=True)

names_dataFrame_2.to_csv('names_3.csv', index=False)
