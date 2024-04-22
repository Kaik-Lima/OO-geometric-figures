class polygons:
    def __init__(self, amount_sides):
        # Número dos lados
        self.n = amount_sides
        self.side = []

    def read_sides(self):
        # Faz a leitura das medidas
        self.side = [float(input('Digite o tamanho do lado ' + str(i + 1) + ': ')) for i in range(self.n)]

    def show_sides(self):
        # Imprime os números propostos de cada lado da forma
        for i in range(self.n):
            print('Lado', i + 1, 'tem comprimento', self.side[i])


class triangle(polygons):
    def __init__(self):
        # Calcula os três lados do triângulo
        polygons.__init__(self, 3)

    def area(self):
        a, b, c = self.side
        # Calcula o semi-perímetro
        s = (a + b + c) / 2
        # Fórmula de calcular a área do triângulo
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('A área do triângulo é %0.2f' % area)


class rectangle(polygons):
    def __init__(self):
        # Calcula os quatro lados do retângulo
        polygons.__init__(self, 4)

    def read_sides(self):
        side1 = float(input('Digite o tamanho do lado 1: '))
        side2 = float(input('Digite o tamanho do lado 2: '))
        # Armazena os tamanhos nas sides corretas
        self.side = [side1, side2, side1, side2]

    def area(self):
        # Realiza a multiplicação dos dois valores diferentes
        return self.side[0] * self.side[1]

    def diagonally(self):
        # Retorna o valor da diagonal do retângulo
        return (self.side[0] ** 2 + self.side[1] ** 2) ** 0.5

    def is_rectangle(self):
        # Verifica se os valores são retângulos
        def is_rectangle(self):
            # Retorna os valores elevado ao quadrado conforme o teorema de Pitagoras
            return(self.side[0] ** 2 == self.side[1] ** 2 + self.side[2] ** 2
                   or self.side[1] ** 2 == self.side[0] ** 2 + self.side[2] ** 2
                   or self.side[2] ** 2 == self.side[0] ** 2 + self.side[1] ** 2)

    def right_triangle(self, triangle):
        # Condições lógicas
        if self.is_rectangle():
            print("O triângulo passado é retângulo.")
        else:
            print("O triângulo passado não é retângulo.")


# Polígono Test
poly = polygons(5)
poly.read_sides()
poly.show_sides()


# Triângulo Test
tri = triangle()
tri.read_sides()
tri.show_sides()
tri.area()


# Retângulo Test
ret = rectangle()
ret.read_sides()
ret.show_sides()
ret.area()
print(f'Área do retângulo: {ret.area():.2f}')


# Diagonal Test
ret.diagonally()
print(f'Área do retângulo: {ret.diagonally():.2f}')


# Triângulo Quadrado Test
tri_ret = triangle()
tri_ret.read_sides()
ret.right_triangle(tri_ret)
