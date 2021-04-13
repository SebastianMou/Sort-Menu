import colorama
from colorama import Fore
colorama.init(autoreset=True)

def menu():
    dec()
    print("\n########################################################################")
    print("#                1. Ordenamiento Burbuja                               #")
    print("#                2. Ordenamiento Shell                                 #")
    print("#                3. Ordenamiento Radix                                 #")
    print("#                4. Ordenamiento por mezcla (Merge sort)               #")
    print("#                5. Ordenamiento por distribución (BucketSort )        #")
    print("#                6. Ordenamiento por montículos (Heapsort)             #")
    print("#                7. Ordenamiento rápido (Quicksort)                    #")
    print("#                8. consultar arreglo puchale 8                        #")
    print("#                0. exit                                               #")
    print("########################################################################")
    option = int(input(": "))

    if option == 1:
        print("1 ")
        menu()

    elif option == 2:
        print("2")
        menu()

    elif option == 3:
        print("3")
        menu()

    elif option == 4:
        print("4")
        menu()

    elif option == 5:
        print("5")
        menu()

    elif option == 6:
        print("6")
        menu()

    elif option == 7:
        print("7")
        menu()

    elif option == 8:
        print("8")
        menu()

    elif option == 0:
        print("$$$$$$$                       $$ | ")
        print("$$  __$$                      $$ | ")
        print("$$ |  $$ |$$    $$   $$$$$$   $$ | ")
        print("$$$$$$$  |$$ |  $$ |$$  __$$  $$ | ")
        print("$$  __$$  $$ |  $$ |$$$$$$$$ | __| ")
        print("$$ |  $$ |$$ |  $$ |$$   ____|     ")
        print("$$$$$$$  | $$$$$$$$ | $$$$$$$  $$  ")
        print(" _______/   ____$$ |  _______| __| ")
        print("          $$    $$ |               ")
        print("           $$$$$$  |               ")
        print("            ______/                ")
        exit()


def dec():
    print(f"{Fore.GREEN}\n $$$$$$\                       $$\           $$\      $$\                               ")
    print(f"{Fore.GREEN}$$  __$$\                      $$ |          $$$\    $$$ |                              ")
    print(f"{Fore.GREEN}$$ /  \__| $$$$$$\   $$$$$$\ $$$$$$\         $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\   $$\ ")
    print(f"{Fore.GREEN}\$$$$$$\  $$  __$$\ $$  __$$  _$$  _|        $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ |  $$ |")
    print(f"{Fore.GREEN} \____$$\ $$ /  $$ |$$ |  \__| $$ |          $$ \$$$  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |")
    print(f"{Fore.GREEN}$$\   $$ |$$ |  $$ |$$ |       $$ |$$\       $$ |\$  /$$ |$$   ____|$$ |  $$ |$$ |  $$ |")
    print(f"{Fore.GREEN}\$$$$$$  |\$$$$$$  |$$ |       \$$$$  |      $$ | \_/ $$ |\$$$$$$$\ $$ |  $$ |\$$$$$$  |")
    print(f"{Fore.GREEN} \______/  \______/ \__|        \____/       \__|     \__| \_______|\__|  \__| \______/ .py")

menu()

