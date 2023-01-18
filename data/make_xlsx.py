import xlsxwriter
import openpyxl
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
from data import *
from bot import *


def Make_Table():
    # Making xlsx file
    workbook = xlsxwriter.Workbook('data.xlsx')

    # offers
    offers = workbook.add_worksheet('offers')
    row = 0
    col = 0
    for field in main_fields:
        offers.write(row, col, field)
        col += 1

    # child offers
    child_offers = workbook.add_worksheet('child_offers')
    row = 0
    col = 0
    for field in child_fields:
        child_offers.write(row, col, field)
        col += 1

    # images
    images = workbook.add_worksheet('images')
    row = 0
    col = 0
    for field in image:
        images.write(row, col, field)
        col += 1

    workbook.close()


def make_note_offers(link, file):
    with open("../файл.txt", "r") as file:
        lines = [line.rstrip() for line in file]
    wb = openpyxl.load_workbook('data.xlsx')
    ws = wb['offers']
    row = 2
    for line in lines:
        try:
            item = parce(line)
        except Exception as ex:
            print(ex)
            continue
        print(row)
        try:
            for col in range(len(main_fields)):
                key = ws[1][col].value
                ws.cell(row, col + 1).value = str(item[key])
        except Exception as ex:
            print(ex)
            continue
        row = row + 1
        print('Written ' + item['slug'])
    wb.save('data.xlsx')


Make_Table()
