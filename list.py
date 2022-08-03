## ---LIST---

#Kumpulan data numbers
print('\n====Kumpulan data numbers===')
data_angka = [1,2,3]
print(data_angka)

#Kumpulan data string
print('\n====Kumpulan data string===')
data_string = ['ucup','otong','odah']
print(data_string)

#kumpulan data boolean
print('\n====Kumpulan data boolean===')
data_boolean = [True, False, True]
print(data_boolean)

#Kumpulan data campuran
print('\n====Kumpulan data campuran===')
data_campuran = [1,'bala-bala',2,False]
print(data_campuran)

#Cara alternatif membuat list
data_range = range(0,10) #range dari 0 sampai sebelum 10
print(data_range)
data_list = list(data_range)
print(data_list)

print('\n')
data_range2 = range(0,10,2) #range (start,stop,step)
data_list2 = list(data_range2)
print(data_list2)

#Membuat list dengan  for loop, list comprehension
print('\n====Membuat list pake for===')
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

print('\n')
list_pake_for2 = [i**3 for i in range(0,10)]
print(list_pake_for2)

#Membuat list pake for pake if
print('\n====Membuat list pake for dan if===')
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if) #hasilnya tidak ada angka 5 nya

print('\n')
list_pake_for_if2 = [i for i in range(0,10) if i %2 == 0]
print(list_pake_for_if2)

print('\n')
list_pake_for_if3 = [i for i in range(0,10) if i %2 != 0]
print(list_pake_for_if3)