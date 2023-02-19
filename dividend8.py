# horizontal line
st.markdown("---")

# define all plots
div_fig = plot_data(
    stock_data,
    key="dividends",
    title="Dividends",
    yaxis_title=currency,
    type="bar"
)
pe_fig = plot_data(
    stock_data, 
    key="historical_PE", 
    title="Historical Price-to-Earnings (P/E) Ratio", 
    yaxis_title="P/E", 
    show_mean=True, 
    mean_text="Average Historical P/E",
)
yield_fig = plot_data(
    stock_data, 
    key="dividend_yield", 
    title="Dividend Yield", 
    yaxis_title="Percent %", 
    show_mean=True, 
    mean_text="Average Historical Dividend Yield",
    type="bar"
)
payout_fig = plot_data(
    stock_data, 
    key="payout_ratio", 
    title="Payout Ratio", 
    yaxis_title="Payout Ratio",
    type="bar",
    show_mean=True,
    mean_text="Average Historical Payout Ratio"
)
cps_fig = plot_data(
    stock_data, 
    key="cash_per_share", 
    title="Cash/Share", 
    yaxis_title=currency,
    type="bar"
)
fcf_fig = plot_data(
    stock_data, 
    key="free_cash_flow_per_share", 
    title="Free Cash Flow/Share", 
    yaxis_title=currency,
    type="bar"
)
eps_fig = plot_data(
    stock_data, 
    key="earnings_per_share", 
    title="Earnings/Share", 
    yaxis_title=currency,
    type="bar"
)
dte_fig = plot_data(
    stock_data,
    key="debt_to_equity",
    title="Debt-to-equity",
    yaxis_title="Debt/Equity"   
)

# align plots side by side
combos = [(div_fig, pe_fig), (eps_fig, yield_fig), (payout_fig, cps_fig), (fcf_fig, dte_fig)]
for (fig1, fig2) in combos:
    cols = st.columns(2)
    if fig1 is not None:
        cols[0].plotly_chart(fig1, use_container_width=True)
    if fig2 is not None:
        cols[1].plotly_chart(fig2, use_container_width=True)
