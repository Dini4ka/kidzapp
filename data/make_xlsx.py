import xlsxwriter
import openpyxl
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
from data.data import *
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


def make_note_in_offers(link, path_to_the_file):
    wb = openpyxl.load_workbook(path_to_the_file)
    ws = wb['offers']
    row = ws.max_row + 1
    item = parce(link)
    for col in range(len(main_fields)):
        key = ws[1][col].value
        ws.cell(row, col + 1).value = str(item[key])
    row = row + 1
    print('Written ' + item['slug'])
    wb.save(path_to_the_file)

Make_Table()
