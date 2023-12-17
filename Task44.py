# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd


list1 = []
for el in range(0, 20):
    list1.append(random.randint(0, 1))
list2 = []
for el in range(0, 20):
    list2.append(0)
for el in range(len(list1)):
    if list1[el] == 0:
        list2[el] = 1
data = pd.DataFrame({'robot':list1, 'human' :list2})

print(data)