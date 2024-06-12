import pandas


my_file = pandas.read_csv('username-password-recovery-code_2.csv')
print(my_file)

print()
my_file_2 = pandas.read_csv('username-or-email_2.csv', index_col='Identifier')
print(my_file_2)

print()
titanic_file_indexNAME = pandas.read_csv('titanic.csv', index_col='Name')
titanic_file_All = pandas.read_csv('titanic.csv')
print(titanic_file_indexNAME[:6])

print()
print('имена столбцов:', my_file.columns)
print('Индексы файла 1', my_file.index)
print('индексы файла 2', my_file_2.index)

print()
print('Файл Титаник:')
print('имена столбцов:', titanic_file_All.columns)
print('количество строк:', len(titanic_file_All))
print('количество строк и столбцов:', titanic_file_All.shape)
print('количество значений:', titanic_file_All.size)
print()
print(f'получаем столбец:\n{titanic_file_All["Age"][:4]}\n'
      f'Тип объекта: {type(titanic_file_All["Age"][:4])}')
print()
print(f'Получаем несоклько столбцов: \n{titanic_file_All[["Name", "Age", "Sex"]][:4]}')
print()
print(f'Строка по значению индекса: \n{titanic_file_indexNAME.loc["Heikkinen, Miss. Laina"]}')
print()
print(f'Несколько строк по значению индекса: \n{titanic_file_indexNAME.loc[["Heikkinen, Miss. Laina", "Bonnell, Miss. Elizabeth"]]}')
print()
print(f'Несколько строк по позициям: \n{titanic_file_indexNAME.iloc[[1, 8]]}')
print()
print(f'Получаем позицию по значению индекса: \n{titanic_file_indexNAME.index.get_loc("Heikkinen, Miss. Laina")}')

print()
print(f'Люди младше 25 True/False: \n{titanic_file_All["Age"] <= 25}')
print()
print(f'Данные людей младше 20 лет: \n{titanic_file_All[titanic_file_All["Age"] <= 20]}')
print()
print(f'Данные людей младше 20 лет: \n{titanic_file_All[(titanic_file_All["Age"] <= 20) & titanic_file_All["Survived"] == 1]}')
print()
print(f'Данные людей младше 20 лет: \n{titanic_file_indexNAME.loc[["Heikkinen, Miss. Laina", "Bonnell, Miss. Elizabeth"], ["Age", "Survived"]]}')

