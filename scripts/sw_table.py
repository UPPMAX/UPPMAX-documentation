import sqlite3

import pandas as pd
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("sw.db")
df = pd.read_sql_query("SELECT * from webpage", con)
keywords = pd.read_sql_query("SELECT * from keywords", con)

keywords = (
    keywords.groupby("key")["keyword"].apply(lambda x: " ".join(x)).reset_index()
)
keywords = (
    keywords.merge(df, on="key")
    .drop_duplicates(subset=["name"])[["name", "keyword"]]
    .rename(columns={"keyword": "keywords"})
)
df = df.merge(keywords).drop(columns=["key"])


keep_cols = ["module", "name", "category", "cluster", "license", "keywords"]

df = df[keep_cols + ["version"]]
df = df.loc[df["module"] != ""]

df = (
    df.groupby(keep_cols)["version"]
    .apply(", ".join)
    .reset_index()
    .drop_duplicates()
    .rename(columns={"version": "versions"})
    .merge(keywords)
)


def get_unique_keywords(kws):
    tmp = []
    for k in kws.split():
        if k not in tmp:
            tmp.append(k)
    return ", ".join(tmp)

df["keywords"] = df["keywords"].apply(get_unique_keywords)

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
