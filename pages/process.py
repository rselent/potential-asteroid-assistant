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
            
            As an artist and as someone who has studied art most of their life, 
            whenever I approach a project like this, I'm often inundated with 
            creative thoughts of "*Wouldn't it be cool if...*"
            
            "*Wouldn't it be cool if..?*"
            
            Wouldn't it be cool if I could create something that could help 
            with literally **saving the planet**?
            
            I was attracted to doing this project specifically when I stumbled across 
            a dataset on Kaggle. Another user had done something similar, and the
            dataset seemed quite interesting (and quite new). I had spent 1-2 weeks investigating,
            exploring, and cleaning their dataset -- combining both domain knowledge I 
            had already possessed and active research -- which they had generated
            utilizing Jet Propulsion Laboratories' own *Small-Body Database Search Engine*.
            
            Through my exploration and investigation, I began to feel aspects of that dataset 
            were becoming inadequate, so I decided to try generating my own dataset from JPL. 
            Through selecting the same features as the baseline Kaggle set, and adding 
            the few more I was searching for, I had found success!
            
            And almost 100,000 more observations, too!
            
            -----
            
            #### Shock
            
            In total, I had selected a dataset that contained almost 1,000,000 observations --
            quite the jump from the last project I had done, which had an 
            absolutely-massive-at-the-time-50,000 observations. Coincidentally, that previous
            project had also been my first *actual* data science project ever.


            """
        ),

    ],
)

layout = dbc.Row([column1])