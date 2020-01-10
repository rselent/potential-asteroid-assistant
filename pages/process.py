# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process
            
            -----
            
            #### Interest
            
            I was originally attracted to doing this project when I stumbled across 
            an entry on Kaggle. Another user had done something similar, and the
            dataset seemed quite interesting. I had spent 1-2 weeks investigating,
            exploring, and cleaning their dataset -- utilizing both domain knowledge I 
            had already possessed and active research -- which they had generated
            utilizing Jet Propulsion Laboratories' own *Small-Body Database Search Engine*.
            
            After that initial time, I had found aspects of that dataset inadequate, so I
            decided to try generating my own dataset from JPL. Utilizing the same
            features as the Kaggle set, and adding a couple more (what I was looking for),
            I had found success!
            
            And almost 100,000 more observations!
            
            #### 


            """
        ),

    ],
)

layout = dbc.Row([column1])