matrix=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
suma_linii=[]
suma_coloane=[0,0,0,0,0]
diagonala_principala=[]
diagonala_secundara=[]
for i in range(len(matrix)):
    print(matrix[i])
    suma_linii.append(sum(matrix[i]))
    for j in range(len(matrix[0])):
        suma_coloane[i]+=matrix[j][i]
        if i==j:
            diagonala_principala.append(matrix[i][j])
        if i+j==len(matrix)-1:
            diagonala_secundara.append(matrix[i][j])
            
for i in range(len(matrix)):
    print(f"Suma pe linia {i} este {suma_linii[i]} ")
for i in range(len(matrix)):
     print(f"Suma pe coloana {i} este {suma_coloane[i]}")
print(f"Elementele diagonalei principale sunt: {diagonala_principala}")
print(f"Elementele diagonalei secundare sunt: {diagonala_secundara}")
