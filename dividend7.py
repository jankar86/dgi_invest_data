def plot_data(data, key, title, yaxis_title, show_mean=False, mean_text="", type="line"):
    # getattr(px, type) if type = 'line' is px.line
    fig = getattr(px, type)(y=data[key], x=data[key].index)
    # add a historical mean if specified
    if show_mean:
        fig.add_hline(data[key].mean(), line_dash="dot", annotation_text=mean_text)
    # set title and axis-titles
    fig.update_layout(
        title=title, 
        xaxis_title="Date",
        yaxis_title=yaxis_title,
        title_x = 0.5,
        showlegend=False
    )
    return fig
