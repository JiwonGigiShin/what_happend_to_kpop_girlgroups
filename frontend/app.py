# Import necessary libraries
# from dash.dependencies import Input, Output
import dash
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import pandas as pd
import numpy as np
import os
from wordcloud import WordCloud, ImageColorGenerator
import base64
from io import BytesIO
from PIL import Image
import requests

app = Dash(__name__)

path = os.path.dirname(os.getcwd())
df_album = pd.read_csv(os.path.join(path, 'data/album_with_images.csv'))


app.layout = html.Div([
    html.H1(children='K-Pop Girlgroup Analysis', style={'textAlign': 'center', 'color':'black', 'fontfamily': 'Poppins'}),
    html.Div([
        dcc.Dropdown(
        options=[{'label': artist, 'value': artist} for artist in df_album.artist_name.unique()],
        value="Girls' Generation",
        id='dropdown-selection',
        style={'textAlign': 'center', 'color': '#D30E92', 'backgroundColor':'#F1D6F5'}

    )
], style={"width": "60%", 'margin': 'auto', 'padding': 50}),
    html.Div(id='image-gallery', children=[], style={'textAlign': 'center'})

])

@app.callback(
    Output('image-gallery', 'children'),
    Input('dropdown-selection', 'value')
)

# html - Multi Pages
def make_image(value):

    df = df_album[df_album['artist_name'] == value].dropna(subset=['song_lyrics'])
    images = []

    for idx, (album_title, year, lyric, album_image) in enumerate(zip(df['album_title'], df['year'], df['song_lyrics'], df['album_image']), start=1):
        #colormaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
        #colormap=random.choice(colormaps),

        response = requests.get(album_image)
        image_data = BytesIO(response.content)
        image_opened = Image.open(image_data)
        image_colors = ImageColorGenerator(np.array(image_opened), default_color = (255,255,255))
        mask = np.array(Image.open(os.path.join(os.getcwd(), 'data/masking_image.jpeg')))

        word_cloud = WordCloud(
            width=200,
            height=200,
            max_words=50,
            mask=mask,
            collocations=False,
            background_color="rgba(255, 255, 255, 0)",
            mode="RGBA",
            font_path='../data/font/JalnanOTF.otf'
        ).generate(lyric)

        image = word_cloud.recolor(color_func=image_colors).to_image()


        with BytesIO() as buffer:
            image.save(buffer, format='png')
            image_str = base64.b64encode(buffer.getvalue()).decode()

        images.append(html.Div(children=[
                html.Div([
                html.H5(album_title, style={'display': 'inline-block', 'margin-right': '10px'}),
                html.H5(" - ", style={'display': 'inline-block'}),
                html.H5(year, style={'display': 'inline-block'})
            ]),
                html.Div([
                html.Img(src=album_image),
                html.Img(src='data:image/png;base64,{}'.format(image_str))
                ])
            ]))

    return images


if __name__ == "__main__":
    app.run_server(debug=True)
