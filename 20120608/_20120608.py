def Gauss_elimination(A):
    nrow = len(A)
    ncol = len(A[0])
    zeros = 1 #Cờ báo cột đang xét có == 0 hay không
    for col in range(ncol - 1):
        pivotRow = col
        if zeros == 1 and col != 0:
            pivotRow = col - 1
        if pivotRow >= nrow:
            pivotRow = nrow - 1
        #Trường hợp phần tử có cùng chỉ số dòng và cột != 0
        if A[pivotRow][col] != 0:
            zeros = 0 #Cột này != 0
            #Chia tất cả các phần tử trong dòng col cho phần tử != 0 đầu tiên của dòng
            pivot = A[pivotRow][col]
            for i in range(col, ncol):
                A[pivotRow][i] /= pivot
            #Xét tất cả các phần tử cùng cột col phía dưới
            #Phần tử nào != 0 thì trừ dòng đó cho <hệ số> * dòng col
            for i in range(pivotRow + 1, nrow):
                if A[i][col] != 0:
                    factor = A[i][col]
                    for j in range(col, ncol):
                        A[i][j] -= factor * A[pivotRow][j]
        #Trường hợp phần tử (có cùng chỉ số dòng và cột) == 0
        else:
            index = pivotRow
            for i in range(pivotRow + 1, nrow):
                #Thực hiện hoán đổi dòng có phần tử cùng cột col mà != 0 đầu tiên
                if A[i][col] != 0:
                    zeros = 0
                    A[pivotRow], A[i] = A[i], A[pivotRow]
                    index = i
                    break
            #Trường hợp tìm ra được dòng có phần tử cùng cột col mà != 0 và đã swap
            if index != pivotRow:
                pivot = A[pivotRow][col]
                for i in range(col, ncol):
                    A[pivotRow][i] /= pivot
                for i in range(index + 1, nrow):
                    if A[i][col] != 0:
                        factor = A[i][col]
                        for j in range(col, ncol):
                            A[i][j] -= factor * A[pivotRow][j]
            else: zeros = 1


def back_substitution(A):
    nrow = len(A)
    ncol = len(A[0])
    result = [0] * (ncol - 1)
    Gauss_elimination(A)
    #Kiểm tra hệ có vô nghiệm hay không
    index = 0
    for i in range(nrow - 1, -1, -1):
       for j in range(ncol):
           if A[i][j] != 0 and j != ncol - 1:
               break
           elif A[i][j] != 0:
               index = ncol - 1
           if index == ncol - 1:
               print("Hệ phương trình vô nghiệm!")
               return
    #Trường hợp số ẩn nhỏ hơn hoặc bằng số phương trình 
    if nrow >= ncol - 1:
        for i in range(ncol - 2, -1, -1):
            
            #Trường hợp hệ có nghiệm duy nhất
            sum = 0
            for j in range(ncol - 2, i, -1):
                sum += A[i][j] * result[j]
            result[i] = A[i][ncol - 1] - sum
    #Trường hợp số ẩn lớn số phương trình 
    else:        
        for i in range(nrow - 1, -1, -1):
            for j in range(ncol - 2, i, -1):
                result[i] -= A[i][j] * result[j]
    #Xuất giá trị nghiệm ra màn hình
    print("Hệ phương trình có nghiệm: ")
    for i in range(nrow):
        print("x" + str(i + 1) + " = " + str(result[i]))

                 
A = [[0, 0, -2, 0, 7, 12], [2, 4, -10, 6, 12, 28], [2, 4, -5, 6, -5, -1]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
C = [[1, 1, 0, 1, 0], [0, 1, 1, 2, 0], [1, 0, 1, 1, 0]]
D = [[1, 1, 1, 2], [1, 1, 2, 3], [1, 2, 3, 1]]
E = [[1, 2, 0, 2, 6], [3, 5, -1, 6, 17], [2, 4, 1, 2, 12], [2, 0, -7, 11, 7]]
#print(B)
#Gauss_elimination(B)
#print(B)
#print(A)
#Gauss_elimination(A)
#print(A)
#print(C)
#Gauss_elimination(C)
#print(C)
#print(D)
#Gauss_elimination(D)
#print(D)
#print(E)
#Gauss_elimination(E)
#print(E)
back_substitution(E)