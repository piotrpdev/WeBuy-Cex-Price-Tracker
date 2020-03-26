
import id_list
#from cex import *

def dupeChecker():
    dupes = 0
    for id in range(len(id_list.id_list)):
        id = id_list.id_list[id]
        matching = [s for s in id_list.id_list if id in s]
        if len(matching) > 1:
            dupes = dupes+1
            print(matching)
            print(len(matching))

    if not dupes > 0:
       pass
    else:
        raise ValueError('Duplicates Found!')

#def printAll():
    #for id in id_list.id_list:
        #Cex = CexClient(id)
        #product = Cex.specific() #Returns the JSON data of a product
        #print(str(product[0][D['bN']]))

#dupeChecker() #Checks for duplicates in id_list.py
#printAll() #Prints the title of each id

#print(len(id_list.id_list))

#for element in range(len(easy)): #Takes a long list and prints the id's assuming they are on the end of the sentence
#    res = easy[element].split()
#    id = res[-1]
#    print(id)

