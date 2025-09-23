number = int(input("Enter a number: "))#number initialized to recieve input from user

def evenorodd(number):
    #if loop to check if number is even or odd
    if number % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
def square(number):
    #function to print square of number
    print("Square is", number**2)
def cube(number):
    #function to print cube of number
    print("Cube is", number**3)

def main():
    #main function to call other functions
    evenorodd(number)
    square(number)
    cube(number)

main()#calling main function