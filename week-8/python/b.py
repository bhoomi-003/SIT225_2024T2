import pandas as pd
import plotly.graph_objects as go
import time

# Paths to your exported CSV files (update these paths if necessary)
csv_x = r"D:\SEM2\SIT225\Task 8.1\acc_x.csv"
csv_y = r"D:\SEM2\SIT225\Task 8.1\acc_y.csv"
csv_z = r"D:\SEM2\SIT225\Task 8.1\acc_z.csv"

# Read data from CSV files
data_x = pd.read_csv(csv_x)
data_y = pd.read_csv(csv_y)
data_z = pd.read_csv(csv_z)

# Combine data into one DataFrame for easier processing
data = pd.DataFrame({
    "x": data_x["value"],
    "y": data_y["value"],
    "z": data_z["value"]
})

# Buffers
main_buffer = []  # Continuously receives data
graph_buffer = []  # Holds the latest N samples for graphing
N = 1000  # Number of samples for graphing

# Debugging log
print("Script started. Processing data...")

# Simulate real-time data fetching
for i in range(len(data)):
    # Fetch new data and append to the main buffer
    new_data = {"x": data["x"][i], "y": data["y"][i], "z": data["z"][i]}
    main_buffer.append(new_data)
    
    # Debugging: Print new data fetched
    print(f"New data fetched: {new_data}")

    # Limit the size of the main buffer
    if len(main_buffer) > 5000:
        main_buffer = main_buffer[-5000:]  # Keep only the latest 5000 samples

    # Debugging: Print buffer sizes
    print(f"Main buffer size: {len(main_buffer)}")

    # Once enough data (N samples) is available, update the graph buffer
    if len(main_buffer) >= N:
        graph_buffer = main_buffer[:N]  # Copy the first N samples
        del main_buffer[:N]  # Remove these samples from the main buffer

        # Convert the graph buffer to a DataFrame for graphing
        graph_data = pd.DataFrame(graph_buffer)

        # Debugging: Print size of graph buffer
        print(f"Graph buffer size: {len(graph_buffer)}")

        # Plot data using Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=graph_data["x"], mode="lines", name="X-axis"))
        fig.add_trace(go.Scatter(y=graph_data["y"], mode="lines", name="Y-axis"))
        fig.add_trace(go.Scatter(y=graph_data["z"], mode="lines", name="Z-axis"))

        # Update layout
        fig.update_layout(
            title="Real-Time Accelerometer Data (Last N Samples)",
            xaxis_title="Samples",
            yaxis_title="Values"
        )

        # Show the graph
        fig.show()

        # Save the graph and data to files
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        fig.write_image(f"graph_{timestamp}.png")  # Requires pip install kaleido
        graph_data.to_csv(f"data_{timestamp}.csv", index=False)

        # Debugging: Print file save confirmation
        print(f"Graph and data saved with timestamp: {timestamp}")

    # Simulate a delay (e.g., real-time data arrival)
    time.sleep(0.1)