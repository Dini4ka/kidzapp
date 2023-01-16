import xlsxwriter
from data import *


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


Make_Table()
