# coding=utf-8

import math


class TargetFunction:
    def __init__(self, gu, n):
        self.givenU = gu  # заданное значение (то, к которому мы хотим приблизить значение заданного узла)
        self.number = n  # номер заданного узла
        self.vectorU = [0, 0, 0, 0]  # вектор значений функции

        self.emf = None  # ЭДС, электродвижущая сила
        self.conductances = None  # проводимости
        self.derivatives = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]  # матрица производных
        self.gradient = [0, 0, 0, 0, 0]  # градиент (вектор частных проиводных)
        self.hessian = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        # гессиан (матрица смешанных частных производных второго порядка)

        self.gaussSeidelA = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.gaussSeidelB = [0, 0, 0, 0]

    def set_parameters(self, e, cond):
        assert isinstance(cond, list)
        self.emf = e
        self.conductances = cond

    def calculate_tf(self):
        self.vectorU[0] = \
            (self.emf * self.conductances[0] * (
                self.conductances[1] * self.conductances[2] * self.conductances[3] +
                self.conductances[1] * self.conductances[2] * self.conductances[4] +
                self.conductances[1] * self.conductances[3] * self.conductances[4] +
                self.conductances[2] * self.conductances[3] * self.conductances[4]
            )) / (
                self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[3] +
                self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[4] +
                self.conductances[0] * self.conductances[1] * self.conductances[3] * self.conductances[4] +
                self.conductances[0] * self.conductances[2] * self.conductances[3] * self.conductances[4] +
                self.conductances[1] * self.conductances[2] * self.conductances[3] * self.conductances[4]
            )
        self.vectorU[1] = \
            (self.emf * self.conductances[0] * (
                self.conductances[1] * self.conductances[2] * self.conductances[3] +
                self.conductances[1] * self.conductances[2] * self.conductances[4] +
                self.conductances[1] * self.conductances[3] * self.conductances[4]
            )) / (
                self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[3] +
                self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[4] +
                self.conductances[0] * self.conductances[1] * self.conductances[3] * self.conductances[4] +
                self.conductances[0] * self.conductances[2] * self.conductances[3] * self.conductances[4] +
                self.conductances[1] * self.conductances[2] * self.conductances[3] * self.conductances[4]
            )
        self.vectorU[2] = \
            (self.emf * self.conductances[0] * (
                self.conductances[1] * self.conductances[2] * self.conductances[3] +
                self.conductances[1] * self.conductances[2] * self.conductances[4]
            )) / (
                self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[3] +
                self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[4] +
                self.conductances[0] * self.conductances[1] * self.conductances[3] * self.conductances[4] +
                self.conductances[0] * self.conductances[2] * self.conductances[3] * self.conductances[4] +
                self.conductances[1] * self.conductances[2] * self.conductances[3] * self.conductances[4]
            )
        self.vectorU[3] = \
            (self.emf * self.conductances[0] * self.conductances[1] * self.conductances[2] * (
                self.conductances[0] * self.conductances[1] * self.conductances[3] +
                self.conductances[0] * self.conductances[2] * self.conductances[3] +
                self.conductances[1] * self.conductances[2] * self.conductances[3]
            )) / ((
                      self.conductances[0] * self.conductances[1] +
                      self.conductances[0] * self.conductances[2] +
                      self.conductances[1] * self.conductances[2]
                  ) * (
                      self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[3] +
                      self.conductances[0] * self.conductances[1] * self.conductances[2] * self.conductances[4] +
                      self.conductances[0] * self.conductances[1] * self.conductances[3] * self.conductances[4] +
                      self.conductances[0] * self.conductances[2] * self.conductances[3] * self.conductances[4] +
                      self.conductances[1] * self.conductances[2] * self.conductances[3] * self.conductances[4]
                  ))

    def init_derivatives(self):
        self.derivatives[0][0] = - self.vectorU[0]
        self.derivatives[0][1] = - self.vectorU[0] + self.vectorU[1]
        self.derivatives[0][2] = 0
        self.derivatives[0][3] = 0
        self.derivatives[0][4] = 0

        self.derivatives[1][0] = 0
        self.derivatives[1][1] = self.vectorU[0] - self.vectorU[1]
        self.derivatives[1][2] = - self.vectorU[1] + self.vectorU[2]
        self.derivatives[1][3] = 0
        self.derivatives[1][4] = 0

        self.derivatives[2][0] = 0
        self.derivatives[2][1] = 0
        self.derivatives[2][2] = - self.vectorU[2] + self.vectorU[1]
        self.derivatives[2][3] = - self.vectorU[2] + self.vectorU[3]
        self.derivatives[2][4] = 0

        self.derivatives[3][0] = 0
        self.derivatives[3][1] = 0
        self.derivatives[3][2] = 0
        self.derivatives[3][3] = - self.vectorU[3] + self.vectorU[2]
        self.derivatives[3][4] = - self.vectorU[3]

    def calculate_gradient(self):
        for i in range(5):
            self.gradient[i] = 2 * (self.vectorU[self.number] - self.givenU) * self.derivatives[self.number][i]

    def calculate_hessian(self):
        self.hessian[0][0] = 2 * self.derivatives[0][0]
        self.hessian[0][1] = 2 * self.derivatives[0][1]
        self.hessian[0][2] = 2 * self.derivatives[0][2]
        self.hessian[0][3] = 2 * self.derivatives[0][3]
        self.hessian[0][4] = 2 * self.derivatives[0][4]

        self.hessian[1][0] = 2 * self.derivatives[0][1]
        self.hessian[1][1] = 2 * self.derivatives[1][1]
        self.hessian[1][2] = 2 * self.derivatives[1][2]
        self.hessian[1][3] = 2 * self.derivatives[1][3]
        self.hessian[1][4] = 2 * self.derivatives[1][4]

        self.hessian[2][0] = 2 * self.derivatives[0][2]
        self.hessian[2][1] = 2 * self.derivatives[1][2]
        self.hessian[2][2] = 2 * self.derivatives[2][2]
        self.hessian[2][3] = 2 * self.derivatives[2][3]
        self.hessian[2][4] = 2 * self.derivatives[2][4]

        self.hessian[3][0] = 2 * self.derivatives[0][3]
        self.hessian[3][1] = 2 * self.derivatives[1][3]
        self.hessian[3][2] = 2 * self.derivatives[2][3]
        self.hessian[3][3] = 2 * self.derivatives[3][3]
        self.hessian[3][4] = 2 * self.derivatives[3][4]

        self.hessian[4][0] = 2 * self.derivatives[0][4]
        self.hessian[4][1] = 2 * self.derivatives[1][4]
        self.hessian[4][2] = 2 * self.derivatives[2][4]
        self.hessian[4][3] = 2 * self.derivatives[3][4]
        self.hessian[4][4] = 2 * self.derivatives[3][4]

    def set_gs_matrix(self):
        self.gaussSeidelA[0][0] = self.conductances[0] + self.conductances[1]
        self.gaussSeidelA[0][1] = - self.conductances[1]
        self.gaussSeidelA[0][2] = 0
        self.gaussSeidelA[0][3] = 0

        self.gaussSeidelA[1][0] = - self.conductances[1]
        self.gaussSeidelA[1][1] = self.conductances[1] + self.conductances[2]
        self.gaussSeidelA[1][2] = - self.conductances[2]
        self.gaussSeidelA[1][3] = 0

        self.gaussSeidelA[2][0] = 0
        self.gaussSeidelA[2][1] = - self.conductances[2]
        self.gaussSeidelA[2][2] = self.conductances[2] + self.conductances[3]
        self.gaussSeidelA[2][3] = - self.conductances[3]

        self.gaussSeidelA[3][0] = 0
        self.gaussSeidelA[3][1] = 0
        self.gaussSeidelA[3][2] = - self.conductances[3]
        self.gaussSeidelA[3][3] = self.conductances[3] + self.conductances[4]

        self.gaussSeidelB[0] = self.emf * self.conductances[0]
        self.gaussSeidelB[1] = 0
        self.gaussSeidelB[2] = 0
        self.gaussSeidelB[3] = 0

    def get_a(self):
        return self.gaussSeidelA

    def get_b(self):
        return self.gaussSeidelB

    def calculate_fy(self):
        return (self.vectorU[self.number] - self.givenU) ** 2

    def calculate_norm(self):  # норма вектора - сумма квадратов его элементов
        return math.sqrt(sum([n**2 for n in self.gradient]))

    def calculate_dy_fy(self):
        return 2 * (self.vectorU[self.number] - self.givenU)

    def get_vector_u(self):
        return self.vectorU

    def get_gradient(self):
        return self.gradient

    def get_hessian(self):
        return self.hessian

    def get_emf(self):
        return self.emf

    def get_conductances(self):
        return self.conductances

    def get_number(self):
        return self.number

    def calculate_fy_in_point(self, point):
        self.set_parameters(self.get_emf(), point)
        self.calculate_tf()
        self.init_derivatives()
        self.calculate_gradient()
        self.calculate_hessian()
        return self.calculate_fy()
