'''
Домашнее задание
1. Ознакомиться с built-in функциями - https://docs.python.org/3/library/functions.html
2. Объявить словарь в котором будут следующие ключи (first_name, last_name, email, age )
3. Перебрать элементы словаря и положить в список только те которые удовлетворяю следующие условия:
- если это строка, то длина должна быть больше 5 и содержать в себе букву "c"
- если это число, то оно должно быть в ренже [25-40]
4. Перебрать созданный в шаге 3 список и удалить из него элементы в которых есть либо буква "g" либо буква "t"
5. Отсортировать список Z-A
6. Собрать из этого списка одну строку в которой элементы списка будут разделены запятой
7. Из строки полученной в шаге 6 сделать обратно список
'''
my_dict = {
    'first_name': 'Evgeniy',
    'last_name': 'Reznikov',
    'sex': 'men',
    'city': 'Kiev',
    'education': 'management',
    'working': 'programmer',
    'email': 'jeincr@gmail.com',
    'year': 1987,
    'age': 30
}

my_list = []
for d in my_dict.values():
    if type(d) == str and len(d) > 3 and 'c' not in d.lower():
        my_list.append(d)
    elif type(d) == int and d in range(25, 40):
        my_list.append(d)
print(my_list)

for lst in my_list:
    if type(lst) == str and 't' in lst.lower() or type(lst) == str and 'y' in lst.lower():
        my_list.remove(lst)
print(my_list)

sort_list = (sorted([str(item) for item in my_list], reverse=True))
# print(sorted(map(str, my_list), reverse=True))
print(sort_list)

my_str = ', '.join(str(s) for s in sort_list)
print(my_str)

new_list = my_str.split(',')[::-1]
print(new_list)

