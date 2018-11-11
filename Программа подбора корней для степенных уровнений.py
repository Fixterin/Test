a = float(input('Введите множитель х^2 '))
b = float(input('Введите множитель х '))
c = float(input('Введите свободный член '))
d = float(input('Введите множитель x^3 '))
e = float(input('Введите множитель x^4 '))
f = float(input('Введите множитель x^5 '))
masX = [1,-1,0.5,-0.5,2,-2,-3,3,-4,4,-5,5,-6,6,-7,7,-8,8,-9,9,10,-10,-11,11,-12,12]
def D_zero(a,b,c,D):
    b = b*-1
    x1 = b/2
    return x1
def D_pos(a,b,c,D):
    D = math.sqrt(D)
    b = b*-1
    x1 = (b-D)/(2*a)
    x2 = (b+D)/(2*a)
    return x1, x2
import math
control = None
if d == 0 and e == 0 and f == 0:
    D = b**2-4*a*c
    if D > 0:
        print('x1 and x2 =', D_pos(a,b,c,D))
    elif D == 0:
        print('x1 =', D_zero(a,b,c,D))
    elif D < 0:
        D = D*-1
        D = math.sqrt(D)
        b = b*-1
        D = D/(2*a)
        b = b/(2*a)
        print('Ваш первый корень ',b,'-',D,'*i','  Где i - это квадратный корень из -1')
        print('Ваш второй корень ',b,'+',D,'*i','  Где i - это квадратный корень из -1')
    else:
        print('Что-то пошло не так =D')
elif e == 0 and f == 0:
    for i in masX:
        control = ((d*i+a)*i+b)*i+c
        if control == 0:
            x3 = i
            c = ((d*i+a)*i+b)
            b = (d*i+a)
            a = d
            D = b**2-4*a*c
            if D > 0:
                print('x1 and x2 =', D_pos(a,b,c,D), 'x3 =', x3)
                break
            elif D == 0:
                print('x1 =', D_zero(a,b,c,D), 'x3 =', x3)
                break
            elif D < 0:
                D = D*-1
                D = math.sqrt(D)
                b = b*-1
                D = D/(2*a)
                b = b/(2*a)
                print('Ваш первый корень ',b,'-',D,'*i','  Где i - это квадратный корень из -1')
                print('Ваш второй корень ',b,'+',D,'*i','  Где i - это квадратный корень из -1')
                print('Третий корень ', x3)
                break
            else:
                print('Что-то пошло не так =D')
                break
elif f == 0:
    for i in masX:
        control = (((e*i+d)*i+a)*i+b)*i+c
        if control == 0:
            x4 = i
            c = ((e*i+d)*i+a)*i+b
            b = (e*i+d)*i+a
            a = e*i+d
            d = e
            for i in masX:
                control = ((d*i+a)*i+b)*i+c
                if control == 0:
                    x3 = i
                    c = ((d*i+a)*i+b)
                    b = (d*i+a)
                    a = d
                    D = b**2-4*a*c
                    if D > 0:
                        print('x1 and x2 =', D_pos(a,b,c,D), 'x3 =', x3)
                        print('Четвертый корень ', x4)
                        break
                    elif D == 0:
                        print('x1 =', D_zero(a,b,c,D), 'x3 =', x3)
                        print('Ваш третий корень ', x4)
                        break
                    elif D < 0:
                        D = D*-1
                        D = math.sqrt(D)
                        b = b*-1
                        D = D/(2*a)
                        b = b/(2*a)
                        print('Ваш первый корень ',b,'-',D,'*i','  Где i - это квадратный корень из -1')
                        print('Ваш второй корень ',b,'+',D,'*i','  Где i - это квадратный корень из -1')
                        print('Третий корень ', x3)
                        print('Четвертый корень ', x4)
                        break
                    else:
                        print('Что-то пошло не так =D')
                        break
elif f != 0:
    for i in masX:
        control = ((((f*i+e)*i+d)*i+a)*i+b)*i+c
        if control == 0:
            x5 = i
            c = (((f*i+e)*i+d)*i+a)*i+b
            b = ((f*i+e)*i+d)*i+a
            a = (f*i+e)*i+d
            d = f*i+e
            e = f
            for i in masX:
                control = (((e*i+d)*i+a)*i+b)*i+c
                if control == 0:
                    x4 = i
                    c = ((e*i+d)*i+a)*i+b
                    b = (e*i+d)*i+a
                    a = e*i+d
                    d = e
                    for i in masX:
                        control = ((d*i+a)*i+b)*i+c
                        if control == 0:
                            x3 = i
                            c = ((d*i+a)*i+b)
                            b = (d*i+a)
                            a = d
                            D = b**2-4*a*c
                            if D > 0:
                                print('x1 and x2 =', D_pos(a,b,c,D), 'x3 =', x3)
                                print('Четвертый корень ', x4)
                                print('Пятый корень ', x5)
                                break
                            elif D == 0:
                                print('x1 =', D_zero(a,b,c,D), 'x3 =', x3)
                                print('Ваш третий корень ', x4)
                                print('Ваш четвертый корень ', x5)
                                break
                            elif D < 0:
                                D = D*-1
                                D = math.sqrt(D)
                                b = b*-1
                                D = D/(2*a)
                                b = b/(2*a)
                                print('Ваш первый корень ',b,'-',D,'*i','  Где i - это квадратный корень из -1')
                                print('Ваш второй корень ',b,'+',D,'*i','  Где i - это квадратный корень из -1')
                                print('Третий корень ', x3)
                                print('Четвертый корень ', x4)
                                print('Пятый корень ', x5)
                                break
                            else:
                                print('Что-то пошло не так =D')
else:
    print('Что-то пошло не так аж в самом начале =(')
