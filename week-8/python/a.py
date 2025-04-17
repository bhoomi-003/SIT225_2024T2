import pandas as pd
import plotly.graph_objects as go

# Define paths for the three CSV files
csv_files = {
    "X-axis": r"D:\SEM2\SIT225\Task 8.1\acc_x.csv",
    "Y-axis": r"D:\SEM2\SIT225\Task 8.1\acc_y.csv",
    "Z-axis": r"D:\SEM2\SIT225\Task 8.1\acc_z.csv"
}

# Iterate through each file and process data
for axis, file_path in csv_files.items():
    print(f"Processing data for: {axis} ({file_path})")

    # Load the CSV file
    data = pd.read_csv(file_path)

    # Preview the first few rows
    print(data.head())

    # Create a line plot for the accelerometer values
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=data["value"], mode="lines", name=f"{axis} values"))

    # Update layout for clarity
    fig.update_layout(
        title=f"Accelerometer Data for {axis}",
        xaxis_title="Samples",
        yaxis_title="Values",
        legend_title="Axis"
    )

    # Show the graph
    fig.show()

    # Perform statistical analysis
    print(f"Statistics for {axis}:")
    print("Mean Value:", data["value"].mean())
    print("Variance:", data["value"].var())
    print("Range:", data["value"].max() - data["value"].min())

    print("\n---------------------------\n")