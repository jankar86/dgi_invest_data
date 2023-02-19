# second column, graph and graph settings

# empty() functions as a placeholder,
# that is, after I later add items to this placeholder,
# the items will appear here before elements that are
# added later. 
graph_placeholder = overview_columns[1].empty()
# The reason a placeholder is used is because I would like
# to show the graph options beneath the graph, but they
# need to be set first so that their returned values can
# be used when constructing the graph

# here I add an empty graph to avoid the elements from
# jumping around when updating the graph
graph_placeholder.plotly_chart(go.Figure(), use_container_width=True)

# options that will dictate the graph:

# radio buttons for what time window to display the stock price
time_window_key = overview_columns[1].radio("Time window", TIME_DIFFS.keys(), index=len(TIME_DIFFS)-1, horizontal=True)
# select the value from the key, i.e. the pd.DateOffset
time_window = TIME_DIFFS[time_window_key]

# slider to select the moving average to display in the graph
moving_average = overview_columns[1].slider("Moving average", min_value=2, max_value=500, value=30)

# Use above to construct the graph:

# show the graph
fig = get_price_data_fig(stock_data["stock_closings"], moving_average, time_window, time_window_key, currency)
# add to placeholder to be displayed before options
graph_placeholder.plotly_chart(fig, use_container_width=True)
