
# Made by RazerMoon - Based on CEX-API by teamplz and hiddencipher

import requests #Used to get the html data
from cex import * #Gets all the files from the cex folder
import id_list


class Check(): #Check the information for specified products and prints it
    def __init__(self):
        
        for id in id_list.id_list: #Gets the information for every id
            Cex = CexClient(id) #Sends the id
            products = Cex.specific() #Returns the JSON data of a product
            Cex.displayResults(products) #Prints the wanted data in a nice looking format into console

Check()
