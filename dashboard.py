import sqlite3
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Connect to database
conn = sqlite3.connect('C:/Users/megha/OneDrive/StockMarketDashboard/database/stocks.db')
query = "SELECT * FROM daily_trends"
df = pd.read_sql(query, conn)
conn.close()

# Initialize Dash app
app = dash.Dash(__name__)

# Create figure
fig = px.line(df, x='date', y='avg_price', title='Stock Market Daily Trends', markers=True)

# App layout
app.layout = html.Div(children=[
    html.H1(children='📈 Stock Market Dashboard', style={'textAlign': 'center'}),
    dcc.Graph(id='trend-graph', figure=fig)
])

# Run app
if __name__ == '__main__':
    app.run(debug=True)

from pyngrok import ngrok

if __name__ == "__main__":
    public_url = ngrok.connect(8050)
    print(f"Public URL: {public_url}")
    app.run_server(port=8050)
