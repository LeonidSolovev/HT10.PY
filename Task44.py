# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
list1 = [0, 1]
list2 = [1, 0]
random.shuffle(lst)
data = pd.DataFrame({'robot':list1, 'human' :list2})
print(data.head())

# print(data)