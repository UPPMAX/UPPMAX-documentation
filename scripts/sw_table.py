import sqlite3

import pandas as pd
from dash import Dash, dash_table

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("sw.db")
df = pd.read_sql_query("SELECT * from webpage", con)
df = df[["module", "name", "cluster", "version", "license"]]
df = df.loc[df["module"] != ""]

app = Dash(__name__)

app.layout = dash_table.DataTable(
    data=df.to_dict("records"),
    columns=[{"name": i, "id": i} for i in df.columns],
    filter_action="native",
    sort_action="native",
    sort_mode="multi",
    page_action="native",
    style_data={"whiteSpace": "normal", "height": "auto", "lineHeight": "15px"},
    style_table={
        "height": 1000,
    },
    css=[
        {
            "selector": "table",
            "rule": "table-layout: dynamic",  # note - this does not work with fixed_rows
        }
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
