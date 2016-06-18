# coding=utf-8

import math

from results_to_show_class import ResultsToShow
from target_function_class import TargetFunction


class OptMethods:
    def __init__(self, tf, e, method, opt):
        self.done = False
        self.eps = e
        self.optimal = opt

        assert isinstance(method, str)
        m_name = 'method_' + method
        chosen_m = getattr(self, m_name)
        assert isinstance(tf, TargetFunction)
        self.log = chosen_m(tf)

    def ret(self):
        """

        :rtype: ResultsToShow
        """
        return self.log

    def method_gold(self, target_function, a=-200, b=200):
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        segment = [a, b]
        gold_ratio = (1 + math.sqrt(5.0))/2

        #  расчёт точек
        x1 = segment[1] - (segment[1] - segment[0]) / gold_ratio
        x2 = segment[0] + (segment[1] - segment[0]) / gold_ratio

        #  расчёт значений функции в этих точках
        cond[target_function.get_number()] = x1
        f1 = target_function.calculate_fy_in_point(cond)

        cond[target_function.get_number()] = x2
        f2 = target_function.calculate_fy_in_point(cond)

        step = 0

        while abs(segment[1] - segment[0]) >= self.eps and step < 10000:
            if f1 >= f2:  # >= для минимума, <= для максимума
                segment[0] = x1
                x1 = x2
                x2 = segment[0] + (segment[1] - segment[0]) / gold_ratio

                #  расчёт значений функции
                cond[target_function.get_number()] = x2
                f2 = target_function.calculate_fy_in_point(cond)

                #  запись результатов
                result.vectorFY.append(f2)
                result.vectorU += target_function.get_vector_u()
            else:
                segment[1] = x2
                x2 = x1
                x1 = segment[1] - (segment[1] - segment[0]) / gold_ratio

                #  расчёт значений функции
                cond[target_function.get_number()] = x1
                f1 = target_function.calculate_fy_in_point(cond)

                #  запись результатов
                result.vectorFY.append(f1)
                result.vectorU += target_function.get_vector_u()
            step += 1

        if step < 10000:
            self.done = True

        return result

    def method_fibonacci(self, target_function, iterations=20, a=-200.0, b=200.0):
        assert isinstance(target_function, TargetFunction)
        assert iterations > 2
        result = ResultsToShow()
        cond = target_function.get_conductances()
        segment = [a, b]
        n = iterations

        def fib(x):
            return 1 if x == 1 or x == 2 else (fib(x-1) + fib(x-2))

        #  расчёт точек
        x1 = segment[0] + (segment[1] - segment[0]) * fib(n-2) / fib(n)
        x2 = segment[0] + (segment[1] - segment[0]) * fib(n-1) / fib(n)

        #  расчёт значений функции в этих точках
        cond[target_function.get_number()] = x1
        f1 = target_function.calculate_fy_in_point(cond)

        cond[target_function.get_number()] = x2
        f2 = target_function.calculate_fy_in_point(cond)

        while n != 1:
            n -= 1
            if f1 > f2:
                segment[0] = x1
                x1 = x2
                x2 = segment[1] - (x1 - segment[0])
                f1 = f2

                #  расчёт значений функции
                cond[target_function.get_number()] = x2
                f2 = target_function.calculate_fy_in_point(cond)

                #  запись результатов
                result.vectorFY.append(f2)
                result.vectorU += target_function.get_vector_u()
            else:
                segment[1] = x2
                x2 = x1
                x1 = segment[0] + (segment[1] - x2)
                f2 = f1

                #  расчёт значений функции
                cond[target_function.get_number()] = x1
                f1 = target_function.calculate_fy_in_point(cond)

                #  запись результатов
                result.vectorFY.append(f1)
                result.vectorU += target_function.get_vector_u()

        if n == 1:
            self.done = True

        return result

    def method_dichotomy(self, target_function, a=-200, b=200):
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        segment = [a, b]
        const = 1  # 1 для минимума, -1 для максимума
        step = 0

        while abs(segment[1] - segment[0]) >= self.eps and step < 10000:
            x = sum(segment) / 2.0

            #  расчёт значений функции
            cond[target_function.get_number()] = x - self.eps
            f1 = target_function.calculate_fy_in_point(cond)

            cond[target_function.get_number()] = x + self.eps
            f2 = target_function.calculate_fy_in_point(cond)

            if const * f1 < const * f2:
                segment[1] = x

                #  запись результатов
                result.vectorFY.append(f2)
                result.vectorU += target_function.get_vector_u()
            else:
                segment[0] = x

                #  запись результатов
                result.vectorFY.append(f1)
                result.vectorU += target_function.get_vector_u()
            step += 1

        if step < 10000:
            self.done = True

        return result

    def method_hooke(self, target_function):  # конфигураций
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        temp = [0, 0, 0, 0, 0]
        f1 = target_function.calculate_fy_in_point(cond)
        inc_step = 1
        alpha = 2
        step = 0

        #  исследующий поиск
        while inc_step >= self.eps and step < 10000:
            f = f1
            flag = False
            old_cond = cond
            for i in range(5):
                e = 1
                while True:
                    temp[i] = cond[i] + inc_step * e
                    tmp = cond
                    tmp[i] = temp[i]
                    f1 = target_function.calculate_fy_in_point(tmp)
                    e *= -1
                    if f1 < f:
                        cond[i] = temp[i]
                        flag = True
                    if not (f1 >= f and e != 1):
                        break
            #  движение по образцу
            if flag:
                for i in range(5):
                    cond[i] = old_cond[i] + (old_cond[i] - cond[i])
                f1 = target_function.calculate_fy_in_point(cond)
                result.vectorFY.append(f1)
                result.vectorU += target_function.get_vector_u()
            else:
                inc_step /= alpha
            step += 1

        if step < 10000:
            self.done = True

        return result

    def opt_step(self, target_function, i):
        assert isinstance(target_function, TargetFunction)
        result = 1.0
        cond = target_function.get_conductances()
        f1 = target_function.calculate_fy_in_point(cond)
        begin = cond[i]

        while True:
            result *= 2
            f2 = f1
            d = self.direction(target_function, i)
            cond[i] = begin + result * d
            f1 = target_function.calculate_fy_in_point(cond)

            if not (abs(f2 - f1) >= self.eps):
                break
        result /= 2
        return result

    @staticmethod
    def direction(target_function, i):
        assert isinstance(target_function, TargetFunction)
        result = 1.0
        cond = target_function.get_conductances()
        f1 = target_function.calculate_fy_in_point(cond)
        cond[i] += result
        f2 = target_function.calculate_fy_in_point(cond)
        if f2 > f1:
            result *= -1
        return result

    def method_rosenbrock(self, target_function):  # вращающихся координат
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        new_x = cond
        k = 0
        step = 0

        while True:
            old_x = new_x
            for i in range(5):
                h = self.opt_step(target_function, i)
                d = self.direction(target_function, i)
                cond[i] += h * d
            f1 = target_function.calculate_fy_in_point(cond)
            result.vectorFY.append(f1)
            result.vectorU += target_function.get_vector_u()
            new_x = cond
            k = k + 1 if k < 4 else 1
            step += 1

            if not (abs(old_x[k] - new_x[k - 1]) >= self.eps and step < 10000 and f1 >= self.eps):
                break

        if step < 10000:
            self.done = True

        return result

    def method_powell(self, target_function):  # сопряжённых направлений
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        direct = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
        n = 0
        t = 0.5
        step = 0

        while True:
            for i in range(5):
                cond[i] += t * direct[n][i]
            target_function.set_parameters(target_function.emf, cond)
            target_function.calculate_tf()
            fy = min(self.method_gold(target_function, -200, cond[target_function.get_number()]).vectorFY)
            self.done = False
            result.vectorFY.append(fy)
            result.vectorU += target_function.get_vector_u()
            if n < 4:
                n += 1
            else:
                n = 0
            step += 1

            if not (fy >= self.eps and step < 10000):
                break

        if step < 10000:
            self.done = True

        return result

    def method_gradient(self, target_function):  # градиентный (обычный/с наискорейшим спуском (Коши))
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        step = 0
        result.normEmpty = False

        while True:
            step += 1
            grad = target_function.get_gradient()
            for i in range(5):
                if self.optimal:  # Коши
                    if grad[i] > 0.0:
                        cond[i] += 1.0 / step
                    if grad[i] < 0.0:
                        cond[i] -= 1.0 / step
                else:  # обычный
                    if grad[i] > 0.0:
                        cond[i] += 0.01
                    if grad[i] < 0.0:
                        cond[i] -= 0.01
            fy = target_function.calculate_fy_in_point(cond)
            result.vectorFY.append(fy)
            result.vectorNorm.append(target_function.calculate_norm())
            result.vectorU += target_function.get_vector_u()

            if not (fy >= self.eps and step < 10000):
                break

        if step < 10000:
            self.done = True

        return result

    def method_seidel(self, target_function):  # покоординатный спуск (Гаусса-Зейделя)
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        old_x = target_function.get_vector_u()
        new_x = target_function.get_vector_u()
        fy = 0.0
        result.normEmpty = False
        step = 0
        target_function.set_gs_matrix()

        while True:
            for i in range(4):
                tmp = 0.0
                for j in range(i):
                    tmp += (target_function.get_a()[i][j] * new_x[j])
                for j in range(i+1, 4):
                    tmp += (target_function.get_a()[i][j] * old_x[j])
                new_x[i] = (target_function.get_b()[i] - tmp) / target_function.get_a()[i][i]

            for i in range(4):
                fy += (new_x[i] - old_x[i]) ** 2
            fy = math.sqrt(fy)
            result.vectorFY.append(fy)
            result.vectorU += new_x
            result.vectorNorm.append(target_function.calculate_norm())
            step += 1

            if not (fy >= self.eps and step < 10000):
                break

        if step < 10000:
            self.done = True

        return result

    def method_fletcher(self, target_function):  # сопряжённых градиентов (Флетчера-Ривза)
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        old_p = target_function.get_gradient()
        old_g = target_function.calculate_norm()
        result.normEmpty = False
        step = 0

        while True:
            step += 1
            alpha = min(self.method_gold(target_function).vectorFY)
            self.done = False

            for i in range(5):
                cond[i] += alpha * old_p[i]
            new_f = target_function.calculate_fy_in_point(cond)
            new_p = target_function.get_gradient()
            new_g = target_function.calculate_norm()

            result.vectorFY.append(new_f)
            result.vectorNorm.append(new_g)
            result.vectorU += target_function.get_vector_u()

            if step % 10 == 0:
                beta = 0.0
            else:
                beta = (new_g ** 2) / (old_g ** 2)
            for i in range(5):
                old_p[i] = new_p[i] + beta * old_p[i]
            old_g = new_g

            if not (old_g >= self.eps and step < 10000):
                break

        if step < 10000:
            self.done = True

        return result

    def method_marquardt(self, target_function):  # Левенберга-Марквардта
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        alpha = 1.0
        new_fy = target_function.calculate_fy()
        result.normEmpty = False
        step = 0

        while True:
            old_fy = new_fy
            grad = target_function.get_gradient()
            target_function.calculate_hessian()

            for i in range(5):
                if grad[i] > 0.0:
                    cond[i] += - (grad[i] / (target_function.get_hessian()[i][i] + alpha))
                if grad[i] < 0.0:
                    cond[i] -= - (grad[i] / (target_function.get_hessian()[i][i] + alpha))
            new_fy = target_function.calculate_fy_in_point(cond)
            result.vectorFY.append(new_fy)
            norma = target_function.calculate_norm()
            result.vectorNorm.append(norma)
            result.vectorU += target_function.get_vector_u()

            if new_fy < old_fy:
                alpha *= 2
            else:
                alpha /= 2
            step += 1

            if not (norma >= self.eps and step < 10000):
                break

        if step < 10000:
            self.done = True

        return result

    def method_davidon(self, target_function):  # Дэвидона-Флетчера-Пауэлла
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        new_cond = target_function.get_conductances()
        direct = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
        alpha = 10.0
        result.normEmpty = False
        step = 0

        d_grad = [0, 0, 0, 0, 0]
        d_cond = [0, 0, 0, 0, 0]
        uk = [0, 0, 0, 0, 0]
        wk = [0, 0, 0, 0, 0]

        while True:
            target_function.init_derivatives()
            target_function.calculate_gradient()
            grad = target_function.get_gradient()
            old_cond = new_cond
            for i in range(5):
                if grad[i] > 0.0:
                    new_cond[i] -= -1 * alpha * direct[i][i] * grad[i]
                if grad[i] < 0.0:
                    new_cond[i] += -1 * alpha * direct[i][i] * grad[i]
            step += 1
            fy = target_function.calculate_fy_in_point(new_cond)
            result.vectorFY.append(fy)
            norma = target_function.calculate_norm()
            result.vectorNorm.append(norma)
            result.vectorU += target_function.get_vector_u()

            for i in range(5):
                d_cond[i] = new_cond[i] - old_cond[i]
                d_grad[i] = target_function.get_gradient()[i] - grad[i]

                if d_cond[i] != 0 and d_grad[i] != 0:
                    uk[i] = (d_cond[i] ** 2) / (d_cond[i] * d_grad[i])
                    wk[i] = (direct[i][i] ** 2 * d_grad[i] ** 2) / (d_grad[i] ** 2 * direct[i][i])

                direct[i][i] += (uk[i] - wk[i])

            if not (target_function.calculate_norm() >= self.eps and step < 10000):
                break

        if step < 10000:
            self.done = True

        return result

    def method_newton(self, target_function):  # касательных (Ньютона); с оптимальным шагом (Ньютона-Рафсона)
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        cond = target_function.get_conductances()
        result.normEmpty = False
        h = 5
        step = 0

        while True:
            step += 1
            target_function.calculate_fy_in_point(target_function.get_conductances())
            grad = target_function.get_gradient()
            hess = target_function.get_hessian()
            for i in range(5):
                if self.optimal:  # Ньютона-Рафсона
                    if grad[i] > 0.0:
                        cond[i] -= h * (grad[i] / hess[i][i])
                    if grad[i] < 0.0:
                        cond[i] += h * (grad[i] / hess[i][i])
                else:  # Ньютона
                    if grad[i] > 0.0:
                        cond[i] -= (grad[i] / hess[i][i])
                    if grad[i] < 0.0:
                        cond[i] += (grad[i] / hess[i][i])

            fy = target_function.calculate_fy_in_point(cond)
            result.vectorFY.append(fy)
            norma = target_function.calculate_norm()
            result.vectorNorm.append(norma)
            result.vectorU += target_function.get_vector_u()

            if not (fy >= self.eps and step < 10000):
                break

        if step < 10000:
            self.done = True

        return result

    def method_broyden(self, target_function):  # Бройдена-Флетчера-Гольдфарба-Шанно
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        old_x = target_function.get_conductances()
        result.normEmpty = False
        step = 0

        i_matrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
        new_approx = i_matrix
        new_x = [0, 0, 0, 0, 0]
        direct_p = [0, 0, 0, 0, 0]
        s_vector = [0, 0, 0, 0, 0]
        y_vector = [0, 0, 0, 0, 0]
        alpha = 0.05

        while target_function.calculate_norm() >= self.eps and step < 10000:
            target_function.calculate_fy_in_point(old_x)
            old_grad = target_function.get_gradient()

            for i in range(5):
                direct_p[i] = sum([- old_grad[k] * new_approx[k][i] for k in range(5)])

            for i in range(5):
                new_x[i] = old_x[i] + alpha * direct_p[i]  # alpha должно удовлетворять условиям Вольфе

            fy = target_function.calculate_fy_in_point(new_x)
            new_grad = target_function.get_gradient()
            result.vectorFY.append(fy)
            result.vectorNorm.append(target_function.calculate_norm())
            result.vectorU += target_function.get_vector_u()

            for i in range(5):
                s_vector[i] = new_x[i] - old_x[i]
                y_vector[i] = new_grad[i] - old_grad[i]

            old_approx = new_approx
            for i in range(5):
                for j in range(5):
                    new_approx[i][j] =\
                        (i_matrix[i][j] - direct_p[i]*s_vector[i]*y_vector[j]) * old_approx[i][j] *\
                        (i_matrix[i][j] - direct_p[i]*y_vector[i]*s_vector[j]) + (direct_p[i]*s_vector[i]*s_vector[j])
            step += 1

        if step < 10000:
            self.done = True

        return result

    def method_zangwill(self, target_function):  # Зангвилла
        assert isinstance(target_function, TargetFunction)
        result = ResultsToShow()
        result.normEmpty = False
        step = 0

        old_y = target_function.get_conductances()
        old_grad = target_function.get_gradient()
        alpha = 0.5
        myu = 0.05

        while True:
            step += 1
            opt_y = [0, 0, 0, 0, 0]
            for i in range(5):
                opt_y[i] = old_y[i] + alpha * old_grad[i]
            target_function.calculate_fy_in_point(opt_y)
            jalpha = min(self.method_gold(target_function).vectorFY)

            new_y = [0, 0, 0, 0, 0]
            for i in range(5):
                new_y[i] = old_y[i] + jalpha * old_grad[i]
            target_function.calculate_fy_in_point(new_y)
            grad = target_function.get_gradient()

            old_y = new_y

            myu_y = [0, 0, 0, 0, 0]
            for i in range(5):
                myu_y[i] = new_y[i] + myu * grad[i]
            target_function.calculate_fy_in_point(myu_y)
            dia_myu = min(self.method_gold(target_function).vectorFY)

            old_z = [0, 0, 0, 0, 0]
            for i in range(5):
                old_z[i] = new_y[i] + dia_myu * grad[i]
            fz = target_function.calculate_fy_in_point(old_z)

            opt_norm = target_function.calculate_norm()
            result.vectorFY.append(fz)
            result.vectorNorm.append(opt_norm)
            result.vectorU += target_function.get_vector_u()

            if not (opt_norm >= self.eps and step < 10000):
                break
            else:
                myu_z = [0, 0, 0, 0, 0]
                for i in range(5):
                    myu_z[i] = old_z[i] + myu * old_grad[i]
                target_function.calculate_fy_in_point(myu_z)
                new_myu = min(self.method_gold(target_function).vectorFY)

                new_z = [0, 0, 0, 0, 0]
                for i in range(5):
                    new_z[i] = old_z[i] + new_myu * old_grad[i]
                for i in range(5):
                    old_grad[i] = new_z[i] - old_y[i]

        if step < 10000:
            self.done = True

        return result
