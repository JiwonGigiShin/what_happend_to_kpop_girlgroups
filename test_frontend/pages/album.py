import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import os
from PIL import Image

dash.register_page(__name__)


path = os.path.dirname(os.getcwd())
# df_album = pd.read_csv(os.path.join(path, 'data/album_with_images.csv'))
df_album = pd.read_csv(os.path.join(path,'data/cleaned_album_df_311023.csv'))
logo_image = Image.open(os.path.join(os.getcwd(), 'data', 'girlgroup_nobg.png'))

layout = html.Div([
    html.Div([
        html.Img(src = logo_image, style = {'width': '30%', 'height': '30%'})], style={'textAlign': 'center'}),
    html.H1(children='Wordcloud by Albums', style={'textAlign': 'center', 'color':'black', 'fontfamily': 'Poppins'}),

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

@callback(
    Output('image-gallery', 'children'),
    Input('dropdown-selection', 'value')
)

# html - Multi Pages
def make_image(value):

    df = df_album[df_album['artist_name'] == value].sort_values(by='release_date')
    artist_id_ = df.artist_id.iloc[0]
    images = []

    for idx, (album_id, album_title, year, album_image) in enumerate(zip(df['album_id'], df['album_title'], df['year'], df['album_image']), start=1):
        #colormaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
        #colormap=random.choice(colormaps),

        # image = f'wordcloud/{artist_id_}_{album_id}_wc.png'
        # with BytesIO() as buffer:
        #     image.save(buffer, format='png')
        #     image_str = base64.b64encode(buffer.getvalue()).decode()

        pil_image = Image.open(os.path.join(os.getcwd(), f"wordcloud/eng_lemma/{artist_id_}_{album_id}_wc.png"))

        images.append(html.Div(children=[
                html.Div([
                html.H3(album_title, style={'display': 'inline-block', 'margin-right': '10px'}),
                html.H5(" - ", style={'display': 'inline-block'}),
                html.H5(year, style={'display': 'inline-block'})
            ]),
                html.Div([
                html.Img(src=album_image, style={'display': 'inline-block'}),
                html.P(' ', style={'display': 'inline-block'}),
                html.Img(src=pil_image, style={'display': 'inline-block'})

                # html.Img(src='data:image/png;base64,{}'.format(image_str))
                ])
            ]))

    return images
