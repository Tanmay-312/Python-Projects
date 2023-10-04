while True:
    try:
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
        operator = input("Enter the operator you want to work with (+,-,*,/,//): ")

        if operator == '+':
            print(num1 + num2)
        elif operator == '-':
            print(num1 - num2)
        elif operator == '*':
            print(num1 * num2)
        elif operator == '/':
            print(num1 / num2)
        elif operator == '//':
            print(num1 // num2)
        else:
            print("Entered operation not available !!")

        toCal = input("Want to continue calculating ? (Y/N): ")
        if toCal == 'N' or toCal == 'n':
            break

    except ValueError:
        print("You need to provide a number")

    except ZeroDivisionError:
        print("You cannot divide by 0")

    except Exception as e:
        print("Error occurred:- ", e)
