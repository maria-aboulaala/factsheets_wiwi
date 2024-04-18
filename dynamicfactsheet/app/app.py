import dash
import requests
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

labels = ['A', 'B', 'C', 'D']
values = [20, 30, 40, 10]

with open('/home/maboula/Desktop/dynamicfactsheet/app/response_1713280437594.json') as f:
    data = json.load(f)
    df = pd.DataFrame(data["data"])

df['Date'] = pd.to_datetime(df['Date'])
# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
        html.Div(style={
    'display': 'flex',
    'justifyContent': 'center',  # Centrer les éléments horizontalement
    'alignItems': 'center',  # Centrer verticalement le texte dans les divs
    'padding': '10px',  # Ajouter un rembourrage pour l'esthétique
    'color': '#333',  # Faire correspondre la couleur du texte
    'fontSize': '10px',  # Ajuster la taille de la police si nécessaire
    'gap': '20em'  # Espacement de 2 unités entre les éléments
},
    children=[
        html.Div('Upfront Annual Management Fees: 0.85%', style={'margin': '0'}),
        html.Div('Daily Liquidity, with no Exit Fees', style={'margin': '0'}),
        html.Div('Factsheet As Of 01 April, 2024', style={'margin': '0'})
    ]
),
    html.Div(
        style={
            'backgroundColor': '#FFFFFF', 
            'color': '#0F73F8', 
            'padding': '10px 20px', 
            'display': 'flex', 
            'alignItems': 'center', 
            'justifyContent': 'space-between'
        }, 
        children=[
            html.Img(src='/assets/logo.png', style={'height': '50px'}),
            html.Div(
                style={
                    'padding': '10px 0',  
                    'color': '#A6A6A6', 
                    'fontSize': '10px',
                    'backgroundColor': '#FFF',  
                    'borderBottom': '0px solid #DDD',
                    'marginTop': '0px'  
                },
                children=[
                    html.Div('FinaMaze achieves an optimal diversification within the Smartfolio and saves on transaction costs, by investing in Single Stocks, Futures and, when efficient, Exchange Traded Funds and Exchange Traded Products.', style={'marginRight': '40px'}),
                    html.Div('FinaMaze selects the most beneficial ones, seeking the investor\'s best interest.', style={'marginRight': '40px'}),
                ]
            )
        ]
    ),

    html.Div([
        html.Button("Download as PDF", id="download-pdf-button", n_clicks=0)]),

    html.Div(
        style={'backgroundColor': '#0F73F8', 'color': 'white', 'padding': '10px 0'}, 
        children=[
            html.H2('NATIVE TOKENS', style={'textAlign': 'center', 'margin': '0'})
        ]
    ),
    dcc.Tabs(
        id='tabs',
        style={'fontSize': '18px', 'padding': '0'}, 
        children=[
            dcc.Tab(label='Overview', value='overview', style={'padding': '6px'}, selected_style={'backgroundColor': 'white', 'color': '#0F73F8'}),
            dcc.Tab(label='Price Performance', value='price-performance', style={'padding': '6px'}, selected_style={'backgroundColor': 'white', 'color': '#0F73F8'}),
            dcc.Tab(label='Metrics & Perfomances', value='metrics', style={'padding': '6px'}, selected_style={'backgroundColor': 'white', 'color': '#0F73F8'}),
            dcc.Tab(label='News & Reviews', value='news-reviews', style={'padding': '6px'}, selected_style={'backgroundColor': 'white', 'color': '#0F73F8'}),
        ],
        colors={
            "border": "white",
            "primary": "#0F73F8",
            "background": "#FFFFFF"
        }
    ),

