from datetime import datetime
from sys import setswitchinterval

#date_birth="1988-08-25"
#print(datetime.date(datetime.strptime(date_birth,"%Y-%m-%d")))
#date_birth_data=(datetime.date(datetime.strptime(date_birth,"%Y-%m-%d")))
#year=date_birth_data.year
#print(year)
#now_year=datetime.now().year
#print(now_year)
#age(now_year-year)
#print(age)
#b=10
#Верное диагональ!
# a=float(input("Диагональ 1"))
# print("переменая А:",str(a),sep="-",end="/")
# b=float(input("Диагональ 2"))
# print("переменая b:",str(b),sep="-",end="/")
# print("Итого:"),(a*b)/2
#print("to be","or not","to be",sep='\n')
#Задания 5
# print('"life is what happens')
# print('     when')
# print("   you're"'busy making other plans"')
# True(Верно)
# False(Обман)
# None
# a=5
# b=5
# c=5
# print(a==b)
# # if {Истина}else{ложь}

# if a>b<c:
#     print("истина")
#     c=1
#     print(a)
# else:
#     print("ложь")
#     c=2
# print(c)
# if a>b:
#     print("Истина1")
# elif a>b-1:(
#     print("истина 2"))
# else:a>b-3
# print("Ложь")
#
# if a>b:
#     print("истина1")
#     if a==b:
#         print("итсина2")
#         if a<c:
#             print("Истина3")
#         else:
#             print("ложь 1")
#         else:
#         print("ложь2")
#     else:
#         print("ложь 3")
# Верное задания
# string =input("Ведите 3 числа через пробле")
# print(string)
# numbers = string.split(" ")
# print(numbers)
# # summa = int(numbers[0])+int(numbers[1])+int(numbers[2])
# summa2=0
# for i in numbers:
#     summa2+=int(i)
#     print(summa2)
# a=True
# Плошадь треугольника,Верное
# triangle = input("ведите H и L:")
# h = int(triangle.split(" ")[0])
# l = int(triangle.split(" ")[1])
# print("итого рлощпдь треугольника равна:", h*l/2)
#Верное 3 числа
# string=input()
# numbers=string.split(" ")
# if len(numbers) == 4:
#     result=int(numbers[0])*int(numbers[1])*int(numbers[2])*int(numbers[3])
#     print("* ", result)
# elif len(numbers) ==3:
#     result=int(numbers[0])+int(numbers[1])+int(numbers[2])
# elif len(numbers)<1:
#     print("Данные не ведены")
# else:
#     print("Веденое 1 или 2 числа")
#Пример деления верно:
# string=input()
# numbers=string.split(" ")
# if len(numbers) == 4:
#     result=int(numbers[0])*int(numbers[1])*int(numbers[2])*int(numbers[3])
#     print("* ", result)
# elif len(numbers) ==3:
#     result=int(numbers[0])+int(numbers[1])+int(numbers[2])
#     print("+ ",result)
# elif len(numbers)<1:
#     print("Данные не ведены")
# else:
#     result=(float(numbers[0])/float(numbers[1])).__format__(".4f")
#     print("/ ",result)
#     print("Веденное 1 или 2 число")
#Один из способов решения!!!
# string=input()
# numbers=string.split(" ")
# integer = int(len(numbers))
# print(numbers)
# if numbers[0]=="":
#     print("Пустая строка")
#     integer=0
# match integer:
#     case 4:
#         result=(int(numbers[0])*int(numbers[1])*int(numbers[2])*int(numbers[3]))
#     case 3:
#         result = (int(numbers[0])+int(numbers[1])+int(numbers[2])+int(numbers[3]))
#     case 2:
#         result = (int(numbers[0])/int(numbers[1])/int(numbers[2])/int(numbers[3]))
#     case 1:
#         print("Веддено 0 или 1 число")
#Пример циклов!
# a=0
# while a<5:
#     print("Мы в цикле")
#     print("Faer")
#     a=a+1
# #завершения цикла
#     if a==3:
#      break
#     a=a+1
# print("game over")
#Континиум
#перевернуть цифры
# a=0
# while a<5:
#
#     print(a)
#     a=a+1
#     if a==3:
#         a=a+1
# else:
#     print("game over")
#     b=10
#     while b>=0:
#         print(b)
#         b=b-1
#перебор цифр 1-10 верно
# for i in range(10):
#     print(i)
#перебор цифр назад от 10-1 верно
# for i in range(10):
#     print(9-i)
#Четные числа
# for i in range(10):
#      if i%2:
#          continue
#      print(i)
#Нечетные
# for i in range(10):
#      if i%3:
#          continue
#      print(i)
#Деления числов
# for i in range(1,100):
#     if i%3==0:
#         print(i)
#         #break
# else:
#     print("завершения")
#домашка,№1
# string=input("ведите числа через проблем и знак").split(" ")
# numbers1=float(string[0])
# numbers2=float(string[1])
# numbers3=float(string[2])
# znak=string[3]
# if znak=="+":
#     result=numbers1+numbers2+numbers3
# elif znak=="*":
#     result=numbers1*numbers2*numbers3
#     print(result)
# elif znak=="-":
#     result=numbers1-numbers2-numbers3
#     print(result)
# elif znak=="/":
#     result=(numbers1/numbers2/numbers3).__format__("f4")
#     print(result)
# else:
#     print("Некореректные данные")
#Самое простейшие решения:Математического характера:
# print(eval(string))
#Задания №2
# string=input("ведите 3 числа").split(" ")
# numbers=[]
# for i in string:
#     numbers.append(int(i))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers)/len(numbers))
#Вариант cо строкой и цифры
# string=input("ведите 3 числа").split(" ")
# numbers=[]
# for i in string:
#     numbers.append(int(i))
# print("max:"+str(max(numbers)))
# print("min:",min(numbers))
# print(f"Avg{str(sum(numbers)/len(numbers))}")
#Задания№3
# string=input().split(" ")
# numbers1=float(string[0])
# znak=string[1]
# if znak=="m":
#     result=(numbers1/16.09).__format__(".5f")
#     print("Mile",result)
# elif znak=="d":
#     result=(numbers1*39.3701).__format__(".5f")
#     print("Duim",result)
# elif znak=="y":
#     result=(numbers1*1.09361).__format__(".5f")
#     print("Yards",result)
# print("Данные ккорректны")
#Задания№4
print(ffdf)



