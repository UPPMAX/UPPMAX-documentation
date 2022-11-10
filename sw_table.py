import sqlite3

import pandas as pd
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("sw.db")
df = pd.read_sql_query("SELECT * from webpage", con)
df = df[["module", "name", "category", "cluster", "version", "license"]]
df = df.loc[df["module"] != ""]

df["id"] = df["module"]
df.set_index("id", inplace=True, drop=False)

app = Dash(__name__)

app.layout = html.Div(
    [
        dash_table.DataTable(
            id="datatable-row-ids",
            columns=[
                {"name": i, "id": i, "deletable": True}
                for i in df.columns
                # omit the id column
                if i != "id"
            ],
            data=df.to_dict("records"),
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            page_action="native",
            page_current=0,
            page_size=10,
            style_data={
                "whiteSpace": "normal",
                "height": "fixed",
                "lineHeight": "15px",
            },
            style_table={
                "height": "auto",
            },
            css=[
                {
                    "selector": "table",
                    "rule": "table-layout: dynamic",  # note - this does not work with fixed_rows
                }
            ],
        ),
        html.Div(id="datatable-row-ids-container"),
    ]
)


@app.callback(
    Output("datatable-row-ids-container", "children"),
    Input("datatable-row-ids", "derived_virtual_row_ids"),
    Input("datatable-row-ids", "selected_row_ids"),
    Input("datatable-row-ids", "active_cell"),
)
def update_graphs(row_ids, selected_row_ids, active_cell):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = df
        # pandas Series works enough like a list for this to be OK
        row_ids = df["id"]
    else:
        dff = df.loc[row_ids]

    dff = dff.groupby("category").count().reset_index()

    active_row_id = active_cell["row_id"] if active_cell else None

    colors = [
        "#C41237"
        if id == active_row_id
        else "#C41237"
        if id in selected_id_set
        else "#C41237"
        for id in row_ids
    ]

    return dcc.Graph(
        id="category" + "--row-ids",
        figure={
            "data": [
                {
                    "x": dff["category"],
                    "y": dff["module"],
                    "type": "bar",
                    "marker": {"color": colors},
                }
            ],
            "layout": {
                "xaxis": {"automargin": True},
                "yaxis": {"automargin": True, "title": {"text": "category"}},
                "height": 250,
                "margin": {"t": 10, "l": 10, "r": 10},
            },
        },
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