html.Div(
    id = 'smartfolio_description',
    style={'backgroundColor': 'white', 'color': '#333', 'padding': '75px', 'margin': '0px 0'}, 
    children=[
        html.P('This portfolio seeks to reproduce the performance of alternative coins (Ethereum, Binance Coin, Cardano, Solana...)', style={'textAlign': 'left'}),
        html.Li('It builds exposure to the top 9 largest native tokens of original protocols, excluding Bitcoin.', style={'textAlign': 'left'}),
        html.Li('It aims to capture the trend favoring the blockchain protocols that will form the basis of a large panel of the economic activity in the future.', style={'textAlign': 'left'}),
        html.Li('Investing in 9 native tokens reduces the risk of any individual protocol failing or being superseded by better or more adopted technology.', style={'textAlign': 'left'}),
        html.Li([
            "The whole 'Native Tokens' Smartfolio is offered with a deleveraged exposure to significantly reduce the impact of the volatility of the tokens."
        ], style={'textAlign': 'left'})
    ]
),

    html.Div(
        id='header-section',
        style={
            'fontSize': '18px',
            'padding': '20px',
            'textAlign': 'center',  # Align the content to the center
            'margin': '0 auto',  # Horizontally center the div
            'width': '80%',  # Adjust the width of the centered div if needed
            'display': 'flex',
            'justifyContent': 'space-between',  # Create space between elements
            'alignItems': 'center',  # Center the children vertically
            'color': '#0F73F8'
        }, 
        children=[
            html.Div(children=[
                html.H1(children='5'), 
                html.H3(children='Number Of Individual Exposures')  # Text at the bottom
            ]),
            html.Div(children=[
                html.H1(children='0.62%'), 
                html.H3(children='Weighted Average Total Expense Ratio')  # Text at the bottom
            ]),
            html.Div(children=[
                html.H1(children='5'),  
                html.H3(children='Number of Exchange Traded Funds')  
            ])
        ]
    ),
    html.Div(
        id = 'NB-description',
                children=[
                    html.Div('FinaMaze achieves an optimal diversification within the Smartfolio and saves on transaction costs, by investing in Single Stocks, Futures and, when efficient, Exchange Traded Funds and Exchange Traded Products.', style={'marginRight': '40px'}),
                    html.Div('FinaMaze selects the most beneficial ones, seeking the investor\'s best interest.', style={'marginRight': '40px'}),
                ]
            ),
    html.Div([
    html.Div(
        id='AI_vs_FullExposure',
    children=[
        html.P([
            html.Span("AI Autopilot or Full Exposure", style={'color': '#0F73F8'}),
            html.Br(),
            html.Span("• The Full Exposure Smartfolio mirrors the specified market without taking into account the investor’s risk profile. Investing in this Smartfolio on a Full Exposure basis is risky and volatile. It should be considered only by "),
            html.Span("sophisticated investors who have experience in Cryptocurrencies, and only in sizes that they are comfortable to expose to high losses,", style={'fontWeight': 'bold'}),
            html.Span(" for potentially higher profits."),
            html.Br(),
            html.Span("• The AI Autopilot Smartfolio's algorithm adjusts the investment to remain in line with the investor’s risk profile and volatility targets, derived from over 4,000 possible risk levels, as shown in the "),
            html.Span("light",style={'color': '#49C3FB', 'fontWeight': 'bold'}),
            html.Span("-to-dark", style={'color': '#31356E', 'fontWeight': 'bold'}),
            html.Span (" blue band"),
            html.Span(". AI Autopilot Smartfolios are not always 100%: they keep a regularly adjusted portion of cash to manage the overall volatility of the portfolio. Losses and Profits from the AI Autopilot Smartfolio would be most of the time inferior to the Full Exposure."),
            html.Span(" Investors with limited experience in Cryptocurrency would prefer to invest in AI Autopilot Smartfolios.", style={'fontWeight': 'bold'}),
        ], style={'textAlign': 'left'})
    ]
    ),
    html.Div(id ='Composition')], style={'display': 'flex', 'justifyContent': 'center'}),
    

    html.Div(
        id='No-Conflict-of-Interest',
        children=[
            html.P([ "FinaMaze does not receive any sort of payment or advantage from any ETF provider nor from any broker" ], style={'color' : '#0F73F8', 'textAlign': 'center', 'textTransform': 'uppercase', 'fontWeight': 'bold'})
        ]
    ),

html.Div(
    id='Guarantee-Disclaimer',
    children=[
        html.P([
            "Just like any other investment, your FinaMaze investment performance is not guaranteed. Past performance is NOT a reliable indicator of future performance.",
        ], style={'textAlign': 'center'})
    ]
),

