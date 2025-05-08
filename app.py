{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c5bc6183-f873-4de9-b8a4-ebf6aea92871",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x199f30afe60>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import dash\n",
    "from dash import dcc, html\n",
    "from dash.dependencies import Input, Output\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(\"historical_automobile_sales.csv\")  # Replace with your actual dataset\n",
    "\n",
    "# Initialize the Dash app\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "# Layout\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"Automobile Sales Dashboard\", style={\"textAlign\": \"center\"}),\n",
    "\n",
    "    html.Label(\"Select Vehicle Type\"),\n",
    "    dcc.Dropdown(\n",
    "        id=\"vehicle-dropdown\",\n",
    "        options=[{\"label\": vt, \"value\": vt} for vt in df[\"Vehicle_Type\"].unique()],\n",
    "        value=df[\"Vehicle_Type\"].unique()[0],\n",
    "        clearable=False\n",
    "    ),\n",
    "\n",
    "    html.Label(\"Select Recession Status\"),\n",
    "    dcc.Dropdown(\n",
    "        id=\"recession-dropdown\",\n",
    "        options=[\n",
    "            {\"label\": \"Recession\", \"value\": 1},\n",
    "            {\"label\": \"Non-Recession\", \"value\": 0}\n",
    "        ],\n",
    "        value=1,\n",
    "        clearable=False\n",
    "    ),\n",
    "\n",
    "    html.Div(id=\"output-container\", style={\"marginTop\": \"20px\"})\n",
    "])\n",
    "\n",
    "# Single callback to handle multiple outputs\n",
    "@app.callback(\n",
    "    Output(\"output-container\", \"children\"),\n",
    "    [Input(\"vehicle-dropdown\", \"value\"),\n",
    "     Input(\"recession-dropdown\", \"value\")]\n",
    ")\n",
    "def update_output(selected_vehicle, recession_status):\n",
    "    filtered_df = df[(df[\"Vehicle_Type\"] == selected_vehicle) & (df[\"Recession\"] == recession_status)]\n",
    "\n",
    "    # 2.4 - Display total sales\n",
    "    total_sales = filtered_df[\"Automobile_Sales\"].sum()\n",
    "    sales_text = html.H3(f\"Total Sales for {selected_vehicle} during {'Recession' if recession_status == 1 else 'Non-Recession'}: {total_sales}\")\n",
    "\n",
    "    # 2.5 - Line plot for recession statistics\n",
    "    fig1 = px.line(filtered_df, x=\"Year\", y=\"Automobile_Sales\", title=f\"Sales Trend for {selected_vehicle}\")\n",
    "\n",
    "    # 2.6 - Bar plot for yearly statistics\n",
    "    fig2 = px.bar(filtered_df, x=\"Year\", y=\"Automobile_Sales\", color=\"Vehicle_Type\", title=\"Yearly Sales by Vehicle Type\")\n",
    "\n",
    "    return [\n",
    "        sales_text,\n",
    "        dcc.Graph(figure=fig1),\n",
    "        dcc.Graph(figure=fig2)\n",
    "    ]\n",
    "\n",
    "# Run the app\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, port=8050, use_reloader=False)  # Runs on http://127.0.0.1:8050\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "571b0f88-a5ad-4645-ad2c-1ba189284516",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
