import dash
from dash import html
import os
from PIL import Image


dash.register_page(__name__, path='/')

logo_image = Image.open(os.path.join(os.getcwd(), 'data', 'girlgroup_nobg_home2.png'))

layout = html.Div([
    html.Div([
        html.Img(src = logo_image, style = {'width': '80%', 'height': '80%'})], style={'textAlign': 'center'}),
    html.H2('About this project', style={'margin': '20px 20px 20px 20px', 'textAlign': 'center'}),
    html.Div([
        html.P('This project explores the evolution of K-pop girl group concepts, particularly focusing on themes of feminism and empowerment, from 2005 to the current year, 2022. It leverages multiple sources including social media, YouTube comments, song lyrics, and Google Trends for data collection and analysis. The project’s primary language focus includes Korean, English, Chinese, Spanish, and Japanese.'),
        html.P("The hypothesis central to this study posits that feminism has significantly influenced female audiences, leading to a shift in the target demographic of K-pop girl groups away from male fans. Additionally, the project hypothesizes that empowering lyrics and concepts, despite potentially self-objectifying, have positive effects on feminism and have significantly contributed to the global appeal of K-pop."),
    ], style={'margin': '20px 20px 50px 50px'}),

    html.Div([
        html.H3("Key findings and observations include:"),
        html.H5('2005-2010: Dominance of powerful but sexualized concepts, with girl groups like Miss A, 2NE1, and Sistar singing about heteronormative love but also displaying independence.'),
        html.H5('2012-2015: A mix of cute and sexy concepts with girl groups like SNSD and T-Ara, but with sexy concepts often criticized for being overly sensationalized.'),
        html.H5('2015-2020: Shift towards girlish and submissive concepts with groups like APINK, GFriend, and TWICE, with a heavy use of the word "소녀" (young girl) in group titles and lyrics.'),
        html.H5('2020s-onward: Return to neoliberal feminism with empowering, proactive lyrics and a move away from love-themed songs, seen in groups like MAMAMOO, Blackpink, and Aespa.'),
        html.P('The project uses Natural Language Processing (NLP) as its primary method for analysis. Data is compiled and organized in a Google Spreadsheet, and visualizations are created using Python, Flask, Plotly Dash. Additional references include YouTube videos on the history of K-pop girl groups, discussions on heteronormativity within the industry, and lists of influential K-pop songs and albums.'),
        html.P("The research ultimately aims to provide a comprehensive overview of the changing themes and concepts within K-pop girl groups over the last two decades, shedding light on the industry's relationship with feminism and empowerment.")
    ], style={'margin': '20px 20px 50px 50px'})
])
