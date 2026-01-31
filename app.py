import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the processed data
df = pd.read_csv("formatted_sales.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Highlight the price increase date
fig.add_shape(
    type="line",
    x0="2021-01-15",
    x1="2021-01-15",
    y0=0,
    y1=1,
    xref="x",
    yref="paper",
    line=dict(color="red", dash="dash"),
)

fig.add_annotation(
    x="2021-01-15",
    y=1,
    xref="x",
    yref="paper",
    text="Price Increase (15 Jan 2021)",
    showarrow=False,
    yanchor="bottom",
    font=dict(color="red")
)

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods – Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),
        dcc.Graph(figure=fig)
    ]
)

# Run server
if __name__ == "__main__":
    app.run(debug=True)
