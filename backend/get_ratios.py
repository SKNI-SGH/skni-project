import yahoo_fin.stock_info as si
import pandas as pd

tickers_list = pd.read_csv('tickers.csv')
tickers_list = tickers_list['Symbol'].to_list()[:1]


def get_stock_prices(tickers):

    for ticker in tickers:
        prices_df = si.get_data(ticker, start_date='01/01/2020', end_date='01/01/2021')

        # tutaj zwracamy ceny


def get_stock_finance(tickers):

    for ticker in tickers:
        finance_df = si.get_financials(ticker)

        quart_income_statement = finance_df['quarterly_income_statement']
        quart_balance_sheet = finance_df['quarterly_balance_sheet']
        quart_cash_flow = finance_df['quarterly_cash_flow']

        print(quart_income_statement, quart_balance_sheet, quart_cash_flow)


get_stock_finance(tickers_list)
