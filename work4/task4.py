#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print("Введите кол-во долек шоколада 'n': ")
n = int(input())
print("Введите кол-во долек шоколада 'm': ")
m = int(input())
print("Введите кол-во долек шоколада которые можно отломить 'k': ")
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да')
else:
    print('Нет')