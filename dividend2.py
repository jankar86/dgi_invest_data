# save for 5 hours
@st.cache(ttl=60*60*5)
def load_data(ticker):
    # load data
    profile = fa.profile(ticker, FA_API_KEY)
    key_metrics_annually = fa.key_metrics(ticker, FA_API_KEY, period="annual")
    stock_data = fa.stock_data(ticker, period="5y", interval="1d")
    financial_ratios_annually = fa.financial_ratios(ticker, FA_API_KEY, period="annual")
    income_statement_annually = fa.income_statement(ticker, FA_API_KEY, period="annual")
    try:
        dividends = fa.stock_dividend(ticker, FA_API_KEY)
        dividends.index = pd.to_datetime(dividends.index)
        dividends = dividends["adjDividend"].resample("1Y").sum().sort_index()
    except:
        dividends = pd.Series(0, name="Dividends")

    # return information of interest
    return {
        "stock_closings": stock_data["close"].sort_index(),
        "historical_PE": key_metrics_annually.loc["peRatio"].sort_index(),
        "payout_ratio": financial_ratios_annually.loc["payoutRatio"].sort_index(),
        "dividend_yield": 100*financial_ratios_annually.loc["dividendYield"].sort_index(),
        "cash_per_share": key_metrics_annually.loc["cashPerShare"].sort_index(),
        "debt_to_equity": key_metrics_annually.loc["debtToEquity"].sort_index(),
        "free_cash_flow_per_share": key_metrics_annually.loc["freeCashFlowPerShare"].sort_index(),
        "dividends": dividends,
        "earnings_per_share": income_statement_annually.loc["eps"].sort_index(),
        "info": profile.iloc[:, 0]
    }
