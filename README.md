# Cex Price Tracker

A python script that gets the prices of certain Cex products and uploads them to google sheets.

## Getting Started

The script currently works fine and has the option to get the title or price of the product. Just download the
files and run it in whatever you want, but make sure you get the prerequisites first!

### Prerequisites

As of me writing this, you will need [Selenium](https://selenium-python.readthedocs.io/installation.html), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [WxPython](https://wxpython.org/pages/downloads/index.html). Of course you also have to get the latest version of [Python](https://www.python.org/downloads/)

Selenium requires you to use either a Firefox or Chrome Webdriver, so make sure to get one of those [here](https://selenium-python.readthedocs.io/installation.html). You also need the actual web browser installed itself (Default is set to Firefox).

### Installing

After downloading the files and prerequisites go to the settings.txt file and enter in the location of your webdriver. 
Make sure to also select whichever webdriver you're using.

Running the script as is should return the price for the [following](https://ie.webuy.com/product-detail/?id=5030917285752&categoryName=playstation4-software&superCatName=gaming&title=call-of-duty-modern-warfare-%282019%29) product on the website.

![Getting the element](http://i.imgur.com/XMk6lRk.jpg)
![Printing the element](https://i.imgur.com/pUW3b5w.png)

## Release History
* 0.1.1
    * Added a [config.py](config.py) file to allow interchange between Chromedriver and Geckodriver
    * Discovered [CeX Go Client](https://github.com/Southclaws/go-cex) and [CEX-API](https://github.com/teamplz/CEX-API)
* 0.1.0
    * The first alpha release
    * FIX: Adding time.sleep(1) before the parsing has stopped the value only for only appearing some of the time
    * IN PROGRESS: Working on adding a graphical interface using [WxPython](https://wxpython.org/pages/downloads/index.html) for ease of use
    * IN PROGRESS: Working on a config file for webdriver selection 
* Pre-0.1.0
    * ISSUE: Only loads values some of the time, seems to be an issue with parsing
    * ISSUE: The load time for a value is around 10 seconds, if this is repeated for even a small amount of prices the wait time will be very large
    * Selenium has been chosen as it is able to load javascript elements however it is slower as expected and isn't asynchronous
    * Initial experimantation has shown that [requests_html](https://pypi.org/project/requests-html/) and [requests](https://pypi.org/project/requests/) cannot be used because of their inability to load javascript

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgement

Big thanks to [Sothclaws](https://github.com/Southclaws) for his [CeX Go Client](https://github.com/Southclaws/go-cex) and [teamplz](https://github.com/teamplz) for his [CEX-API](https://github.com/teamplz/CEX-API). They really helped me out and saved me a lot of time!
