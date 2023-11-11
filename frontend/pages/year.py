import os
import base64
import dash
from dash import html

dash.register_page(__name__)

# Function to convert image to base64 for web display
def img_to_base64_str(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Function to generate the file path and convert to base64
def generate_file_path(year):
    file_path = os.path.join(os.getcwd(), 'wordcloud', 'eng_year', f'{year}_wc.png')
    return "data:image/png;base64," + img_to_base64_str(file_path)

# Generate a list of blocks with year label and image for each year
year_blocks = []
for year in range(2007, 2024):
    year_block = html.Div([
        html.H3(str(year), style={'textAlign': 'center', 'fontSize': '24px'}),
        html.Img(src=generate_file_path(year), style={'padding': '10px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})
    ])
    year_blocks.append(year_block)

# Convert logo image to base64 string
logo_path = os.path.join(os.getcwd(), 'data', 'girlgroup_nobg_year.png')
logo_image_base64 = "data:image/png;base64," + img_to_base64_str(logo_path)

# Layout of the Dash app
layout = html.Div([
    html.Div([
        html.Img(src=logo_image_base64, style={'width': '50%', 'height': '50%'})], style={'textAlign': 'center'}),
    html.H2('Wordcloud By Year', style={'textAlign': 'center', 'fontSize': '30px'}),
    html.Div('Wordcloud from 2007-2023', style={'textAlign': 'center', 'fontSize': '15px'}),
    html.Div(year_blocks)
])


# 당시 차트 1,2,3,4,5위 누구였는지. 가장 인기많은 곡이 뭐였는지
# ngram
