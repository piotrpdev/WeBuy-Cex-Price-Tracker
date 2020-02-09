# WeBuy Cex Price Tracker [![Build Status](https://img.shields.io/badge/license-MIT-green)

A python script that gets the prices of certain CeX products and uploads them to google sheets. Based on [CEX-API](https://github.com/teamplz/CEX-API)

## Getting Started

The script is currently able to get the information of multiple products using their id's. Put in the id's of the games you want and you will get their prices.

### Prerequisites

You will need the latest version of [Python](https://www.python.org/downloads/), [OAuth2Client](https://oauth2client.readthedocs.io/en/latest/#supported-python-versions), [Requests](https://pypi.org/project/requests/), 
[GSpread](https://pypi.org/project/gspread/) and [GSpread-Formatting](https://pypi.org/project/gspread-formatting/)

### Installing

After downloading the files and prerequisites you can enter the id's of the products you want to check into the [id_list.py](id_list.py) and run [main.py](main.py).

Running the script as is should return the information for some products. The addon.update_list() function will always check for new id's and ungenerated google sheet products.

![Getting the id](captures/getting_id.gif)
![The id's](captures/id_list.png)
![Final result](captures/sheet.gif)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgement

Big thanks to [Sothclaws](https://github.com/Southclaws) for his [CeX Go Client](https://github.com/Southclaws/go-cex) and [teamplz](https://github.com/teamplz) for his [CEX-API](https://github.com/teamplz/CEX-API). They really helped me out and saved me a lot of time!
