import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load and prepare data
df = pd.read_csv("formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f4f6f8",
        "padding": "30px",
    },
    children=[
        html.H1(
            "Soul Foods – Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "10px",
            },
        ),

        html.P(
            "Explore Pink Morsel sales trends before and after the price increase on 15 January 2021.",
            style={
                "textAlign": "center",
                "color": "#555",
                "marginBottom": "30px",
                "fontSize": "16px",
            },
        ),

        html.Div(
            style={
                "width": "60%",
                "margin": "0 auto",
                "backgroundColor": "#ffffff",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 10px rgba(0, 0, 0, 0.1)",
                "marginBottom": "30px",
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "bold",
                        "marginBottom": "10px",
                        "display": "block",
                    },
                ),
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All Regions", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"textAlign": "center"},
                    inputStyle={"marginRight": "6px", "marginLeft": "20px"},
                ),
            ],
        ),

        html.Div(
            style={
                "width": "90%",
                "margin": "0 auto",
                "backgroundColor": "#ffffff",
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 10px rgba(0, 0, 0, 0.1)",
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ],
        ),
    ],
)

# Callback to update graph
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        labels={
            "Date": "Date",
            "Sales": "Total Sales",
        },
    )

    # Add price increase marker
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
        font=dict(color="red"),
    )

    fig.update_layout(
        title="Pink Morsel Sales Over Time",
        legend_title_text="Region",
        margin=dict(l=40, r=40, t=60, b=40),
    )

    return fig


# Run server
if __name__ == "__main__":
    app.run(debug=True)
