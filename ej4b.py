ORDEN = 100

def sumar_matrices(A, B):
    C = [[0]*ORDEN for _ in range(ORDEN)]
    for i in range(ORDEN):
        for j in range(ORDEN):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Ejemplo de uso
A = [[0]*ORDEN for _ in range(ORDEN)]
B = [[0]*ORDEN for _ in range(ORDEN)]

# Cargamos algunos valores (rala => la mayoría son ceros)
A[0][0] = 5
B[0][0] = 3
B[10][20] = 7

C = sumar_matrices(A, B)

print(C[0][0])    # 8
print(C[10][20])  # 7
