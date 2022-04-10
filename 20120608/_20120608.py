def printMatrix(A):
    for row in A:
        for element in row:
            if element - int(element) == 0:
                print(int(element), end = " ")
            else:
                print(element, end = " ")
        print()

def Gauss_elimination(A):
    nrow = len(A)
    ncol = len(A[0])
    zeros = 1 #Cờ báo cột đang xét có == 0 hay không
    pivotRow = -1
    for col in range(ncol - 1):
        pivotRow += 1
        if pivotRow >= nrow and zeros == 0:
            break
        #Kiểm tra cột trước đó có bằng 0 hay không
        if zeros == 1 and col != 0:
            pivotRow -= 1
        #Trường hợp phần tử (có cùng chỉ số dòng và cột) != 0
        if A[pivotRow][col] != 0:
            zeros = 0 #Cột này != 0
            #Chia tất cả các phần tử trong dòng col cho phần tử != 0 đầu tiên của dòng
            pivot = A[pivotRow][col]
            for i in range(col, ncol):
                A[pivotRow][i] /= pivot
            #Xét tất cả các phần tử cùng cột col phía dưới
            #Phần tử nào != 0 thì trừ dòng đó cho <hệ số> * dòng col
            for i in range(nrow):
                if i != pivotRow and A[i][col] != 0:
                    factor = A[i][col]
                    for j in range(col, ncol):
                        A[i][j] -= factor * A[pivotRow][j]
        #Trường hợp phần tử (có cùng chỉ số dòng và cột) == 0
        else:
            index = pivotRow
            for i in range(index + 1, nrow):
                #Thực hiện hoán đổi dòng có phần tử cùng cột col mà != 0 đầu tiên
                if i != pivotRow and A[i][col] != 0:
                    zeros = 0
                    A[pivotRow], A[i] = A[i], A[pivotRow]
                    index = i
                    break
            #Trường hợp tìm ra được dòng có phần tử cùng cột col mà != 0 và đã swap
            if index != pivotRow:
                pivot = A[pivotRow][col]
                for i in range(col, ncol):
                    A[pivotRow][i] /= pivot
                for i in range(nrow):
                    if (i < pivotRow or i >= index + 1) and A[i][col] != 0:
                        factor = A[i][col]
                        for j in range(col, ncol):
                            A[i][j] -= factor * A[pivotRow][j]
            else: zeros = 1

def back_substitution(A):
    nrow = len(A)
    ncol = len(A[0])
    result = [0] * (ncol - 1)
    #Kiểm tra hệ có vô nghiệm hay không
    count = 0 #Biến đếm số dòng khác 0
    index = 0 #Chỉ số cột có phần tử != 0 đầu tiên trong dòng
    for i in range(nrow - 1, -1, -1):
       for j in range(ncol):
           if A[i][j] != 0 and j != ncol - 1:
               count += 1
               break
           elif A[i][j] != 0:
               index = ncol - 1
       if index == ncol - 1:
           print("Hệ phương trình vô nghiệm!")
           return
    #Trường hợp hệ có nghiệm duy nhất
    if count == ncol - 1:
        for i in range(ncol - 1):
            result[i] = A[i][ncol - 1];
        #Xuất giá trị nghiệm ra màn hình
        print("Hệ phương trình có nghiệm duy nhất: ")
        for i in range(ncol - 1):
            if result[i] - int(result[i]) == 0:
                print("x" + str(i + 1) + " = " + str(int(result[i])))
            else:
                print("x" + str(i + 1) + " = " + str(result[i]))
    #Trường hợp hệ có vô số nghiệm
    elif count < ncol - 1:
        used = [0] * (ncol - 1) #Mảng đánh dấu 
        #Tìm nghiệm tự do
        for i in range(count - 1, -1, -1):
            first = 0 #Đánh dấu nghiệm phụ thuộc vào các nghiệm tự do
            solve = i #Biến lưu vị trí của nghiệm phụ thuộc
            for j in range(i, ncol - 1):
                if A[i][j] != 0 and first == 0:
                    solve = j
                    first = 1
                elif first != 0 and used[j] == 0:
                    result[j] = "a" + str(j + 1)
                    used[j] = 1
            if A[i][ncol - 1] - int(A[i][ncol - 1]) == 0:                     
                result[solve] = str(int(A[i][ncol - 1]))
                used[solve] = 1
            else:
                result[solve] = str(A[i][ncol - 1])
                used[solve] = 1
            for j in range(solve + 1, ncol - 1):
                if A[i][j] > 0:
                    if A[i][j] != 1:
                        if A[i][j] - int(A[i][j]) == 0:
                            result[solve] += "-" + str(int(A[i][j])) + str(result[j])
                        else:
                            result[solve] += "-" + str(A[i][j]) + str(result[j])
                    else:
                        result[solve] += "-" + str(result[j])
                elif A[i][j] < 0:
                    if A[i][j] != -1:
                        if A[i][j] - int(A[i][j]) == 0:
                            result[solve] += "+" + str(int(abs(A[i][j]))) + str(result[j])
                        else:
                            result[solve] += "+" + str(abs(A[i][j])) + str(result[j])
                    else:
                        result[solve] += "+" + str(result[j])
        #Xuất giá trị nghiệm ra màn hình
        print("Hệ phương trình có vô số nghiệm có dạng: ")
        for i in range(ncol - 1):
            print("x" + str(i + 1) + " = " + str(result[i]))
        
    

                 
