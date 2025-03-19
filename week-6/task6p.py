import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, dash_table 
from dash.dependencies import Input, Output

# Load dataset safely
try:
    data = pd.read_csv("gyroscope_data.csv")

    # Ensure correct column names
    data.rename(columns={'timestamp': 'Timestamp'}, inplace=True)

    # Convert Timestamp to datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')

except Exception as e:
    print(f"Error loading CSV: {e}")
    data = pd.DataFrame(columns=["Timestamp", "x", "y", "z"])  # Empty DataFrame

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Gyroscope Data Visualization"),
    
    html.Label("Select Graph Style:"),
    dcc.Dropdown(id='graph-type', options=[
        {'label': 'Scatter Plot', 'value': 'scatter'},
        {'label': 'Line Graph', 'value': 'line'},
        {'label': 'Histogram', 'value': 'histogram'}
    ], value='scatter'),

    html.Label("Select Data Variables:"),
    dcc.Dropdown(
        id='axis-select', 
        options=[
            {'label': 'X-axis', 'value': 'x'},
            {'label': 'Y-axis', 'value': 'y'},
            {'label': 'Z-axis', 'value': 'z'}
        ], 
        multi=True,
        value=['x', 'y', 'z']
    ),

    html.Label("Number of Samples to Display:"),
    dcc.Input(id='sample-size', type='number', value=100, min=1),

    html.Button('Previous Batch', id='prev-button', n_clicks=0),
    html.Button('Next Batch', id='next-button', n_clicks=0),

    dcc.Graph(id='chart-output'),
    dash_table.DataTable(id='summary-table')
])

@app.callback(
    [Output('chart-output', 'figure'), 
     Output('summary-table', 'data')],
    [Input('graph-type', 'value'), 
     Input('axis-select', 'value'), 
     Input('sample-size', 'value'), 
     Input('prev-button', 'n_clicks'), 
     Input('next-button', 'n_clicks')]    
)
def update_chart(graph_type, axis_select, sample_size, prev_click, next_click):
    start_index = max(0, (next_click - prev_click) * sample_size)
    subset = data.iloc[start_index:start_index + sample_size]

    # Ensure subset is not empty
    if subset.empty:
        return px.scatter(title="No Data Available"), []

    # Create the selected graph type
    if graph_type == 'scatter':
        fig = px.scatter(subset, x='Timestamp', y=axis_select, title='Gyroscope Data')
    elif graph_type == 'line':
        fig = px.line(subset, x='Timestamp', y=axis_select, title='Gyroscope Data')
    elif graph_type == 'histogram':
        fig = px.histogram(subset, x='Timestamp', y=axis_select, title='Gyroscope Data')
    else:
        fig = px.scatter(title="Invalid Selection")

    # Generate summary statistics
    summary = subset[axis_select].describe().reset_index().to_dict('records')

    return fig, summary

if __name__ == '__main__':
    app.run_server(debug=True)
