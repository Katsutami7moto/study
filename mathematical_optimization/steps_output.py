# coding=utf-8

from opt_methods_class import OptMethods
from target_function_class import TargetFunction


def show_values_vector(target_function):
    assert isinstance(target_function, TargetFunction)
    print
    print "Вектор значений функции: "
    print target_function.get_vector_u()
    print


def show_gradient(target_function):
    assert isinstance(target_function, TargetFunction)
    print "Градиент функции: "
    print target_function.get_gradient()
    print
    print "Норма градиента: "
    print target_function.calculate_norm()
    print


def show_hessian(target_function):
    assert isinstance(target_function, TargetFunction)
    hm = target_function.get_hessian()
    print "Матрица Гессе: "
    for line in hm:
        print line
    print


def show_optimization(target_function, accuracy, method, optimal):
    assert isinstance(target_function, TargetFunction)
    calculated = OptMethods(tf=target_function, e=accuracy, method=method, opt=optimal)
    result = calculated.ret()

    print "Решение найдено за " + str(len(result.vectorFY)) + " шагов."
    print
    for i in range(len(result.vectorFY)):
        print "Шаг " + str(i+1) + ":"
        for j in range(i*4, i*4+4):
            tmp = 4 if (j+1) % 4 == 0 else (j+1) % 4
            print " U" + str(tmp) + " = " + str(result.vectorU[j])
        if not result.normEmpty:
            print
            print " Норма градиента = " + str(result.vectorNorm[i])
        print
        print " F(Y) = " + str(result.vectorFY[i])
        print
        print
    if not calculated.done:
        print "Допустимое кличество шагов превышено."


given_function = TargetFunction(gu=12.0, n=1)  # n - от 0 до 3
given_function.set_parameters(e=11.0, cond=[11.0, 12.0, 11.0, 12.0, 11.0])
given_function.calculate_tf()
given_function.init_derivatives()
given_function.calculate_gradient()
given_function.calculate_hessian()

show_values_vector(given_function)
show_gradient(given_function)
show_hessian(given_function)

#  Аргументы для показа:
#
#               Методы одномерной оптимизации:
#
#  'gold' - для метода золотого сечения
#
#  'fibonacci' - для метода чисел Фибоначчи
#
#  'dichotomy' - для метода дихотомии
#
#               Методы 0-го порядка:
#
#  'hooke' - для метода конфигураций (Хука-Дживса)
#
#  'rosenbrock' - для метода вращающихся координат (Розенброка)
#
#  'powell' - для метода сопряжённых направлений (Пауэлла)
#
#               Методы 1-го порядка:
#
#  'gradient' - для градиентного метода (opt = False/True) = (с дискретным шагом/с наискорейшим спуском (Коши))
#
#  'seidel' - для метода покоординатного спуска (Гаусса-Зейделя)
#
#  'fletcher' - для метода сопряжённых градиентов (Флетчера-Ривза)
#
#  'marquardt' - для метода Левенберга-Марквардта
#
#  'davidon' - для метода Дэвидона-Флетчера-Пауэлла
#
#  'zangwill' - для метода Зангвилла
#
#               Методы 2-го порядка:
#
#  'newton' - для метода (opt = False/True) = (касательных (Ньютона)/с оптимальным шагом (Ньютона-Рафсона))
#
#  'broyden' - для метода Бройдена-Флетчера-Гольдфарба-Шанно
#


arg = (given_function, 0.1, 'rosenbrock', False)

show_optimization(*arg)
