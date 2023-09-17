from dash import Dash, html, callback, Input, Output, State, page_container
import dash_mantine_components as dmc
from utils import navigacny_panel

app = Dash(__name__, use_pages=True)
server = app.server

links = {
    "o-mne": {"label": "O mne"},
    "skusenosti": {"label": "Skúsenosti"},
    "projekty": {"label": "Projekty"},
    "kontakty": {"label": "Kontakty"},
}

app.layout = dmc.MantineProvider(
    [
        navigacny_panel(odkazy=links, logo="tabler:square-rounded-letter-l"),
        html.Div(page_container, style={"margin-top": "40px"})
    ],
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    id="provider-temy")


@callback(
    Output("provider-temy", "theme"),
    Input("tlacidlo-zmena-temy", "n_clicks"),
    State("provider-temy", "theme"),
    prevent_initial_call=True
)
def zmen_temu(n_clicks, tema):
    if tema["colorScheme"] == "dark":
        return {"colorScheme": "light"}
    else:
        return {"colorScheme": "dark"}


if __name__ == "__main__":
    app.run(debug=False)