html.Div(
    id='color-band-description',
    
    children=[
        html.P([
            "Your AI Autopilot Smartfolios performance would have been inside the ",
            html.Span("light", style={'color': '#49C3FB', 'fontWeight': 'bold'}),
            " ",
            html.Span("(Most Prudent)", style={'color': '#49C3FB'}),
            "-to-",
            html.Span("dark", style={'color': '#31356E', 'fontWeight': 'bold'}),
            " ",
            html.Span("(Most Aggressive)", style={'color': '#31356E'}),
            " blue band."
        ], style={'textAlign': 'center'})
    ]
),

html.Div(
        id = 'Exposure-description',
                children=[
                    html.Div('* Indicative Exposure: Depending on the risk profile', style={'marginRight': '40px'}),
                    html.Div('it changes over time within the range to calibrate for the risk involved.', style={'marginRight': '40px'}),

                ]
            ),

html.Div(
        id = 'Information-only-description',
                children=[
                    html.Div('This document is not investment advice, it is for information purposes only.'),
                ]
            ),


 dcc.Graph(id='time-series-chart'),
    
html.Div([
    html.Div(id ='Sectoral Composition', style={'flex': '1', 'textAlign': 'right'}),  
    html.Div(id ='Annualized Returns', style={'flex': '1', 'textAlign': 'center'}),  
    html.Div(id ='Current Holdings', style={'flex': '1', 'textAlign': 'left'})  
], style={'display': 'flex', 'justifyContent': 'space-between'}) ,




html.Div( children=[ html.Hr(id='line1')]),


html.Div(style={'display': 'flex', 'justifyContent': 'space-between'}, children=[
    html.Div([
        html.Div(id='volatility_metric', children=[
            html.P([
                html.Span("VOLATILITY", style={'color': '#0F73F8'}),
            ], style={'transform': 'rotate(-90deg)', 'text-align': 'left'})
        ]),
        html.Div(id ='Volatility_definition', children=[
            html.Span("Volatility in a financial portfolio refers to the measure of the variability of returns of that portfolio over a specific period of time. It is typically calculated using the standard deviation of returns, indicating the magnitude and frequency of price fluctuations of the assets held in the portfolio. Higher volatility implies greater uncertainty about future returns, while lower volatility is often associated with relative stability in portfolio performance")
        ])
    ]),
    dcc.Graph(id ='Volatility_plot')
])


])

@app.callback(
    dash.dependencies.Output('time-series-chart', 'figure'),
    [dash.dependencies.Input('time-series-chart', 'id')]
)
def update_graph(_):
    trace1 = go.Scatter(x=df['Date'], y=df['Bitcoin_2022'], mode='lines',showlegend=False, name='Bitcoin 2022')
    trace2 = go.Scatter(x=df['Date'], y=df['Native Tokens_2022'], mode='lines', showlegend=False, name='Native Tokens 2022')
    
    trace3 = go.Scatter(
        x=df['Date'], y=df['Native Tokens AI Autopilot Prudent_2022'],
        mode='lines', name='Prudent 2022',
        line=dict(color='blue'), 
        fill='tonexty', 
        showlegend=False,
        fillcolor='rgba(173,216,230,0.4)' 
    )
    trace4 = go.Scatter(
        x=df['Date'], y=df['Native Tokens AI Autopilot Risky_2022'],
        mode='lines', name='Risky 2022',
        line=dict(color='navy'), 
        fill='tonexty',
        showlegend=False,
        fillcolor='rgba(0,0,255,0.4)' 
    )

    # Combine traces into a figure
    fig = go.Figure(data=[trace1, trace2, trace3, trace4])
    fig.update_layout(title='Cryptocurrency Performance Over Time',
                      xaxis_title='Date',
                      yaxis_title='Index Value')

    return fig

@app.callback(
    dash.dependencies.Output('Composition', 'children'),
    [dash.dependencies.Input('Composition', 'id')]
)
def update_donut_chart(_):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.2)])

    fig.update_layout(title='Composition',
                      width=350,
                      height=350,
                      title_x=0.5,  
                      margin=dict(t=50, b=50, l=50, r=50))  

    return dcc.Graph(figure=fig)
