import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H2('Wordcloud By Year', style={'textAlign': 'center'}),
    html.Div('content', style={'textAlign': 'center'}),
])
