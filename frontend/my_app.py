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
        html.P('This project explores the evolution of K-pop girl group concepts, particularly focusing on themes of feminism and empowerment, from 2005 to the current year, 2022. It leverages multiple sources including social media, YouTube comments, song lyrics, and Google Trends for data collection and analysis. The project’s primary language focus includes Korean, English, Chinese, Spanish, and Japanese.'),
        html.P("The hypothesis central to this study posits that feminism has significantly influenced female audiences, leading to a shift in the target demographic of K-pop girl groups away from male fans. Additionally, the project hypothesizes that empowering lyrics and concepts, despite potentially self-objectifying, have positive effects on feminism and have significantly contributed to the global appeal of K-pop."),
    ]),
    html.Div([
        html.H3("Key findings and observations include:"),
        html.H5('2005-2010: Dominance of powerful but sexualized concepts, with girl groups like Miss A, 2NE1, and Sistar singing about heteronormative love but also displaying independence.'),
        html.H5('2012-2015: A mix of cute and sexy concepts with girl groups like SNSD and T-Ara, but with sexy concepts often criticized for being overly sensationalized.'),
        html.H5('2015-2020: Shift towards girlish and submissive concepts with groups like APINK, GFriend, and TWICE, with a heavy use of the word "소녀" (young girl) in group titles and lyrics.'),
        html.H5('2020s-onward: Return to neoliberal feminism with empowering, proactive lyrics and a move away from love-themed songs, seen in groups like MAMAMOO, Blackpink, and Aespa.'),
        html.P('The project uses Natural Language Processing (NLP) as its primary method for analysis. Data is compiled and organized in a Google Spreadsheet, and visualizations are created using Google Trends. Additional references include YouTube videos on the history of K-pop girl groups, discussions on body shaming within the industry, and lists of influential K-pop songs and albums.'),
        html.P("The research ultimately aims to provide a comprehensive overview of the changing themes and concepts within K-pop girl groups over the last two decades, shedding light on the industry's relationship with feminism and empowerment.")
    ]),
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
