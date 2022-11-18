import math


def monthly_payment():
    pass


def no_of_months():
    b = float(input("Enter the balance of the credit card:\n"))
    apr = float(input("Enter the apr % of the credit:\n"))
    p = float(input("What is the monthly payment you can make:\n"))
    i = apr / 365
    n = (-1/30)*((math.log10(1+((b/p)*(1-(math.pow(1+i, 30))))))/math.log10(i+1))
    print(f'No of months required to pay of credit card bill is:\n{round(n)}')


def main():
    print("-------------------------")
    print("----Enter your choice----")
    print("-------------------------")
    print("1 - Calculate number of months")
    print("2 - Calculate monthly payment")
    print("3 - Exit\n")
    choice = int(input())
    if choice == 1:
        no_of_months()
    elif choice == 2:
        monthly_payment()
    elif choice == 3:
        exit(0)
    else:
        print("Wrong choice, Try Again....\n")


if __name__ == "__main__":
    main()
