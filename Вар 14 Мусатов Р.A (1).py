print('''Введите значения через Enter, после ввода последнего
символа нажмите Enter дважды''')
mas = []
while True:
    try:
        a = int(input())
        mas.append(a)
    except:
        break
print(mas[::-1])
