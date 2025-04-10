from arduino_iot_cloud import ArduinoCloudClient
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from collections import deque
import threading
from datetime import datetime
import pandas as pd
import os

# Arduino Cloud Configuration
DEVICE_ID = "1f087a6a-6d2c-40dd-aa33-c40ecdcca76f"
USERNAME = "1f087a6a-6d2c-40dd-aa33-c40ecdcca76f"
PASSWORD = "EQNLxhwpMc5iYwj#@0Bcjy0dx"

BUFFER_SIZE = 1000      
data_lock = threading.Lock()
timestamps = deque(maxlen=BUFFER_SIZE)
x_data = deque(maxlen=BUFFER_SIZE)
y_data = deque(maxlen=BUFFER_SIZE)
z_data = deque(maxlen=BUFFER_SIZE)

# Initialize Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='graph-update', interval=1000, n_intervals=0)  # Update every 1 second
])

# Callback to Update Graph
@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    # Safely copy data to avoid thread conflicts
    with data_lock:
        ts = list(timestamps)
        x = list(x_data)
        y = list(y_data)
        z = list(z_data)

    # Create Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ts, y=x, name='X', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=ts, y=y, name='Y', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=ts, y=z, name='Z', line=dict(color='yellow')))
    fig.update_layout(
        title='Real-Time Accelerometer Data',
        xaxis_title='Time',
        yaxis_title='Value',
        showlegend=True
    )
    return fig

# Arduino Cloud Callbacks (Write to CSV + Update Buffers)
def on_py_x(client, value):
    try:
        value = float(value)  # Ensure the value is a float
        timestamp = datetime.now().replace(year=2025)
        with data_lock:
            x_data.append(value)
            timestamps.append(timestamp)
        # Append to CSV
        with open('x.csv', 'a') as f:
            f.write(f"{timestamp.isoformat()},{value}\n")
        print(f"Written X data: {timestamp.isoformat()},{value}")  # Debugging
    except ValueError as e:
        print(f"Invalid x value: {value} ({e})")

def on_py_y(client, value):
    try:
        value = float(value)  # Ensure the value is a float
        timestamp = datetime.now().replace(year=2025)
        with data_lock:
            y_data.append(value)
        # Append to CSV
        with open('y.csv', 'a') as f:
            f.write(f"{timestamp.isoformat()},{value}\n")
        print(f"Written Y data: {timestamp.isoformat()},{value}")  # Debugging
    except ValueError as e:
        print(f"Invalid y value: {value} ({e})")

def on_py_z(client, value):
    try:
        value = float(value)  # Ensure the value is a float
        timestamp = datetime.now().replace(year=2025)
        with data_lock:
            z_data.append(value)
        # Append to CSV
        with open('z.csv', 'a') as f:
            f.write(f"{timestamp.isoformat()},{value}\n")
        print(f"Written Z data: {timestamp.isoformat()},{value}")  # Debugging
    except ValueError as e:
        print(f"Invalid z value: {value} ({e})")

# Initialize CSV Files
for axis in ['x', 'y', 'z']:
    if not os.path.exists(f'accel_{axis}.csv'):
        with open(f'accel_{axis}.csv', 'w') as f:
            f.write("timestamp,value\n")
            print(f"Created new file: accel_{axis}.csv")  # Debugging

# Connect to Arduino Cloud
client = ArduinoCloudClient(
    device_id=DEVICE_ID,
    username=USERNAME,
    password=PASSWORD
)
client.register("x", on_write=on_py_x)
client.register("y", on_write=on_py_y)
client.register("z", on_write=on_py_z)

# Start Arduino Cloud Thread
cloud_thread = threading.Thread(target=client.start)
cloud_thread.daemon = True
cloud_thread.start()

if __name__ == '__main__':
    app.run_server(debug=False)
