
# RazerMoon - 02/2020 - V0.5 - NOT FULLY WOKRING - non-asyncronous - Soup & Selenium

# Can access normal site data but messes up when trying to access something after a comment, only way to fix is to keep switching between the different find() functions.

from bs4 import BeautifulSoup, Comment #Used to parse through HTML and prettify
from selenium import webdriver #Used to generate browser sessions
import time
import wx
import wx.lib.buttons as buttons  
import config

class Config:
    if config.webdriver['type'] == 2:
        print('Using Chrome driver')
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        options = ChromeOptions() #variable for simplicity
        options.add_argument("--headless") #adds headless parameter to options
        options.add_argument("--log-level=3")
        web_driver_path = config.webdriver['location']
        driver = webdriver.Chrome(executable_path=web_driver_path, options=options, service_log_path='NUL')
    else:
        print('Using Firefox driver')
        from selenium.webdriver.firefox.options import Options as FirefoxOptions #Options to enable headless mode, can potentially reduce lag / wait time
        options = FirefoxOptions() #variable for simplicity
        options.add_argument('--headless') #adds headless parameter to options
        web_driver_path = config.webdriver['location']
        driver = webdriver.Firefox(executable_path=web_driver_path, options=options, service_log_path='NUL')

class Tracker():

    def __init__(self, *args, **kw):
    
        url = 'https://ie.webuy.com/product-detail?id=5030917285752&categoryName=playstation4-games&superCatName=gaming&title=call-of-duty-modern-warfare-%282019%29' #Url that gets checked
        #url = 'https://ie.webuy.com/product-detail?id=0711719386070&categoryName=playstation4-software&superCatName=gaming&title=god-of-war-%282018%29-no-dlc'
    
        errorcount = 0
    
        #while (errorcount < 3):
        try:
            driver = Config.driver
            #driver = webdriver.Chrome(executable_path=r'C:\Users\games\AppData\Local\Programs\Microsoft VS Code\chromedriver.exe', options=options2)
            driver.get(url)
            time.sleep(1) # VERY IMPORTANT Delay needed for value to load before parsing, TRACKER WILL NOT WORK WITHOUT THIS! If there are issues, increasing this value might help
            html = BeautifulSoup(driver.page_source, 'lxml')
            errorcount = errorcount + 1
            result = html.find('tr', {'valign':'top'}).find('td', {'id':'Asellprice'}).text
            #result = html.find('div', {'class':'productDescriptionArea'}).find('h2').text
            if not result: #raises an exception if the result string is empty
                raise ValueError()
            print(result) #switching between these two sometimes fixes things, should try putting one of them in the except
            driver.quit()
            #break
        except AttributeError:
            print('Attribute Error! (html.find probably returned a NoneType)')
            driver.quit()
        except ValueError:
            print('Value Error! (Resulting text is probably empty)')
            driver.quit()

Tracker()


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

