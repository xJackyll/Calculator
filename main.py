#!/usr/bin/env python3

def main():

    print("====================================")
    print("Operazioni disponibili:")
    print("1) Somma")
    print("2) Sottrazione")
    print("3) Divisione")
    print("4) Moltiplicazione")
    print("5) Potenza")
    print("------------------------------------")
    print("0) Esci")
    print("====================================")

    while True:
        try:
            operand = input("Immetti l'operazione che vuoi eseguire: ")
            num1 = float(input("Immetti il primo numero: "))
            num2 = float(input("Immetti il secondo numero: "))


            match operand:
                case "0":
                    print("Bye Bye")
                    exit()
                case "1":
                    sum = num1 + num2
                case "2":
                    sum = num1 - num2
                case "3":
                    sum = num1 / num2
                case "4":
                    sum = num1 * num2
                case "5":
                    sum = num1 ** num2

            print(f"The result is {sum}")

        except Exception as e:
            print(e)






# Execute
if __name__ == '__main__':
    main()
