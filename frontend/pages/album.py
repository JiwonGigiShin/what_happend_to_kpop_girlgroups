import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import os
from PIL import Image

dash.register_page(__name__)

path = os.path.dirname(os.getcwd())
# df_album = pd.read_csv(os.path.join(path, 'data/album_with_images.csv'))
df_album = pd.read_csv(os.path.join(path,'data/updated_df_111123.csv'))
logo_image = Image.open(os.path.join(os.getcwd(), 'data', 'girlgroup_nobg_album.png'))

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




# import dash
# from dash import html, dcc, callback, Input, Output
# import pandas as pd
# import os
# from PIL import Image

# dash.register_page(__name__)

# # logo_image = Image.open(os.path.join(os.getcwd(), 'data', 'girlgroup_nobg_home2.png'))

# layout = html.Div([
#     # html.Div([
#         # html.Img(src = logo_image, style = {'width': '80%', 'height': '80%'})], style={'textAlign': 'center'}),
#     html.H2('About this project', style={'margin': '20px 20px 20px 20px', 'textAlign': 'center'}),
#     html.Div([
#         html.H3('So, it is less hetero-normative than before?'),
#         html.P('Boy index'),
#         html.P('Love index'),
#         html.P('Love N-gram'),
#     ], style={'margin': '20px 20px 50px 50px'}),

#     html.Div([
#         html.H3("Key findings"),
#         html.P("-")
#     ], style={'margin': '20px 20px 50px 50px'})
# ])
