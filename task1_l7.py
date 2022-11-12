class Matrix:
    def __init__(self, name, m):
        self.name = name
        self.m = m

    def __str__(self):
        return f" Матрица {self.name} =\n" \
               f"| {self.m[0][0]} | {self.m[0][1]} | {self.m[0][2]} |\n" \
               f"| {self.m[1][0]} | {self.m[1][1]} | {self.m[1][2]} |\n" \
               f"| {self.m[2][0]} | {self.m[2][1]} | {self.m[2][2]} |\n" \

    def __add__(self, other):
        
        result_m = list()
        for m in range(len(self.m)):
            result_m.append(list())

        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                result_m[i].append(self.m[i][j] + other.m[i][j])
                
        return f" Результирующая матрица =\n" \
               f"| {result_m[0][0]} | {result_m[0][1]} | {result_m[0][2]} |\n" \
               f"| {result_m[1][0]} | {result_m[1][1]} | {result_m[1][2]} |\n" \
               f"| {result_m[2][0]} | {result_m[2][1]} | {result_m[2][2]} |\n" \

a_list = [[31, 22, 38], [37, 43, 21], [51, 46, 12]]
b_list = [[34, 12, 12], [13, 49, 31], [42, 36, 23]]

a = Matrix("A", a_list)
b = Matrix("B", b_list)

print(a)
print(b)
print(a + b)


