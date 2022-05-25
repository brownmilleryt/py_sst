from lib.pyLight import process_file
from lib.pyLight import process_folder
from lib.pyLight import is_valid_path



def szukanie(pdf_input, lista_wyrazow, pdf_output):
    for el in lista_wyrazow:
        if lista_wyrazow.index(el) > 0:
            process_file(input_file=pdf_output,
            output_file=pdf_output,
            action="Frame",
            search_str=el)
        else:
            process_file(input_file=pdf_input,
            output_file=pdf_output,
            action="Frame",
            search_str=el)


def lista_wyrazow(database):
    is_valid_path(database)
    with open(database, "r") as dane:
        return [line.strip() for line in dane.readlines()]

szukanie("D-05.03.04.pdf",lista_wyrazow("dane.txt"),"output/D-05.03.04_add.pdf")

