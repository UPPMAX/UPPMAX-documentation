import sqlite3

import pandas as pd


def get_table():
    def get_unique_keywords(kws):
        return ", ".join(set(kws.split()))

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

    df["keywords"] = df["keywords"].apply(get_unique_keywords)

    df["id"] = df["module"]
    df.set_index("id", inplace=True, drop=False)

    return df


def save_to_html_file(html_content, filename="software_table.html"):
    with open(f"../docs/software/{filename}", "w") as f:
        f.write(html_content)


def main():
    df = get_table()

    # Convert to html
    html_table = df.to_html(classes="my_table", index=False)

    html_template = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your Table Title</title>

        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.css">
    </head>

    <body>

        <!-- Placeholder for the Generated Table -->
        {table_content}

        <!-- Include jQuery and DataTables libraries -->
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.js"></script>

        <!-- Initialize DataTables -->
        <script>
            $(document).ready( function () {
                $('.my_table').DataTable({
                    "stripeClasses": ['', 'table-striped'], // For stripes
                    "hover": true,  // For hover effect
            });
            });
        </script>

    </body>

    </html>
    """

    # Replace placeholder with actual table content
    final_html = html_template.replace("{table_content}", html_table)

    # Save to file
    save_to_html_file(final_html)


if __name__ == "__main__":
    main()
