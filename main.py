from src.operations import Matrix, dot, oneVector, multiply, inverse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print(f"Data input modes:\n1. CSV")
    choice = int(input())
    if choice == 1:
        fileName = input("File name: ")
        df = pd.read_csv(fileName)

    else:
        return

    col1 = df.columns[0]
    col2 = df.columns[1]
    xVals = df[col1]
    yVals = df[col2]
    dataLen = len(xVals)
    plt.scatter(xVals, yVals)
    plt.xlabel(col1)
    plt.ylabel(col2)

    onesVec = oneVector(dataLen)
    A = Matrix([[dot(onesVec, onesVec), dot(onesVec, xVals)],
                [dot(xVals, onesVec), dot(xVals, xVals)]])
    C = Matrix([[dot(onesVec, yVals)], [dot(xVals, yVals)]])

    B = inverse(A) * C
    yIntercept = B[0][0]
    slope = B[1][0]
    print(f"y = {slope}x + {yIntercept}")
    xRegressionValues = [i for i in range(xVals.sort_values().iloc[-1])]
    yRegressionValues = [i*slope + yIntercept for i in xRegressionValues]

    plt.plot(xRegressionValues, yRegressionValues,
             label=f"y = {slope}x + {yIntercept}")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
