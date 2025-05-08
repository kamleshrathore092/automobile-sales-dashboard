# Automobile Sales Dashboard

This is an interactive dashboard built using **Dash (Plotly)** and **Pandas** to visualize historical automobile sales data. It allows users to:

- Select vehicle types (e.g., Cars, SUVs, Trucks)
- Filter data by economic status (Recession vs. Non-Recession)
- View total sales based on selected filters
- Explore trends with dynamic line and bar charts

## Features

- Dropdowns for filtering data
- Total sales summary display
- Year-wise line chart for selected vehicle types
- Bar chart showing yearly sales distribution

## Technologies Used

- Python
- Dash (by Plotly)
- Pandas
- Plotly Express

## Run Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/automobile-sales-dashboard.git
    cd automobile-sales-dashboard
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    python app.py
    ```

The dashboard will be available at `http://127.0.0.1:8050`.

## Deployment

This app can be deployed for free using [Render.com](https://render.com). A `render.yaml` is included for easy configuration.

## Dataset

Make sure to include the file `historical_automobile_sales.csv` in the project directory. The CSV should contain at least the following columns:
- `Year`
- `Vehicle_Type`
- `Automobile_Sales`
- `Recession`

## License

This project is licensed under the MIT License.
