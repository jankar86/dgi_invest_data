def get_price_data_fig(srs, moving_average, time_window, time_window_key, currency):
    # create moving average
    ma = srs.rolling(window=moving_average).mean().dropna()
    # only in time window
    start = (pd.to_datetime("today").floor("D") - time_window)
    srs = srs.loc[start:]
    ma = ma.loc[start:]
    # create figures for normal and moving average
    fig1 = px.line(y=srs, x=srs.index)
    fig1.update_traces(line_color="blue", name="Price", showlegend=True)
    fig2 = px.line(y=ma, x=ma.index)
    fig2.update_traces(line_color="orange", name=f"Moving average price ({moving_average})", showlegend=True)
    # combine and add layout
    fig = go.Figure(data = fig1.data + fig2.data)
    fig.update_layout(
        title=f"Price data last {time_window_key}",
        xaxis_title="Date",
        yaxis_title=currency,
        title_x = 0.5,
        # align labels top-left, side-by-side
        legend=dict(y=1.1, x=0, orientation="h"),
        showlegend=True
    )
    return fig
