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

np.random.seed(123456)
s_random = pd.Series(np.random.normal(size=891),
                     index=my_file_1_copy.index)
print(f'\nВыводим рандомные числа: \n{s_random[:4]}')
my_file_1_copy.loc[:, 'random_numbs'] = s_random
print(f'\nВыводим нашу табличку + новый столбец с рандомными числами: \n{my_file_1_copy[:5]}')

print(f'\nВыводим столбцы нашей таблички в обратном порядке: \n{my_file_1_copy[my_file_1_copy.columns[::-1]][:5]}')

my_file_1_copy['item_for_delete'] = s_random
print(f'\nСоздали новый столбец для удаления: \n{my_file_1_copy[:3]}')
del my_file_1_copy['item_for_delete']
print(f'\nУдалили новый столбец для удаления при помощи комады del: \n{my_file_1_copy[:3]}\n')


popped = my_file_1_copy.pop('random_summ_from_first_numbs')
print(f'\nВыводим удаленный столбец при помощи команды pop:\n{popped}')
print(f'\nВыводим таблицу без удаленного столбка: \n{my_file_1_copy[:5]}')

dropped = my_file_1_copy.drop(['random_summ_from_numbs'], axis=1)
print(f'\nВыводим данные из переменной dropped, в которой удалили столбец random_summ_from_numbs\n{dropped}')
