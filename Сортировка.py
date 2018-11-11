list = [10,-3,5,14,7,28,0,36]
def sort(mas):
    Dlina = len(mas)
    for i in range(0,Dlina):
        save_point = i
        for z in range(i,Dlina):
            if mas[z] > mas[i]:
                per = mas[i]
                mas[i] = mas[z]
                mas[z] = per
        print(mas)
    return mas
print(sort(list))
