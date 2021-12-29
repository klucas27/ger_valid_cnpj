from configs_scri import validador
import random
from configs_scri import run_os


def run_gerador():
    run_os.os_run("cls")
    numbers = [str(random.randint(10, 99)), str(random.randint(100, 999)), str(random.randint(100, 999)),
               str(random.randint(1000, 9999))]

    new_cnpj = numbers[0]+numbers[1]+numbers[2]+numbers[3]

    cont = 5
    soma = 0

    for pas in new_cnpj:
        if cont < 2:
            cont = 9
        soma += (int(pas) * cont)
        cont -= 1

    first_number = 11 - (soma % 11)

    if first_number > 10:
        first_number = 0

    cont = 6
    soma = 0

    for pas in str(new_cnpj)+str(first_number):
        if cont < 2:
            cont = 9
        soma += (int(pas) * cont)
        cont -= 1

    second_number = 11 - (soma % 11)

    if second_number > 10:
        second_number = 0

    return f"{numbers[0]}.{numbers[1]}.{numbers[2]}/{numbers[3]}-{first_number}{second_number}"


if __name__ == '__main__':
    print(run_gerador())
