from files.tools import run_os
# from .files.tools import configs_val


def menu():

    run_os.os_run("cls")
    lista_menu = {
        1: ["Validar CNPJ;", "print(configs_val)"],
        2: ["Gerar CNPJ"],
    }

    for nm, vlr in lista_menu.items():
        print(f"{nm} --> {vlr[0]}")

    option = input("select option: ")

    exec(lista_menu.get(int(option))[1])


if __name__ == "__main__":
    menu()