@app.callback(
    dash.dependencies.Output('Sectoral Composition', 'children'),
    [dash.dependencies.Input('Sectoral Composition', 'id')]
)
def update_sunburst_chart(_):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/sales_success.csv')
    levels = ['salesperson', 'county', 'region']  # Les niveaux utilisés pour le graphique hiérarchique
    color_columns = ['sales', 'calls']
    value_column = 'calls'

    # Fonction pour construire le DataFrame hiérarchique
    def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
        """
        Construire une hiérarchie de niveaux pour les graphiques Sunburst ou Treemap.
        """
        df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
        for i, level in enumerate(levels):
            df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
            dfg = df.groupby(levels[i:]).sum()
            dfg = dfg.reset_index()
            df_tree['id'] = dfg[level].copy()
            if i < len(levels) - 1:
                df_tree['parent'] = dfg[levels[i+1]].copy()
            else:
                df_tree['parent'] = 'total'
            df_tree['value'] = dfg[value_column]
            df_tree['color'] = dfg[color_columns[0]] / dfg[color_columns[1]]
            df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
        total = pd.Series(dict(id='total', parent='',
                               value=df[value_column].sum(),
                               color=df[color_columns[0]].sum() / df[color_columns[1]].sum()))
        df_all_trees = df_all_trees.append(total, ignore_index=True)
        return df_all_trees

    # Construction du DataFrame hiérarchique
    df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
    average_score = df['sales'].sum() / df['calls'].sum()

    # Création du graphique Sunburst
    fig = go.Figure(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        marker=dict(
            colorscale='RdBu',
            cmid=average_score),
        hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
        maxdepth=2  # Exclure la dernière couche
    ))

    # Mise à jour du layout
    fig.update_layout(title='Sectoral Composition',  # Titre du graphique
                      title_font=dict(family='Open Sans', size=16, color='#2478F6'),  # Style du titre
                      width=280,  # Largeur du graphique
                      height=280,  # Hauteur du graphique
                      title_x=0.5,  # Alignement du titre au centre
                      margin=dict(t=40, b=40, l=40, r=40))  # Marges

    return dcc.Graph(figure=fig)


@app.callback(
    dash.dependencies.Output('Annualized Returns', 'children'),
    [dash.dependencies.Input('Annualized Returns', 'id')]
)
def update_bar_chart(_):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months,
        y=[20, 14, 25, 16, 18, 22, 19],
        name='Primary Product',
        marker_color='#2478F6'
    ))
    fig.add_trace(go.Bar(
        x=months,
        y=[19, 14, 22, 14, 16, 19, 15],
        name='Secondary Product',
        marker_color='#5CA6F6'
    ))

    fig.update_layout(
        title='Annualized Returns',  # Titre du graphique
        title_font=dict(family='Open Sans', size=16, color='#2478F6'),  # Style du titre
        width=400,  # Largeur du graphique
        height=280,  # Hauteur du graphique
        title_x=0.5,  # Alignement du titre au centre
        margin=dict(t=40, b=40, l=40, r=40),  # Marges
        barmode='group',  # Mode de regroupement des barres
        xaxis_tickangle=-45  # Angle d'inclinaison des étiquettes de l'axe x
    )

    return dcc.Graph(figure=fig)


@app.callback(
    dash.dependencies.Output('Current Holdings', 'children'),
    [dash.dependencies.Input('Current Holdings', 'id')]
)
def update_sunburst_chart(_):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/sales_success.csv')
    levels = ['salesperson', 'county', 'region']  # Les niveaux utilisés pour le graphique hiérarchique
    color_columns = ['sales', 'calls']
    value_column = 'calls'

    # Fonction pour construire le DataFrame hiérarchique
    def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
        """
        Construire une hiérarchie de niveaux pour les graphiques Sunburst ou Treemap.
        """
        df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
        for i, level in enumerate(levels):
            df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
            dfg = df.groupby(levels[i:]).sum()
            dfg = dfg.reset_index()
            df_tree['id'] = dfg[level].copy()
            if i < len(levels) - 1:
                df_tree['parent'] = dfg[levels[i+1]].copy()
            else:
                df_tree['parent'] = 'total'
            df_tree['value'] = dfg[value_column]
            df_tree['color'] = dfg[color_columns[0]] / dfg[color_columns[1]]
            df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
        total = pd.Series(dict(id='total', parent='',
                               value=df[value_column].sum(),
                               color=df[color_columns[0]].sum() / df[color_columns[1]].sum()))
        df_all_trees = df_all_trees.append(total, ignore_index=True)
        return df_all_trees

    # Construction du DataFrame hiérarchique
    df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
    average_score = df['sales'].sum() / df['calls'].sum()

    # Création du graphique Sunburst
    fig = go.Figure(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        marker=dict(
            colorscale='RdBu',
            cmid=average_score),
        hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
        maxdepth=2  # Exclure la dernière couche
    ))

    # Mise à jour du layout
    fig.update_layout(title='Sectoral Composition',  # Titre du graphique
                      title_font=dict(family='Open Sans', size=16, color='#2478F6'),  # Style du titre
                      width=280,  # Largeur du graphique
                      height=280,  # Hauteur du graphique
                      title_x=0.5,  # Alignement du titre au centre
                      margin=dict(t=40, b=40, l=40, r=40))  # Marges

    return dcc.Graph(figure=fig)

