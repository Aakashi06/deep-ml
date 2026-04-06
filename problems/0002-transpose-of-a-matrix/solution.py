def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    m = len(a)        # number of rows
    n = len(a[0])     # number of columns

    # create result matrix of shape (n, m)
    result = [[0 for _ in range(m)] for _ in range(n)]

    # fill the result using transpose logic
    for i in range(m):
        for j in range(n):
            result[j][i] = a[i][j]

    return result