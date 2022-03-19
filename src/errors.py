# error handling


class MissingArguments(Exception):
    """Exception raised when incorrect nuber arguments are supplied to function

    Attributes:
        args -- arguments
    """

    def __init__(self, args, expected="> 0"):
        self.args = args
        self.expected = expected

    def __str__(self):
        return f"Length of args {len(self.args)} !{self.expected}"


class VectorLengthMismatch(Exception):
    """Exception raised when vectors are not of the same size during dot product calculations.

    Attributes:
        arr1 -- vector 1
        arr2 -- vector 2
    """

    def __init__(self, arr1, arr2, message="Vector length mismatch. Must be equal"):
        self.arr1 = arr1
        self.arr2 = arr2
        self.message = message

    #        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} {len(self.arr1)} != {len(self.arr2)}"


class MatrixDimensionError(Exception):
    """Exception raised when matrix is not 2x2.

    Attributes:
        mx - matrix
    """

    def __init__(self, mx, dimension="2x2"):
        self.mx = mx
        self.message = f"Matrix must have dimension {dimension}."
        self.dimensions = [len(mx), len(mx[0])]

    def __str__(self):

        return f"{self.message} {self.dimensions[0]}x{self.dimensions[1]} != 2x2"
