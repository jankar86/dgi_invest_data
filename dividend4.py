info = stock_data["info"]
currency = info["currency"]

# Title
st.title(f"{info['companyName']} ({info['symbol']})")

# Add changes for different periods
close = stock_data["stock_closings"]
latest_price = close.iloc[-1]
# should all be displayed on the same row
change_columns = st.columns(len(TIME_DIFFS))
today = pd.to_datetime("today").floor("D")
for i, (name, difference) in enumerate(TIME_DIFFS.items()):
    # go back to the date <difference> ago
    date = (today - difference)
    # if there is no data back then, then use the earliest
    if date < close.index[0]:
        date = close.index[0]
    # if no match, get the date closest to it back in time, e.g. weekend to friday
    previous_price = close.iloc[close.index.get_loc(date,method='ffill')]
    # calculate change in percent
    change = 100*(latest_price - previous_price) / previous_price
    # show red if negative, green if positive
    color = "red" if change < 0 else "green"

    # color can be displayed as :red[this will be red] in markdown
    change_columns[i].markdown(f"{name}: :{color}[{round(change, 2)}%]")
