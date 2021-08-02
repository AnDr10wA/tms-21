"""
Есть список словарей со учениками и их оценками по 3 предметам. Пример:
{
‘name’: ‘John Smith’,
‘math’: 10,
‘phys’: 9,
‘chem’: 5,
}
Создать список словарей, содержащих имя и среднюю оценку каждого
ученика. Список отсортировать по значению средней оценки.

"""

spisok = [
{ "name": "John Smith","math": 9, "phys": 9, "chem": 5,},
{ "name": "Andi Antowin","math": 8, "phys": 9, "chem": 7,},
{ "name": "Kris Bush","math": 7, "phys": 4, "chem": 5,},
{ "name": "Milania Leonova","math": 9, "phys": 9, "chem": 9,}
]
new_spisok = []
for n in spisok:
    new_dict = {}
    new_dict["name"] = n["name"]
    new_dict["average"] = (n["math"]+n["phys"]+n["chem"])/3
   # new_spisok[n["name"]] = (n["math"]+n["phys"]+n["chem"])/3
    new_spisok.append(new_dict)
print(new_spisok)

#list_s = list(new_spisok.items())
#print(list_s)
new_spisok.sort(key=lambda i: i["average"], reverse=True)
for i in new_spisok:
    print(i)

'''
print(list_s)
new_dict = {}
for i in list_s:
    new_dict[i[0]] = i[1]
print("*"*100)
print(new_dict)
print("*"*100)

'''
