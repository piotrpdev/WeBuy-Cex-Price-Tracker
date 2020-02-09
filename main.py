
# Made by RazerMoon - Based on CEX-API by teamplz and hiddencipher
# https://docs.google.com/spreadsheets/d/1HeJvXZaNQ3oFkR2bRu0TrMu6MlGDgccCX3s0H4CSchw/edit#gid=0

import addon #imports the functions in addon.py used for adding new products and formatting to sheet
from oauth2client.service_account import ServiceAccountCredentials #Used to access google account
from datetime import date, timedelta #Used to get current day
from cex import * #Gets all the files from the cex folder
import gspread #Used to work with google sheets
import requests #Used to get the html data
import id_list #Gets all the product id's

#Uses creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope) #Replace client_secret.json with the credentials file
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("").sheet1

#Gets the date according to the format, change it if you like
today = date.today()
date1 = today.strftime("%d/%m/%Y")

class PriceUpdate(): #Updates the prices of the id's in id_list
    def __init__(self):

        print('-------------------')
        print('Checking prices...')
        print('')
        updated = 0
        cooldown = 0
        def getInfo(id): 
            Cex = CexClient(id) #Searches for product info
            products = Cex.specific() #Returns the JSON data of a product
            print('Updating prices for {}'.format(products[0][D['bN']]))
            sell = products[0][D['sP']] #Sets prices, refer to cex > const.py for details
            buycash = products[0][D['cP']] 
            buyvoucher =  products[0][D['eP']]

            cell = sheet.find(id) #Looks for the cell with a matching product name and sets the coordinates for it
            namerow = cell.row - 1
            namecol = cell.col

            def freeColumn(): # looks for empty column
                cols = sheet.range(namerow, namecol, namerow, sheet.col_count)
                maxcol = max([cell.col for cell in cols if cell.value]) + 1
                return maxcol

            maxcol = freeColumn() #Sets maxcol to a free column 

            return namerow, maxcol, sell, buycash, buyvoucher

        for id in id_list.id_list:
            updated = updated+1
            cooldown = cooldown+1
            if cooldown > 24:
                print('Cooling down for 100 seconds...')
                cooldown = 0
                time.sleep(100)

            namerow, maxcol, sell, buycash, buyvoucher = getInfo(id)

            sheet.update_cell(namerow, maxcol, date1)
            sheet.update_cell(namerow+3, maxcol, sell)
            sheet.update_cell(namerow+4, maxcol, buycash)
            sheet.update_cell(namerow+5, maxcol, buyvoucher)

        
        print('')
        print('{} Prices updated!'.format(updated))
        print('-------------------')

addon.update_list(sheet) # This need to be run on first launch and after adding new id's, just leave it on

PriceUpdate()

