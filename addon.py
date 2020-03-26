#Adds any products in id_list.py to the sheets if it isn't there

from cex import *
import id_list
import gspread
from gspread_formatting import *
import time

def update_list(sheet):
    print('-------------------')
    print('Checking sheet for missing products...')
    print('')
    updated = 0
    cooldown = 0

    def titleFmt():
        fmt = cellFormat(textFormat=textFormat(bold=True, foregroundColor=color(0, 0, 0), fontSize=12), horizontalAlignment='CENTER', backgroundColor=color(1, 1, 1))
        return fmt

    def pricesFmt():
        fmt = cellFormat(textFormat=textFormat(bold=True, foregroundColor=color(0, 0, 0), fontSize=10), horizontalAlignment='LEFT', backgroundColor=color(1, 1, 1))
        return fmt
    
    def consoleFmt():
        fmt = cellFormat(textFormat=textFormat(bold=True, foregroundColor=color(0, 0, 0), fontSize=11, italic=True), numberFormat=numberFormat('TEXT', ""), horizontalAlignment='CENTER', backgroundColor=color(1, 1, 1))
        return fmt

    for id in id_list.id_list:
        Cex = CexClient(id)
        products = Cex.specific() #Returns the JSON data of a product
        try:
            cell = sheet.find(id) #Looks for cell with matching contents
        except gspread.exceptions.CellNotFound:
            print('{} was not found! Adding...'.format(products[0][D['bN']]))
            updated = updated+1
            cooldown = cooldown+1

            if cooldown > 8:
                print('Cooling down for 100 seconds...')
                cooldown = 0
                time.sleep(120)

            cols = sheet.range(2, 1, sheet.row_count, 1)
            try:
                emptyrow = max([cell.row for cell in cols if cell.value]) + 1
            except ValueError:
                emptyrow = 2
            
            sheet.update_cell(emptyrow, 1, products[0][D['bN']])
            format_cell_range(sheet, 'A{}:A{}'.format(emptyrow+1, emptyrow+1), consoleFmt())
            sheet.update_cell(emptyrow+1, 1, id)
            sheet.update_cell(emptyrow+2, 1, products[0][D['cN']])
            sheet.update_cell(emptyrow+3, 1, 'CeX Sells For')
            sheet.update_cell(emptyrow+4, 1, 'CeX Buys For Cash')
            sheet.update_cell(emptyrow+5, 1, 'CeX Buys For Voucher') 
                   
            format_cell_range(sheet, 'A{}:A{}'.format(emptyrow, emptyrow), titleFmt())
            format_cell_range(sheet, 'A{}:A{}'.format(emptyrow+2, emptyrow+2), consoleFmt())
            format_cell_range(sheet, 'A{}:A{}'.format(emptyrow+3, emptyrow+3), pricesFmt())
            format_cell_range(sheet, 'A{}:A{}'.format(emptyrow+4, emptyrow+4), pricesFmt())
            format_cell_range(sheet, 'A{}:A{}'.format(emptyrow+5, emptyrow+5), pricesFmt())
    
    if updated < 1:
        pass
    else:
        print('')

    print('{} Missing product(s) added!'.format(updated))
    print('-------------------')
    print('')
