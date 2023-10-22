# Import necessary libraries
# from dash.dependencies import Input, Output
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import pandas as pd
import os
from wordcloud import WordCloud
import base64
from io import BytesIO
import random

path = os.path.dirname(os.getcwd())
df_year = pd.read_csv(os.path.join(path, 'data/artist_by_year.csv'))

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='What Happened to K-pop Girl Groups?', style={'textAlign': 'center'}),
    dcc.Dropdown(
        options=[{'label': artist, 'value': artist} for artist in df_year.artist_name.unique()],
        value="Girls' Generation",
        id='dropdown-selection'
    ),
    html.Div(id='image-gallery', children=[])
])

@app.callback(
    Output('image-gallery', 'children'),
    Input('dropdown-selection', 'value')
)



def make_image(value):
    df = df_year[df_year['artist_name'] == value].dropna(subset=['song_lyrics'])
    images = []

    for idx, (year, lyric) in enumerate(zip(df['year'], df['song_lyrics']), start=1):
        colormaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

        word_cloud = WordCloud(width=400, height=200, max_words=50, collocations=False, background_color='white',
                                colormap=random.choice(colormaps), font_path='../data/font/JalnanOTF.otf').generate(lyric)
        image = word_cloud.to_image()

        with BytesIO() as buffer:
            image.save(buffer, format='png')
            image_str = base64.b64encode(buffer.getvalue()).decode()

        images.append(html.Div(children=[
            html.H5(year),
            html.Img(src='data:image/png;base64,{}'.format(image_str))
        ]))

    return images

if __name__ == '__main__':
    app.run_server(debug=True)





# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Dummy data for artists (update with real data)
# artists = {
#     1: 'Artist 1',
#     2: 'Artist 2',
#     3: 'Artist 3'
# }

# # Define the app layout
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])

# index_page = html.Div([
#     dcc.Link('Home', href='/'),
#     html.Br(),
#     dcc.Link('How the girl group lyrics changed?', href='/page-2'),
#     html.Br(),
#     dcc.Link('By artist / By album', href='/page-3'),
# ])

# page_1_layout = html.Div([
#     html.H1('Home Page'),
#     html.P('Description about our project'),
#     html.Div([
#         dcc.Link('Go to Page 2', href='/page-2'),
#         html.Br(),
#         dcc.Link('Go to Page 3', href='/page-3'),
#     ]),
# ])

# page_2_layout = html.Div([
#     html.H1('How the girl group lyrics changed?'),
#     html.Div([
#         html.Div(id='div1', children=[
#             dcc.Graph(id='graph-2010'),
#             dcc.Graph(id='graph-2015'),
#             dcc.Graph(id='graph-2020')
#         ]),
#         html.Div(id='div2')
#     ]),
#     html.Div([
#         dcc.Link('Go back to home', href='/')
#     ]),
# ])

# page_3_layout = html.Div([
#     html.H1('By artist / By album'),
#     html.Div([
#         dcc.Dropdown(
#             id='artist-dropdown',
#             options=[{'label': name, 'value': id_} for id_, name in artists.items()],
#             value=1
#         ),
#         dcc.RadioItems(
#             id='selection-type',
#             options=[
#                 {'label': 'By Year', 'value': 'year'},
#                 {'label': 'By Album', 'value': 'album'}
#             ],
#             value='year'
#         ),
#         html.Div(id='word-cloud-container')
#     ]),
#     html.Div([
#         dcc.Link('Go back to home', href='/')
#     ]),
# ])

# # Define the app callback for page navigation
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/page-2':
#         return page_2_layout
#     elif pathname == '/page-3':
#         return page_3_layout
#     else:
#         return page_1_layout

# # Page 2 Callback (This is just a structure, real implementation needed based on your data)
# @app.callback(
#     [Output('graph-2010', 'figure'),
#      Output('graph-2015', 'figure'),
#      Output('graph-2020', 'figure')],
#     [Input('url', 'pathname')]
# )
# def update_page_2_graphs(pathname):
#     # Use this space to create plots for 2010, 2015, and 2020
#     # Here, I am returning dummy figures, replace them with real plots
#     return {}, {}, {}

# # Page 3 Callback
# @app.callback(
#     Output('word-cloud-container', 'children'),
#     [Input('artist-dropdown', 'value'),
#      Input('selection-type', 'value')]
# )
# def update_word_cloud(artist_id, selection_type):
#     # Use wc_by_year or wc_by_album here to generate word clouds
#     # Convert the word cloud to an image and display

#     def wc_by_year(df, artist_id_):
#         df = '../data/artist_by_year.csv'
#         df = df[df['artist_id']==artist_id_]
#         lyric_lst = [i for i in df.song_lyrics]
#         year_lst = [i for i in df.year]

#         for lyric in lyric_lst:
#             word_cloud = WordCloud(font_path='../data/font/JalnanOTF.otf', width = 1000, height = 500,
#             colormap='BuPu', max_words=50, collocations = False).generate(lyric)

#             plt.figure(figsize = (5,5))
#             plt.imshow(word_cloud, interpolation='bilinear')
#             plt.axis("off")
#             plt.title(f'{df.artist_name.iloc[0]} - {year_lst[lyric_lst.index(lyric)]}')
#             plt.show()

#     def wc_by_album(df, artist_id_):
#         df = '../data/artist_by_year_and_album.csv'

#         df = df[df['artist_id']==artist_id_]
#         df = df.sort_values('year')
#         lyric_lst = [i for i in df.song_lyrics]
#         year_lst = [i for i in df.year]
#         album_lst = [i for i in df.album_title]

#         artist_name_ = df.artist_name.iloc[0]


#         for lyric in lyric_lst:
#             word_cloud = WordCloud(font_path='../data/font/JalnanOTF.otf', width = 1000, height = 500,
#             colormap='prism', background_color= 'white', max_words=30, collocations = False).generate(lyric)

#             plt.figure(figsize = (6,4))
#             plt.imshow(word_cloud, interpolation='bilinear')
#             plt.axis("off")
#             plt.title(f'{artist_name_} - {df.album_title.iloc[lyric_lst.index(lyric)]} - {year_lst[lyric_lst.index(lyric)]}')
#             plt.show()

#     if selection_type == 'year':
#         # You need to define df for wc_by_year
#         # For now, using dummy df
#         df = pd.DataFrame()
#         wc_by_year(df, artist_id)
#     elif selection_type == 'album':
#         # You need to define df for wc_by_album
#         # For now, using dummy df
#         df = pd.DataFrame()
#         wc_by_album(df, artist_id)

#     # Convert plot to base64 encoded image and return as html.Img component
#     # This is just a structure, real implementation needed based on your functions
#     # Assuming you've saved your plots as PNG images as per your functions
#     encoded_image = base64.b64encode(open('path_to_saved_plot.png', 'rb').read())
#     return html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))

# # Start the Dash app
# if __name__ == '__main__':
#     app.run_server
