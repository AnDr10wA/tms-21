a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

for i in a.keys():
    a[i] += str(len(i))
print(a)
dict_list = list(a.keys())
ind_dict = len(a) - 1
print(dict_list)
while ind_dict>=0:
    a[dict_list[ind_dict]] += str(len(dict_list[ind_dict]))
    ind_dict -= 1
print(a)