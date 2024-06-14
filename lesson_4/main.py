import pandas as pd
import numpy as np


my_file_1 = pd.read_csv('titanic.csv')

print(my_file_1[:4])
print(my_file_1.columns)


my_file_1_rename_Name = my_file_1.rename(columns={'Name': 'FullName'})
print(f'\nПереименовываем ячейку в шапке через новую переменную: \n{my_file_1_rename_Name.columns}')


my_file_1.rename(columns={'Name': 'FullName_original_file'}, inplace=True)
print(f'\nПереименовываем ячейку в шапке через новую переменную \n{my_file_1.columns}')

my_file_1_copy = my_file_1.copy()
my_file_1_copy['random_summ_from_first_numbs'] = (my_file_1_copy['PassengerId']
                                                 + my_file_1_copy['Survived']
                                                 + my_file_1_copy['Pclass'])
print(f'\nДобавил новый столбец в конце \n{my_file_1_copy[:4]}')

my_file_1_copy.insert(12, 'random_summ_from_numbs', (my_file_1_copy['PassengerId']
                                                     + my_file_1_copy['Fare']
                                                     + 0.1547))
print(f'\nДобавил новый предпоследний столбец \n{my_file_1_copy[:4]}')
print(my_file_1_copy.columns)

my_file_1_copy['random_summ_from_numbs'] = my_file_1_copy['random_summ_from_numbs'].round()
print(f'\nОкругляем предпоследнюю колонку:\n{my_file_1_copy[:4]}')

print(f'\nВспоминаем количество столбцов и строк: {my_file_1_copy.shape}')
