rows = int(input("please enter the number of rows:  "))
columns = int(input("please enter the number of columns:  "))
for i in range(1, rows+1):
    for j in range(1, columns+1):
        c = i*j
        print("{:2d} ".format(c), end='')
    print("\n")
