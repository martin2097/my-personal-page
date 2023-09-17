from utils import priprava_dat
from dash import register_page, html, dcc, callback, Input, Output
import dash_mantine_components as dmc
from plotly.express import bar

register_page(__name__)

df = priprava_dat()

layout = dmc.Stack([
    dmc.Select(
        id="vyber-uzemi",
        value="Česká republika",
        label="Vyberte oblasť:",
        data=[
            {"value": moznost, "label": moznost}
            for moznost in df["uzemi_txt"].drop_duplicates().sort_values()

        ]
    ),
    dcc.Graph(id="graf-vzdelania")
])


@callback(
    Output("graf-vzdelania", "figure"),
    Input("vyber-uzemi", "value"),
)
def data_do_grafu(uzemie):
    w_df = df.copy()
    w_df = w_df[w_df["uzemi_txt"] == uzemie]
    w_df = w_df.groupby(by=["vzdelani_txt"])["hodnota"].sum().reset_index()

    fig = bar(w_df, x="vzdelani_txt", y="hodnota")

    return fig
