r1 = r2 = c1 = c2 = dA = dB = 0
A = []
B = []
Add = []
Sub = []
Mul = []

def create_matrices():
    global A, r1, c1, r2, c2, B
    A = []
    B = []  
    r1 = int(input("Enter the row number of matrix A: "))
    c1 = int(input("Enter the column number of matrix A: "))
    for i in range(r1):
        row = []  
        for j in range(c1):
            val = int(input(f"Enter element A[{i+1}][{j+1}]: "))
            row.append(val)
        A.append(row)  
    print("\nMatrix A is:")
    for row in A:
        print(row)

    r2 = int(input("Enter the row number of matrix B: "))
    c2 = int(input("Enter the column number of matrix B: "))
    for i in range(r2):
        row = []  
        for j in range(c2):
            val = int(input(f"Enter element B[{i+1}][{j+1}]: "))
            row.append(val)
        B.append(row)  
    print("\nMatrix B is:")
    for row in B:
        print(row)

def addition():
    global A, r1, c1, r2, c2, B, Add
    Add = []
    if r1 == r2 and c1 == c2:      
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(A[i][j] + B[i][j])
            Add.append(row)
        for i in Add:
            print(i)
    else:
        print("Addition not possible (dimensions must match)")

def substraction():
    global A, r1, c1, r2, c2, B, Sub
    Sub = []
    if r1 == r2 and c1 == c2:      
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(A[i][j] - B[i][j])
            Sub.append(row)
        for i in Sub:
            print(i)
    else:
        print("Subtraction not possible (dimensions must match)")

def multiplication():
    global A, r1, c1, r2, c2, B, Mul
    Mul = []
    if c1 == r2:
        for i in range(r1):
            row = []
            for k in range(c2):
                s = 0
                for j in range(c1):
                    s += A[i][j] * B[j][k]
                row.append(s)
            Mul.append(row)
        for i in Mul:
            print(i)
    else:
        print("Multiplication not possible (column of A should match row of B)")

def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1)**c) * matrix[0][c] * determinant(minor, n-1)
        return det
def inverse(matrix,n):
    d = determinant(matrix, n)
    if d == 0:
        print("Inverse not possible (determinant = 0)")
        return
    cof = []
    for i in range(n):
        cof_row = []
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cof_row.append(((-1)**(i+j)) * determinant(minor, n-1))
        cof.append(cof_row)
    adj = [[cof[j][i] for j in range(n)] for i in range(n)]
    inv = [[adj[i][j] / d for j in range(n)] for i in range(n)]
    print("\nInverse of the matrix is:")
    for row in inv:
        print(row)
choice = ''
print("Welcome to the Matrix Calculator created by slacker_deb")
while choice != '7':
    choice = input("""
Press 1 to Create/Recreate two Matrices
Press 2 to Add existing Matrices
Press 3 to Substract existing Matrices
Press 4 to Multiply existing Matrices
Press 5 to find Determinant of existing Matrices
Press 6 to find Inverse of existing Matrices
Press 7 to Exit
Enter your Choice: """)
    if choice == '1':
        create_matrices()
    elif choice == '2':
        print("Addition of A and B is: \n")
        addition()
    elif choice == '3':
        print("Subtraction of A and B is: \n")
        substraction()
    elif choice == '4':
        print("Multiplication of A and B is: \n")
        multiplication()
    elif choice == '5':
        if (r1 == c1 or r2 == c2):   
            c = input("Which matrix would you like to calculate the determinant (A/B): ").upper()
            if c == 'A' and r1 == c1:
                matrix = A
                n = r1
            elif c == 'B' and r2 == c2:
                matrix = B
                n = r2
            else:
                print("Wrong Input or Non-square matrix")
                continue
            Ans = determinant(matrix, n)
            print("Determinant Value is:", Ans)
        else:
            print("Determinant is not possible (matrix must be square)")
    elif choice == '6':
        if (r1 == c1 or r2 == c2):   
            c = input("Which matrix would you like to calculate the Inverse (A/B): ").upper()
            if c == 'A' and r1 == c1:
                matrix = A
                n = r1
            elif c == 'B' and r2 == c2:
                matrix = B
                n = r2
            else:
                print("Wrong Input or Non-square matrix")
                continue
            inverse(matrix, n)
        else:
            print("Determinant is not possible (matrix must be square)")
    elif choice == '7':
        print("Exiting...")
    else:
        print("Wrong option chosen. Please choose a correct option from below")
