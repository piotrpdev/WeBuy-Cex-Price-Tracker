import requests
from cex.const import *

class CexClient(object):

    def __init__(self, searchItem):
        self.API_URL = 'https://wss2.cex.ie.webuy.io/v3/boxes?q={}&firstRecord=1&count=50&sortOrder=desc'.format(searchItem)

    def specific(self):
        print('')
        print(self.API_URL)
        mPop = requests.get(self.API_URL) #Get the product information
        mPop = mPop.json() #Convert it to JSON
        mPop = mPop['response']['data']['boxes']
        return mPop

    def displayResults(self, products):
        for i in range(len(products)): #Prints the item(s)
            print("=---------------------------------------=")
            print("Product Name:        "+str(products[i][D['bN']]))
            print("Category:            "+str(products[i][D['cN']]))
            print("CeX Sells For:       "+"€"+str(products[i][D['sP']]))
            print("Cex Buys For Cash:   "+"€"+str(products[i][D['cP']]))
            print("CeX Buys For Voucher:"+"€"+str(products[i][D['eP']]))
            print("=---------------------------------------=")
            print('')
        pass
