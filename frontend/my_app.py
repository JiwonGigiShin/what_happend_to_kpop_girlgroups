from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import dash

app = Dash(__name__, use_pages=True)
server = app.server


app.layout = html.Div([
    html.H1('WHAT HAPPENED TO K-POP GIRL GROUPS?', style={'textAlign': 'center'}),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ], style={'textAlign': 'center', 'fontSize': 25, 'color': 'white'}),
    dash.page_container
])




if __name__ == "__main__":
    app.run_server(debug=True)
