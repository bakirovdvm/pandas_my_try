import pandas as pd
import numpy as np
import datetime


df_1 = pd.read_excel('titanic3.xls', sheet_name='Sheet1')
print(df_1.shape)

df_2 = pd.read_excel('titanic3.xls', sheet_name='Sheet2')
print(df_2.shape)

print('\nAPPEND')
appended = df_1._append(df_2, ignore_index=True)
print(appended.shape)
print(appended)

print('\nCONCAT')
concated = pd.concat([df_1, df_2])
print(concated.shape)
print(concated[:5])

concated_idx = pd.concat([df_1, df_2], keys=['list_1', 'list_2'])
print(concated_idx)

print('\nДОБАВЛЕНИЕ СТРОКИ ВРУЧНУЮ')
concated.loc[2700] = [1,
                      1,
                      'Mr Timur',
                      'male',
                      30,
                      2,
                      2,
                      'PC 12344',
                      25.445,
                      'A23',
                      'S',
                      '222',
                      '2222',
                      'Astana'
]

print(concated.loc[1])

print('\nУДАЛЕНИЕ СТРОК МЕТОДОМ DROP')
concated = concated.reset_index()
print(concated.index)
print(concated.shape)
dropped = concated.drop([0, 1])
print(dropped.shape)


print('\nФИЛЬТРАЦИЯ СТРОК')
age_30 = concated[concated['age'] > 30]
print(age_30.shape)
print(age_30[:5])
surv = concated[concated['survived'] == 1]
print('Количество выживших', len(surv))
print('Количество выживших', concated['survived'].sum())

print('\n', concated[-1:])

