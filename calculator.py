# I prefer to have anyother function up here before main. 
def do_the_math(first_number, second_number, operation):

    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "/":
        answer = first_number / second_number
    else:
     return print('Invalid operation, please try again...')

    return print(f"The answer is {answer}")

def main():
    
    first_number = input('Enter the first number:')
    second_number = input('Enter the second number:')

    # Inspired by `https://www.youtube.com/watch?v=u0402sx05yI`
    try:
       first_number = int(first_number)
       second_number = int(second_number)
    except ValueError:
        print("Invalid input, please try again...")

    else :
        operation = input("Choose the operation (+, -, /, *):")
        do_the_math(first_number, second_number,operation )
        
   
if __name__ == '__main__':
    main()
