#MAKING A TOP STOCKS PRICE PULLER
#Impoorting the libraries
import yfinance as yf

#Creating a pre defined stock names available in the both markets
glbl_tkrs = {
    "INDIA": {
        "RELIANCE.NS": "Reliance Industries Limited",
        "BHARTIARTL.NS": "Bharti Airtel Limited",
        "HDFCBANK.NS": "HDFC Bank Limited",
        "ICICIBANK.NS": "ICICI Bank Limited",
        "SBIN.NS": "State Bank of India",
        "TCS.NS": "Tata Consultancy Services Limited",
        "INFY.NS": "Infosys Limited",
        "BAJFINANCE.NS": "Bajaj Finance Limited",
        "LT.NS": "Larsen & Toubro Limited",
        "HINDUNILVR.NS": "Hindustan Unilever Limited",
    },
    "US": {
        "AAPL": "Apple Inc.",
        "NVDA": "NVIDIA Corporation",
        "MSFT": "Microsoft Corporation",
        "GOOGL": "Alphabet Inc. (Class A)",
        "AMZN": "Amazon.com, Inc.",
        "META": "Meta Platforms, Inc.",
        "AVGO": "Broadcom Inc.",
        "TSLA": "Tesla, Inc.",
        "LLY": "Eli Lilly and Company",
        "BRK-B": "Berkshire Hathaway Inc. (Class B)",
    },
}

#Creating the dictionary for time period

timeprds = {
    "1" : "1d",
    "5" : "5d",
    "10": "10d",
    "15": "15d",
    "20": "20d",
}

#taking the input from the user for region(
user = input("Which region?(India or US): ").strip().upper()
#taking the input from the user for time period
timeprd = input('How much of days?: ').strip()


#assigning the glbl_tkrs dict to the user for merging the stocks by using .get()
slctd_stk = glbl_tkrs.get(user)
days = timeprds.get(timeprd)

#using if/else statments to check valid inputs and printing!
if not slctd_stk or not days:
    print("invalid Region or days entered.")
else:
    tickers_list = list(slctd_stk.keys())
    data = yf.download(tickers_list, period=days)

    print(f"Closing Price: \n{data['Close']}")
    print(f"High: \n{data['High']}")
    print(f"Low: \n{data['Low']}")
    print(f"Volume: \n{data['Volume']}")

print("Thanks for using our service.")
user_input = input("Do you wanna explore another stock?(yes/no): ").strip().lower()

#making a loop
while user_input == "yes":
    user = input("Which region?(India or US): ").strip().upper()
    timeprd = input("How much of days?: ").strip()

    slctd_stk = glbl_tkrs.get(user)
    days = timeprds.get(timeprd)

    if not slctd_stk or not days:
        print("invalid Region or days entered.")
    else:
        tickers_list = list(slctd_stk.keys())
        data = yf.download(tickers_list, period=days)

        print(f"Closing Price: \n{data['Close']}")
        print(f"High: \n{data['High']}")
        print(f"Low: \n{data['Low']}")
        print(f"Volume: \n{data['Volume']}")

    user_input = input("Explore another? (yes/no): ").strip().lower()

print("Bye")