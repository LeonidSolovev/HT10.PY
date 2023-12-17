# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

# lst = ['robot'] * 10
# lst += ['human'] * 10
list1 = [0, 1] * 10
list2 = [1, 0] * 10
random.shuffle(list1)
for el in list2:
    if list1[el] == 0:
        list2[el] = 1
    else:
        list2[el] = 0
data = pd.DataFrame({'robot':list1, 'human' :list2})
# for el in data:
#     if data['human'][el] 'robot' == 0:
#         data['human'][el] = 1
#     else:
#         data['human'][el] = 0
# print(data.head())

print(data)