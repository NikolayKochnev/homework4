immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
#immutable_var[0] = [3]
#print(immutable_var)   # Ошибка буквально сообщает нам, что кортеж не поддерживает обращение по элементам

mutable_list = [1, 2, 'a', 'c']
print(mutable_list)
mutable_list[0]='d'
print(mutable_list)
