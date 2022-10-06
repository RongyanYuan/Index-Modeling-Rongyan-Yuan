import datetime as dt
import pandas as pd
import numpy as np

# Input database:
stock_prices = pd.read_csv("data_sources/stock_prices.csv")  # file path might need to be modified accordingly


# Setting dates as form of datetime
date_index = 0
Stock_date = []
for dates in stock_prices["Date"]:
    Stock_date += [dt.date(day=int(dates[0:2]), month=int(dates[3:5]), year=int(dates[6:]))]
    date_index += 1
stock_prices["Date"] = pd.Series(data=Stock_date)

# Setting Column of Dates as the index of the stock_prices pandas dataframe
stock_prices.set_index("Date", inplace=True)

# Global variables:
max_cap_stock_weight = 0.5  # the weight of the stock with the highest stock cap
seq_cap_stock_weight = 0.25  # the weight of the sotcks with the second and third stock cap


# Helper functions:
def select_stocks(stocks: pd.Series) -> list:
    """
    :param stocks: series of stock at specific time
    :return: list of stocks with the highest cap values in order: the first element has the highest cap value
    """
    stocks_copy = stocks.copy()
    selected_stocks = []
    i = 0
    while i < 3:
        highest_cap_stock = stocks_copy.idxmax()
        selected_stocks += [highest_cap_stock]
        stocks_copy.drop(labels=[highest_cap_stock], inplace=True)
        i += 1
    return selected_stocks

def require_date_for(ele_date: int) -> str:
    """
    :param ele_date: an element of date
    :return string of correct form of date
    """

    if ele_date >= 10:
        return str(ele_date)
    else:
        return '0' + str(ele_date)


class IndexModel:
    def __init__(self) -> None:
        self.out_index_data = []

    def calc_index_level(self, start_date: dt.date, end_date: dt.date) -> None:
        start_date_format = require_date_for(start_date.day) + "/" + require_date_for(
            start_date.month) + "/" + require_date_for(start_date.year)
        moving_index = 100  # index_level at initial date set up
        index_output = pd.DataFrame(np.array([moving_index]), index=[start_date_format], columns=["index_level"])
        index_output.index.names = ["Date"]  # assign date index name

        # Base values set up
        portfolio_stock = select_stocks(stock_prices.loc[stock_prices.index[
            1]])  # determine stocks in portfolio based on info last day of month before start_date
        previous_date = start_date  # date variable set up
        previous_stock_prices = stock_prices.loc[previous_date]  # setup of base stock prices in a month

        for business_date in stock_prices.index[3:]:
            # Obtain the stock with the highest, second, third cap value at last day of previous month
            highest_stock = portfolio_stock[0]
            second_stock = portfolio_stock[1]
            third_stock = portfolio_stock[2]

            # Calculate return rate of each stock selected and the total return rate with assigned weight
            Return_one = (stock_prices.loc[business_date][highest_stock] - previous_stock_prices[highest_stock]) / \
                         previous_stock_prices[highest_stock]
            Return_two = (stock_prices.loc[business_date][second_stock] - previous_stock_prices[second_stock]) / \
                         previous_stock_prices[second_stock]
            Return_three = (stock_prices.loc[business_date][third_stock] - previous_stock_prices[third_stock]) / \
                           previous_stock_prices[third_stock]
            Total_return = Return_one * max_cap_stock_weight + Return_two * seq_cap_stock_weight + Return_three * seq_cap_stock_weight
            Today_index = (1 + Total_return) * moving_index

            # Update calculated value to our pandas dataframe
            Date_format = require_date_for(business_date.day) + "/" + require_date_for(
                business_date.month) + "/" + require_date_for(business_date.year)
            index_output.loc[Date_format] = np.array(Today_index)

            # Determine of previous day is the last day of previous month and update information
            if business_date.month != previous_date.month:
                portfolio_stock = select_stocks(stock_prices.loc[previous_date])
                moving_index = Today_index
                previous_stock_prices = stock_prices.loc[business_date]
            previous_date = business_date

            # Determine if current business day is the end date required and end loop
            if business_date == end_date:
                break
        self.out_index_data = index_output  # assign result

    def export_values(self, file_name: str) -> None:
        self.out_index_data.to_csv(file_name)  # export dataframe to a csv file
