from configs_scri import run_os
from configs_scri import validador
from configs_scri import gerador
import time


def menu():
    while True:
        run_os.os_run("cls")
        lista_menu = {
            1: ["Validar CNPJ;", "print(validador.run_valid())"],
            2: ["Gerar CNPJ", "print(gerador.run_gerador())"],
        }

        for nm, vlr in lista_menu.items():
            print(f"{nm} --> {vlr[0]}")

        option = input("select option: ")

        try:
            option = int(option)
        except ValueError:
            print("Error[main-1]")
            exit()

        try:
            try:
                exec(lista_menu.get(int(option))[1])
                time.sleep(5)
            except IndexError:
                print("Error[main-2]")
                time.sleep(2)
        except TypeError:
            print("Error[main-3]")
            time.sleep(2)


if __name__ == "__main__":
    menu()
