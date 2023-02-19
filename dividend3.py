# create 3 columns and add a text_input
# in the second/center column
ticker = st.columns(3)[1].text_input("Ticker")

if ticker != "":
    stock_data = load_data(ticker)
