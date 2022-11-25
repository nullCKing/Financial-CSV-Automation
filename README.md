# Financial-CSV-Automation

A program that automates a variety of CSV creation tasks for stock market research and/or algorithmic trading.


## Requirements
csvtickerlist==0.0.2
customtkinter==4.6.3
pandas==1.5.0
XlsxWriter==3.0.3
yahoofinancials==1.6
yfinance==0.1.86


## Option 1: Create detailed ticker files
**This creates individual files for each ticker symbol**
![detailedfiles](https://user-images.githubusercontent.com/113802864/204017327-463f5b83-c170-4859-871c-99717fba2c55.gif)


Each file contains:

- Date, opening price, closing price, daily high/low, daily volume, dividend issues, stock splits.


## Option 2: Create complete list of tickers CSV
**This creates one file of all currently active tickers**
![fullcsv](https://user-images.githubusercontent.com/113802864/204018308-dca30b04-d3d9-4c1d-9344-00501312a86d.gif)


The file contains:

- Symbol, name, last price, net change, % change, market cap, country, IPO year, volume, sector, industry


## Option 3: Create CSV financial report of tickers
**This creates one file, based upon start and endpoints, containing detailed financial information**

The file contains:

- Book value, EV to EBITDA, Price to Book, Market Cap, Price Sales, Previous Close, Outstanding Shares