@app.callback(
    dash.dependencies.Output('Volatility_plot', 'figure'),
    [dash.dependencies.Input('Volatility_plot', 'id')]
)
def update_graph(_):
    trace1 = go.Scatter(x=df['Date'], y=df['Bitcoin_2022'], mode='lines',showlegend=False, name='Bitcoin 2022')
    trace2 = go.Scatter(x=df['Date'], y=df['Native Tokens_2022'], mode='lines', showlegend=False, name='Native Tokens 2022')
    
    trace3 = go.Scatter(
        x=df['Date'], y=df['Native Tokens AI Autopilot Prudent_2022'],
        mode='lines', name='Prudent 2022',
        line=dict(color='blue'), 
        fill='tonexty', 
        showlegend=False,
        fillcolor='rgba(173,216,230,0.4)' 
    )
    trace4 = go.Scatter(
        x=df['Date'], y=df['Native Tokens AI Autopilot Risky_2022'],
        mode='lines', name='Risky 2022',
        line=dict(color='navy'), 
        fill='tonexty',
        showlegend=False,
        fillcolor='rgba(0,0,255,0.4)' 
    )

    # Combine traces into a figure
    fig1 = go.Figure(data=[trace1, trace2, trace3, trace4])
    fig1.update_layout(title='Volatility Over Time',
                      xaxis_title='Date',
                      yaxis_title='Index Value')

    return fig1



