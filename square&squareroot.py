y = float(input("Enter Number: "))
x = int(input("Type_1 for square and Type_2 for squareroot: "))

def main():
    def square(n):
        return pow(n, 2)
    if x == 1:
        print("Square of number:", square(y))
    
main()

def main():
    def squareroot(c):
        return pow(c, 1/2)
    if x == 2:
        print("Squareroot of number:", squareroot(y))
        
main()