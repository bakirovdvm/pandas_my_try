import pandas


my_file = pandas.read_csv('username-password-recovery-code_2.csv')
print(my_file)

print()
my_file_2 = pandas.read_csv('username-or-email_2.csv', index_col='Identifier')
print(my_file_2)

print()
print(my_file_2[:1])

print()
print(my_file.columns)
print(my_file.index)


