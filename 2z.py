# Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom(a):
    if a == a[::-1]:
        print("yes")
    else:
        print("no")
str_ = input("Введите слово для проверки: ")
palindrom(str_)