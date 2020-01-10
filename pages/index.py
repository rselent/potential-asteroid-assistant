# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predictions, insights, process
import pandas as pd
import plotly.express as px

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## According to NASA

            An asteroid that's just 140m wide is large enough to destroy a city.  
            And if such an asteroid was on a path to collide with Earth 
            in less than a year, the *only* option for survival is to evacuate that city. 
            
            We're discovering more and more asteroids every year, but classifying those asteroids
            and, more crucially, determining if one is potentially a danger to life on Earth or not
            still requires the same amount of time and consideration.
            
            But since time is so critical in not only making these determinations but 
            in forming potential responses as well, why not try to speed up the process where
            we can...?  

            """
        ),
        dcc.Link( dbc.Button( "Don't Panic", color= 'primary'), href= '/predictions')
    ],
    md=4,
)

#gapminder = px.data.gapminder()
#fig = px.scatter( gapminder.query( "year==2007"), x= "gdpPercap", y= "lifeExp", size= "pop", color= "continent",
#           hover_name= "country", log_x= True, size_max= 60)

df = pd.read_csv( 'https://raw.githubusercontent.com/rselent/lambda-buildweek2-asteroids/master/iForgotDateColumns.csv',
                   low_memory= False)

df = df[ df.columns.drop( 'Unnamed: 0')]         # whyisthishere, itdoesntmatter idonthavetime, fixed
df = df.dropna()
df[ df.columns[ 1]] = df[ df.columns[ 1]].replace( {'Y': 1, 'N': 0}).astype( int)
df[ df.columns[ 2]] = df[ df.columns[ 2]].replace( {'Y': 1, 'N': 0}).astype( int)

fig = px.histogram( df.where( df.neo > 0), x= 'first_obs_y', y= 'neo', range_x= (1920, 2019), cumulative= True,
                    title= 'Near-Earth Objects Recorded Over Time', labels= {'Year', 'Number of Known NEOs'})

column2 = dbc.Col(
    [
        dcc.Graph( figure= fig),
    ]
)

layout = dbc.Row( [column1, column2])