@app.callback(
    [Output('header-section', 'style'),
     Output('smartfolio_description', 'style'),
     Output('NB-description', 'style'),
     Output('AI_vs_FullExposure', 'style'),
     Output('No-Conflict-of-Interest', 'style'),
     Output('Guarantee-Disclaimer', 'style'),
     Output('color-band-description', 'style'),
     Output('time-series-chart', 'style'),
     Output('Exposure-description', 'style'),
     Output('Information-only-description', 'style'),
     Output('Composition', 'style')],
    [Input('tabs', 'value')]
)
def toggle_components(tab):
    if tab == 'overview':
        header_style = {
            'fontSize': '18px',
            'padding': '20px',
            'textAlign': 'center',
            'margin': '0 auto',
            'width': '80%',
            'display': 'flex',
            'justifyContent': 'space-between',
            'alignItems': 'center',
            'color': '#0F73F8'
        }
        description_style = {
            'backgroundColor': 'white',
            'color': '#333',
            'padding': '10px 60px',
            'margin': '20px 100',
        }
        NB_description_style = {
            'padding': '0px 0',  
            'color': '#A6A6A6', 
            'fontSize': '10px',
            'padding': '10px',  
            'backgroundColor': '#FFF',  
            'borderBottom': '0px solid #DDD',
            'marginTop': '0px',
            'textAlign': 'center'  
        }
        AI_vs_FullExposure_style = {
        'border': 'solid',
        'borderWidth': '2px',
        'borderColor': '#0F73F8',  
        'backgroundColor': 'white',  
        'padding': '10px',  
        'margin': '10px 10', 
        'position': 'relative',
        'left': '5%',
        'width': '60%' 
        }
        No_Conflict_of_Interest_style = {
            'backgroundColor': 'white',
            'color': '#333',
            'padding': '0px',
            'margin': '0px 0' 
        }
        Guarantee_Disclaimer_style = {
        'padding': '0px',  
        'color': '#A6A6A6', 
        'fontSize': '10px',
        'backgroundColor': '#FFF',
        'marginBottom': '0px'  # This is set to 0px to reduce space
        }
        color_band_description_style = {
        'backgroundColor': 'white',
        'color': '#333',
        'padding': '0px 75px', 
        'margin': '0px 0',  
        'textAlign': 'center' 
        }
        exposure_description_style = {
            'padding': '0px',
            'color': '#A6A6A6',
            'fontSize': '10px',
            'backgroundColor': '#FFF',
            'borderBottom': '0px solid #DDD',
            'marginTop': '0px',
            'textAlign': 'center',
            'position': 'absolute',
            'right': '1%',
            'top': '50%', 
            'transform': 'translateY(-50%) rotate(90deg)',
            'transform-origin': 'top right', 
        }
        information_only_style = {
            'padding': '0px',
            'color': '#A6A6A6',
            'fontSize': '10px',
            'backgroundColor': '#FFF',
            'marginTop': '0px',
            'textAlign': 'center',
            'position': 'relative',
            'right': '99%',
            'top': '50%', 
            'transform': 'translateY(50%) rotate(-90deg)',
            'transform-origin': 'top right', 
        }
        composition_style = {
            'backgroundColor': 'white',
            'color': '#333',
            'padding': '0px 75px', 
            'margin': '0px 0',  
            'textAlign': 'center' 
        }

    
        return header_style, description_style, NB_description_style,   AI_vs_FullExposure_style, No_Conflict_of_Interest_style, Guarantee_Disclaimer_style, color_band_description_style , {'display': 'block'}, exposure_description_style, information_only_style, composition_style
    else:
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'} , {'display': 'none'} , {'display': 'none'} , {'display': 'none'} , {'display': 'none'} , {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}

# @app.callback(
#     [],
#     [Input('tabs', 'value')]
# )
# def toggle_components(tab):
#     if tab == 'price-performance':
#         return 
#         return 
    
@app.callback(
    [Output('Sectoral Composition', 'style'),
     Output('Annualized Returns', 'style'),
     Output('Current Holdings', 'style'),
     Output('line1','style'),
     Output('volatility_metric','style'),
     Output('Volatility_definition','style'),
     Output('Volatility_plot','style')],
    [Input('tabs', 'value')]
)
def toggle_components(tab):
    if tab == 'metrics':
        # container_style = {
        #     'display': 'flex',  # Set display to flex
        #     'justifyContent': 'space-between',  # Distribute items along the main axis (horizontally)
        #     'alignItems': 'center',  # Center items along the cross axis (vertically)
        # #     'width': '100%',  # Ensure the container spans the entire width
        # }
        sectorial_composition_style = {
            'backgroundColor': 'white',
            'color': '#333',
            'padding': '0px 75px', 
            'margin': '0px 0',  
            'textAlign': 'left' 
        }
        annualized_returns_style = {
            'backgroundColor': 'white',
            'color': '#333',
            'padding': '0px 75px', 
            'margin': '0px 0',  
            'textAlign': 'center' 
        }
        current_holdings_style = {
            'backgroundColor': 'white',
            'color': '#333',
            'padding': '0px 75px', 
            'margin': '0px 0',  
            'textAlign': 'right' 
        }
        line_1_style = { 'display': 'flex', 'justifyContent': 'center', 'background-color': '#0F73F8', 'width': '200%', 'height': '2px', 'margin': '20px 0'}
        volatility_metric_style = {'display': 'flex', 'justifyContent': 'space-between'}
        volatility_definition_style = {'flex': '1', 'textAlign': 'left'}
        volatility_plot_style = {'flex': '1', 'textAlign': 'right'}
        return sectorial_composition_style, annualized_returns_style, current_holdings_style, line_1_style, volatility_metric_style, volatility_definition_style, volatility_plot_style
    else:
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display':'none'},{'display':'none'},{'display':'none'},{'display':'none'}



if __name__ == '__main__':
    app.run_server(debug=True)
    
