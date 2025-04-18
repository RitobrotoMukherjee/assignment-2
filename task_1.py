print("\tFind even & odd from your given input\n")

try:
    num = int(input("Enter a number: "))

    if (num % 2 == 0):
        print("%d is an even number" %(num))
    else:
        print(f"{num} is an odd number")
except ValueError:
    print("\nOnly integer number is accepted")
    print("Please run the program again to get correct output")
finally:
    print("\nOdd & Even program ends here!!")