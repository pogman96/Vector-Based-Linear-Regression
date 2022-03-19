from src.errors import MissingArguments, VectorLengthMismatch, MatrixDimensionError


class Matrix:
    def __init__(self, mx):
        self.matrix = mx

    def __mul__(self, other: "Matrix"):
        return multiply(self.matrix, other)

    def __rmul__(self, other: "Matrix"):
        return multiply(other, self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.matrix])


def checkMatrix(*mats):
    for mat in mats:
        if len(mat) == 0:
            raise MissingArguments(mat, expected="> 0")


def oneVector(count):
    return [1 for i in range(count)]


def getDimensions(mx: Matrix):
    return [len(mx), len(mx[0])]


def inverse(mx: Matrix):
    if getDimensions(mx) != [2, 2]:
        raise MatrixDimensionError(mx)

    determinant = mx[0][0] * mx[1][1] - mx[0][1] * mx[1][0]

    for i in range(len(mx)):
        for j in range(len(mx[0])):
            mx[i][j] = mx[i][j] / determinant

    return Matrix([[mx[1][1], -mx[0][1]], [-mx[1][0], mx[0][0]]])


def multiply(mx1: Matrix, mx2: Matrix):
    """Mulitiplies two matrices together. Not communitative, order matters.

    Arugments:
        mx1 -- first matrix to be multiplied
        mx2 -- second matrix"""

    checkMatrix(mx1, mx2)

    resultMx = [[0 for i in range(len(mx2[0]))] for i in range(len(mx1))]
    for i in range(len(mx1)):
        for j in range(len(mx2[0])):
            for k in range(len(mx2)):
                resultMx[i][j] += mx1[i][k] * mx2[k][j]
    return Matrix(resultMx)


def dot(arr1, arr2):
    """Computes dot product of two vectors.

    Arguments:
        arr1 -- vector
        arr2 -- vector"""

    total = 0
    if len(arr1) != len(arr2):
        raise VectorLengthMismatch(arr1, arr2)

    for i in range(len(arr1)):
        total += arr1[i] * arr2[i]

    return total


if __name__ == "__main__":
    pass