A = [[0, 0, -2, 0, 7, 12], [2, 4, -10, 6, 12, 28], [2, 4, -5, 6, -5, -1]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
C = [[1, 1, 0, 1, 0], [0, 1, 1, 2, 0], [1, 0, 1, 1, 0]]
D = [[1, 1, 1, 2], [1, 1, 2, 3], [1, 2, 3, 1]]
E = [[1, 2, 0, 2, 6], [3, 5, -1, 6, 17], [2, 4, 1, 2, 12], [2, 0, -7, 11, 7]]
F = [[1, 0, 2, 3, 4], [2, 0, -1, 5, 3], [3, 0, 4, 6, -2], [4, 0, 2, 7, 0]]
G = [[1, 0, 0, 3], [2, 0, 0, 5], [3, 0, 0, 6], [4, 0, 0, 7]]
H = [[1, 7, 1, 3, 0], [1, 7, -1, -2, -2], [2, 14,2, 7, 0], [6, 42, 3, 13, -3]]
I = [[1, 2, 0, 0, 3, 0, 7], [0, 0, 1, 0, 6, 0, -5], [0, 0, 0, 1, -2, 4, 5]]
J = [[-1, 1, -1, 0, 1], [1, 1, 2, 0, 7]]
K = [[-1, 1, -1, 0], [1, 1, 2, 0], [2, 1, 2, 3], [1, 5, 2, 4], [2, 2, 4, 0], [3, 3, 6, 0]]
L = [[1,0,2,0,-1,0,1], [0,1,0,2,0,-1,-2], [-2,0,-3,0,1,0,-1], [0,-2,0,-3,0,1,1]]
M = [[3,6,6,0,9,3],[-1,-2,-2,1,-4,1],[-3,-6,-6,2,-11,1]]
N = [[1, -1, -2, -3],[2,-1,1,1],[1,1,1,4]]


print("Ma trận D ban đầu")
printMatrix(D)
Gauss_elimination(D)
print("Ma trận D sau khi đưa về dạng bậc thang rút gọn")
printMatrix(D)
back_substitution(D)

print("Ma trận E ban đầu")
printMatrix(E)
Gauss_elimination(E)
print("Ma trận E sau khi đưa về dạng bậc thang rút gọn")
printMatrix(E)
back_substitution(E)

print("Ma trận H ban đầu")
printMatrix(H)
Gauss_elimination(H)
print("Ma trận H sau khi đưa về dạng bậc thang rút gọn")
printMatrix(H)
back_substitution(H)

print("Ma trận A ban đầu")
printMatrix(A)
Gauss_elimination(A)
print("Ma trận A sau khi đưa về dạng bậc thang rút gọn")
printMatrix(A)
back_substitution(A)


#printMatrix(I)
#back_substitution(I)


print("Ma trận J ban đầu")
printMatrix(J)
Gauss_elimination(J)
print("Ma trận J sau khi đưa về dạng bậc thang rút gọn")
printMatrix(J)
back_substitution(J)

#print("Ma trận K ban đầu")
#printMatrix(K)
#Gauss_elimination(K)
#print("Ma trận K sau khi đưa về dạng bậc thang rút gọn")
#printMatrix(K)
#back_substitution(K)

#print("Ma trận L ban đầu")
#printMatrix(L)
#Gauss_elimination(L)
#print("Ma trận L sau khi đưa về dạng bậc thang rút gọn")
#printMatrix(L)
#back_substitution(L)

print("Ma trận M ban đầu")
printMatrix(M)
Gauss_elimination(M)
print("Ma trận M sau khi đưa về dạng bậc thang rút gọn")
printMatrix(M)
back_substitution(M)

#print("Ma trận N ban đầu")
#printMatrix(N)
#Gauss_elimination(N)
#print("Ma trận N sau khi đưa về dạng bậc thang rút gọn")
#printMatrix(N)
#back_substitution(N)