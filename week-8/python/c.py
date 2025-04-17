from dash import Dash, dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.graph_objects as go
import time

# File paths for accelerometer data (update as needed)
csv_x = r"D:\SEM2\SIT225\Task 8.1\acc_x.csv"
csv_y = r"D:\SEM2\SIT225\Task 8.1\acc_y.csv"
csv_z = r"D:\SEM2\SIT225\Task 8.1\acc_z.csv"

# Load CSV data
data_x = pd.read_csv(csv_x, usecols=["value"])["value"].tolist()
data_y = pd.read_csv(csv_y, usecols=["value"])["value"].tolist()
data_z = pd.read_csv(csv_z, usecols=["value"])["value"].tolist()

# Buffers for dynamic updates
buffer_x, buffer_y, buffer_z = [], [], []
BUFFER_SIZE = 100  # Number of samples to display

# Dash app setup
app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="live-graph"),  # Graph placeholder
    dcc.Interval(id="update-interval", interval=1000, n_intervals=0)  # Update every second
])

# Callback to update the graph dynamically
@app.callback(
    Output("live-graph", "figure"),
    [Input("update-interval", "n_intervals")]
)
def update_graph(n):
    global buffer_x, buffer_y, buffer_z

    # Simulate live data by taking one value at a time from the loaded data
    if len(data_x) > 0 and len(data_y) > 0 and len(data_z) > 0:
        buffer_x.append(data_x.pop(0))
        buffer_y.append(data_y.pop(0))
        buffer_z.append(data_z.pop(0))

    # Keep buffer size fixed
    if len(buffer_x) > BUFFER_SIZE:
        buffer_x = buffer_x[-BUFFER_SIZE:]
        buffer_y = buffer_y[-BUFFER_SIZE:]
        buffer_z = buffer_z[-BUFFER_SIZE:]

    # Create graph figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=buffer_x, mode="lines", name="X-axis"))
    fig.add_trace(go.Scatter(y=buffer_y, mode="lines", name="Y-axis"))
    fig.add_trace(go.Scatter(y=buffer_z, mode="lines", name="Z-axis"))

    fig.update_layout(
        title="Real-Time Accelerometer Data",
        xaxis_title="Samples",
        yaxis_title="Values",
        template="plotly_dark"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=False)