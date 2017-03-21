def EditDist(a, b):
    # Stopping condition
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    delta = 1 if a[-1] != b[-1] else 0
    return min( EditDist(a[:-1], b[:-1]) + delta,
                EditDist(a, b[:-1]) + 1,
                EditDist(a[:-1], b) + 1)


def LevenshteinMethod(x, y):
    matrix = []
    for i in range(len(x)+1):
        matrix.append([0] * (len(y)+1)) # initialize the matrix with zeros
    for i in range((len(x) +1 )):
        matrix[i][0] = i # Fill in the first column with acscending integers
    for j in range((len(y) + 1)):
        matrix[0][j] = j # Fill in the first row with ascending integers
    for i in range(1, len(x) + 1 ):
        for j in range(1, len(y) + 1):
            # Fill in other elements
            delta = 1 if x[i-1] != y[j-1] else 0
            distDiag = matrix[i-1][j-1] + delta
            distVer = matrix[i-1][j] + 1
            distHor = matrix[i][j-1] + 1
            matrix[i][j] = min(distDiag, distHor, distVer)
    # print(matrix)
    return matrix[-1][-1]

if __name__ == '__main__':
    import datetime as d
    #st = d.datetime.now()
    #print(EditDist("Shakespeare", "shake spear"))
    #print((d.datetime.now() - st).total_seconds())
    st = d.datetime.now()
    print(LevenshteinMethod("Shakespeare", "shake spear"))
    print((d.datetime.now() - st).total_seconds())
