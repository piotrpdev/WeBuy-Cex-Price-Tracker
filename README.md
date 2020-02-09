# WeBuy Cex Price Tracker

A python script that gets the prices of certain CeX products and uploads them to google sheets. Based on [CEX-API](https://github.com/teamplz/CEX-API)

## Getting Started

The script is currently able to get the information of multiple products using their id's. Put in the id's of the games you want and you will get their prices.

### Prerequisites

You will need the latest version of [Python](https://www.python.org/downloads/), [OAuth2Client](https://oauth2client.readthedocs.io/en/latest/#supported-python-versions),
[GSpread](https://pypi.org/project/gspread/) and [GSpread-Formatting](https://pypi.org/project/gspread-formatting/)

### Installing

After downloading the files and prerequisites you can enter the id's of the products you want to check into the [id_list.py](id_list.py) and run [main.py](main.py).

Running the script as is should return the information for some products. The addon.update_list() function will always check for new id's and ungenerated google sheet products.

![The id's](https://gyazo.com/54fc961fec4a59c665f408d6a20f29c9)
![Final result](https://gyazo.com/be40364620ee8c5e844c9530fd5e2e79)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgement

Big thanks to [Sothclaws](https://github.com/Southclaws) for his [CeX Go Client](https://github.com/Southclaws/go-cex) and [teamplz](https://github.com/teamplz) for his [CEX-API](https://github.com/teamplz/CEX-API). They really helped me out and saved me a lot of time!
