import pandas
import numpy


print()
example_1 = pandas.DataFrame(numpy.arange(1, 5),
                             columns=['num'])
print(example_1)


print()
example_2 = pandas.DataFrame(numpy.array([[1991, 'Tima'],
                                          [1988, 'Mika'],
                                          [1992, 'Dan'],
                                          [1993, 'Rus'],
                                          [1990, 'Zhan']
                                          ]),
                             columns=['year', 'name'])
print(example_2)


print()
names_1 = pandas.Series(['1991', 'Tima'])
names_2 = pandas.Series(['1988', 'Mika'])
example_3 = pandas.DataFrame([names_1, names_2])
example_3.columns = ['year', 'name']
print(example_3)


print()
names_3 = pandas.Series(['Dan', 'Zhan'])
years_3 = pandas.Series([1992, 1992])
example_4 = pandas.DataFrame({'year': years_3,
                             'name': names_3})
print(example_4)


print()
names_4 = pandas.Series(['Dan', 'Zhan'])
years_4 = pandas.Series([1992, 1992])
operations_4 = pandas.Series([3],
                             index=[0])
example_4 = pandas.DataFrame({'year': years_4,
                              'name': names_4,
                              'operations': operations_4})
print(example_4)
