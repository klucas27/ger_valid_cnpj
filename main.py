from files.tools import run_os

clear = run_os

def menu():
    lista_menu = {
        1: ["Validar CNPJ;"],
        2: ["Gerar CNPJ"],
    }

    for nm, vlr in lista_menu.items():
        print(f"{nm} --> {vlr[0]}")


if __name__ == "__main__":
    menu()
