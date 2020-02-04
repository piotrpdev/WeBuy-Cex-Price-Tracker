# WeBuy Cex Price Tracker

A python script that gets the prices of certain CeX products and uploads them to google sheets. Based on [CEX-API](https://github.com/teamplz/CEX-API)

## Getting Started

The script is currently able to get the information of multiple products using their id's. Just download the
files and run it in whatever you want, but make sure you get the prerequisites first!

### Prerequisites

As of writing this, you will need [WxPython](https://wxpython.org/pages/downloads/index.html) for the GUI. Of course you also have to get the latest version of [Python](https://www.python.org/downloads/)

### Installing

After downloading the files and prerequisites you can enter the id's of the products you want to check into the [id_list.py](id_list.py) and run [main.py](main.py).

Running the script as is should return the information for some products.

![Getting the element](https://i.imgur.com/6Rw6y5G.png)

## Release History

* 0.2.0
    * Deleted inneficient tracking code and rewrote the script to use [CEX-API](https://github.com/teamplz/CEX-API)
    * Script is now able to get the information of multiple products at the same time using their id's
* 0.1.1
    * Added a [config.py](config.py) file to allow interchange between Chromedriver and Geckodriver
    * IN PROGRESS: Discovered [CeX Go Client](https://github.com/Southclaws/go-cex) and [CEX-API](https://github.com/teamplz/CEX-API). Rewriting code to adapt those libraries to increase efficiency.
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
