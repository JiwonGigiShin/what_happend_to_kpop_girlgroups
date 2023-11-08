import dash
from dash import html
import os
from PIL import Image

dash.register_page(__name__)

logo_image = Image.open(os.path.join(os.getcwd(), 'data', 'girlgroup_nobg_year.png'))

layout = html.Div([
    html.Div([
        html.Img(src = logo_image, style = {'width': '50%', 'height': '50%'})], style={'textAlign': 'center'}),
    html.H2('Wordcloud By Year', style={'textAlign': 'center'}),
    html.Div('content', style={'textAlign': 'center'}),
])
