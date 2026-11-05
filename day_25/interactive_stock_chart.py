import yfinance as yf
import plotly.graph_objects as go

ticker = "5341.KL"
data = yf.download(
    ticker,
    period = "1y",
    interval = "1d",
    auto_adjust = True
)

print(data.tail())

fig = go.Figure(
    data = [
        go.Candlestick(
            x = data.index,
            open = data["Open"]["5341.KL"],
            high = data["High"]["5341.KL"],
            low = data["Low"]["5341.KL"],
            close = data["Close"]["5341.KL"],
            name = "5341.KL",
        )
    ]
)

fig.update_layout(
    title = "5341.KL Stock Price",
    xaxis_title = "Date",
    yaxis_title = "Price (MYR)",
    xaxis_rangeslider_visible = True,
)

fig.show()
