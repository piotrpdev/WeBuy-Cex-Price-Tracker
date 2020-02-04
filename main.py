
# Made by RazerMoon - Based on CEX-API by teamplz and hiddencipher

import requests #Used to get the html data
from cex import * #Gets all the files from the cex folder
import wx #Used for the GUI
import wx.lib.buttons as buttons #GUI element


class Check(): #Check the information for specified products and prints it
    def __init__(self):
        id_list = ['045496900397', '045496737955', '5030917285752'] #A list of id's for products
        
        for id in id_list: #Gets the information for every id
            Cex = CexClient(id) #Sends the id
            products = Cex.specific() #Returns the JSON data of a product
            Cex.displayResults(products) #Prints the wanted data in a nice looking format into console


#class HelloFrame(wx.Frame):
#    """
#    A Frame that says Hello World
#    """
#
#    def __init__(self, *args, **kw):
#        # ensure the parent's __init__ is called
#        super(HelloFrame, self).__init__(*args, **kw, size=(400, 300), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
#
#        # create a panel in the frame
#        panel = wx.Panel(self)
#
#        #self.t1 = wx.TextCtrl(panel)
#
#        #self.boldtext='default'
#
#        #self.st = wx.StaticText(panel, label=self.boldtext, pos=(0, 30))
#        #font = self.st.GetFont()
#        #font.PointSize += 10
#        #font = font.Bold()
#        #self.st.SetFont(font)
#
#        #self.Bind(wx.EVT_TEXT, self.changed, self.t1)
#
#        btn2 = buttons.GenButton(panel, -1, "Hello World!", (50, 100))
#
#    #def changed(self, event):
#        #updated = self.t1.GetValue()
#        #self.boldtext = updated
#        #self.st.SetLabel(self.boldtext)  
#
#
#
#if __name__ == '__main__':
#    # When this module is run (not imported) then create the app, the
#    # frame, show it, and start the event loop.
#    app = wx.App()
#    frm = HelloFrame(None, title='Cex Price Tracker')
#    frm.Centre()
#    frm.Show()
#    app.MainLoop()

