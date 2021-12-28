import run_os
import re


def get_cnpj(cnpj_re, digit=False):
    cnpj = cnpj_re
    cnpj_ver = re.split(r"[\W]", cnpj)
    pass_cnpj = re.sub(r"[\W]", '', cnpj)
    if len(cnpj_ver) != 5:
        return "Invalid CNPJ[1]"

    for ver in cnpj_ver:
        if not ver.isdecimal():
            return "Invalid CNPJ![2]"

    verify_numbers = [cnpj_ver[0] and cnpj_ver[4] != 2, cnpj_ver[1] and cnpj_ver[2] != 3, cnpj_ver[3] != 4]

    for pas in verify_numbers:
        if not pas:
            return "Invalid CNPJ![3]"

    if digit:
        return pass_cnpj
    else:
        return pass_cnpj[0:12]


def calc_first_dig(cnpj):
    cnpj = get_cnpj(cnpj)
    cont = 5
    soma_num = 0
    for num in cnpj:
        if cont < 2:
            cont = 9
        soma_num += (int(num) * cont)
        cont -= 1

    first_number = 11 - (soma_num % 11)

    if first_number > 9:
        first_number = 0

    return cnpj + str(first_number)


def calc_second_dig(cnpj):
    cnpj = calc_first_dig(cnpj)
    cont = 6
    soma_num = 0
    for num in cnpj:
        if cont < 2:
            cont = 9
        soma_num += (int(num) * cont)
        cont -= 1

    first_number = 11 - (soma_num % 11)

    if first_number > 9:
        first_number = 0

    return cnpj + str(first_number)


def run_valid():
    run_os.os_run("cls")
    cnpj = input("Insert CNPJ: ")
    cnpj_rec = get_cnpj(cnpj, digit=True)
    cnpj_calc = calc_second_dig(cnpj)
    if cnpj_rec == cnpj_calc:
        return "CNPJ Valid!"
    else:
        return "CNPJ Invalid!"


if __name__ == '__main__':
    run_valid()
