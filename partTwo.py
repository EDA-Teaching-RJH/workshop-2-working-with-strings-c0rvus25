import math  

def main():
    A = float(input("Input A: "))
    B = float(input("Input B: "))
    C = pythag(A,B)
    print("Hypotenuse that you're after is: " , C)
def pythag(A,B):
    return math.sqrt(A**2 + B**2)

main()
