import yfinance as yf 
import pandas as pd
import tkinter
import customtkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from yahoofinancials import YahooFinancials
import xlsxwriter
from csvtickerlist import GetCSVFile

def GetDataFolder():
	return filedialog.askdirectory(title = 'Select Folder')

def GetFileLocation():
    return filedialog.askopenfilename()

def CreateDependency():
    folder = GetDataFolder()
    GetCSVFile(folder, 10)
    #GetCSVFile is imported from my PyPi package, csvtickerlist.
	#arg1 (folder) represents the output folder
	#arg2 (10) represents the seconds to wait before closing the web driver.
	#10 seconds is recommended, but increase this when facing connectivity issues.

def TickerInput(startTick, endTick, timeFrame):
    messagebox.showinfo(title="Info", message="Please select the tickers file for detailed conversions.")
    tickerFile = GetFileLocation()
    messagebox.showinfo(title="Info", message="Please select the output folder.")
    folder = GetDataFolder()
    tickers=pd.read_csv(tickerFile)
    oldSymbolList = list(tickers['Symbol']) #Generate a list of every ticker symbol from the selected file.
    newSymbolList = []
    taperedSymbolList = []
    i = 0 #Iterator for newSymbolList
    j = 0 #Iterator for taperedSymbolList
    t = 0 #Used for determining distance between start position and current position.
    startpos = 0
    print(startTick)
    print(endTick)
    #rows = len(tickers.axes[0])
    #We must remove tickers with special characters, they are not able to properly pull ticker data.
    for i in range(0, (len(oldSymbolList) - 1)):
        errorFlag = 0
        if (type(oldSymbolList[i]) is str):
            for char in oldSymbolList[i]:
                if ((char == '/') or (char == '\\') or (char == '^')):
                    errorFlag = 1
            if (errorFlag != 1):
                newSymbolList.append(oldSymbolList[i])
    
    #This loop determines the start point and then defines this starting position for our array definition parameters.
    for j in range(0, (len(newSymbolList) - 1)):
        
        if (newSymbolList[j] == startTick):
            taperedSymbolList.append(newSymbolList[j])
            t = 1
            startpos = j
            print(taperedSymbolList)
            break

    #We generate a new list using our start and end points (i.e. Start: AAPL to AMZN)
    while (newSymbolList[startpos + t] != endTick):
        taperedSymbolList.append(newSymbolList[startpos + t])
        t += 1

    taperedSymbolList.append(endTick)
    print(taperedSymbolList)

    for i in range (0,(len(taperedSymbolList))):
        tick=taperedSymbolList[i]
        print(tick)
        detailedTicker=folder+"\{}.csv".format(tick)  
        file=open(detailedTicker,'w',newline="")
        ticker=yf.Ticker(tick)
        history=ticker.history(period=timeFrame)
        #timeFrame is determined by the timeframe dropdown in the GUI.
        file.write(history.to_csv())
        file.close()
    #Each ticker symol has its own highly detailed file generated.


def financials_fetcher(ticker):
    yahoo_financials=YahooFinancials(ticker)
    key1=yahoo_financials.get_key_statistics_data()
    key2=yahoo_financials.get_summary_data()
    key3=yahoo_financials.get_financial_stmts('annual', 'income')
    bookVal=key1[ticker]['bookValue']
    EV2EBITDA=key1[ticker]['enterpriseToEbitda']
    price2Book=key1[ticker]['priceToBook']
    marketCap=(key2[ticker]['marketCap'])//1000000
    priceToSales=(key2[ticker]['priceToSalesTrailing12Months'])
    previousClose=(key2[ticker]['previousClose'])
    sharesOutstanding=key1[ticker]['sharesOutstanding']

    #Market Cap. is set to display in millions. Will add functionality to change this to
    #a different amount of division.

    if bookVal is None:
        bookVal = "N/A"
    if EV2EBITDA is None:
        EV2EBITDA = "N/A"
    if price2Book is None:
        price2Book = "N/A"
    if marketCap is None:
        marketCap = "N/A"
    if priceToSales is None:
        priceToSales = "N/A"
    if previousClose is None:
        previousClose = "N/A"
    if sharesOutstanding is None:
        sharesOutstanding = "N/A"

    dictFinance = []
    dictFinance = [ticker, bookVal, EV2EBITDA, price2Book, marketCap, priceToSales, previousClose, sharesOutstanding]
    
    print(dictFinance)

    return dictFinance

def GetAllFinancials(startTick, endTick):
    
    tickerFile = GetFileLocation()

    tickers=pd.read_csv(tickerFile)
    tickers_list = list(tickers['Symbol'])
    oldSymbolList = list(tickers['Symbol'])
    newSymbolList = []
    taperedSymbolList = []
    i = 0
    j = 0
    t = 0
    startpos = 0
    print(startTick)
    print(endTick)
    #rows = len(tickers.axes[0])
    #We must remove tickers with special characters, they are not able to properly pull ticker data.
    for i in range(0, (len(oldSymbolList) - 1)):
        errorFlag = 0
        if (type(oldSymbolList[i]) is str):
            for char in oldSymbolList[i]:
                if ((char == '/') or (char == '\\') or (char == '^')):
                    errorFlag = 1
            if (errorFlag != 1):
                newSymbolList.append(oldSymbolList[i])
    
    for j in range(0, (len(newSymbolList) - 1)):
        
        if (newSymbolList[j] == startTick):
            taperedSymbolList.append(newSymbolList[j])
            t = 1
            startpos = j
            print(taperedSymbolList)
            break

    while (newSymbolList[startpos + t] != endTick):
        taperedSymbolList.append(newSymbolList[startpos + t])
        t += 1

    taperedSymbolList.append(endTick)
    print(taperedSymbolList)

    dialog = customtkinter.CTkInputDialog(master=None, text="Name your new excel file:", title="Enter filename")
    filename = dialog.get_input()
    tkinter.messagebox.showinfo("Information","Input the folder to save the excel file to.")
    filepath = askdirectory()
    # create xlsx workbook and worksheet
    print(filename)
    print(filepath)
    combinedfile = (filepath + '/' + filename + '.xlsx')
    outWorkbook = xlsxwriter.Workbook(combinedfile)
    outSheet = outWorkbook.add_worksheet()

    # write column headers
    outSheet.write("A1", "Ticker")
    outSheet.write("B1", "Book Value")
    outSheet.write("C1", "EV to EBITDA")
    outSheet.write("D1", "Price to Book")
    outSheet.write("E1", "Market Cap")
    outSheet.write("F1", "Price to Sales")
    outSheet.write("G1", "Previous Close")
    outSheet.write("H1", "Outstanding Shares")
    outSheet.set_column('A:H', 20)

    row = 2
    for i in range(0,(len(taperedSymbolList))):
        data =  financials_fetcher(taperedSymbolList[i])
        outSheet.write_row(f"A{row}", data)
        row += 1
    
    outWorkbook.close()
    
    