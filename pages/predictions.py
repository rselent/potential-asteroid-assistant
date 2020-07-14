# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
import pandas as pd
from catboost import CatBoostClassifier


# pipeline = load( 'assets/lightPred.joblib')		# cannot use LightGB model -- model dumped incorrectly 
nyanline = load( 'assets/nyanPred.joblib')

@app.callback(
	Output( 'prediction-content', 'children'),
	[Input( 'nyanCode', 'value'), Input( 'nyanNeo', 'value'), Input( 'nyanClass', 'value')],
)
def nyanPredict( nyanCode, nyanNeo, nyanClass):
	df = pd.DataFrame(
		columns= ['condition_code', 'neo', 'class'],
#		cat_features= ['condition_code', 'neo', 'class'],
		data= [[nyanCode, nyanNeo, nyanClass]]
	)
	yPred = nyanline.predict( df)
	return yPred


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
	[
		dcc.Markdown(
			"""
			## Prediction Assistant (lite)

			This tool is built to analyze three pre- categorized features of an asteroid, 
			and then determine whether that asteroid is potentially hazardous to life
			on Earth.  
			Those three categories are the asteroid's:
			
			* Condition Code
			* Class, and
			* Near-Earth Object status
			
			Instructions:
			
			Change each variable until they correspond with the attributes of a
			chosen asteroid, and the assistant will determine, to the best of its
			ability, whether the asteroid can also be classified as a 
			Physically Hazardous Asteroid or not.
			""",
			className= 'wrx',
		),

    ],
    md=4,
)

column2 = dbc.Col(
    [
#		html.Label('Condition Code'),
		dcc.Markdown(
			"""
			-----

			#### Condition Code
			
			"""
		),
		dcc.Slider(
			id='nyanCode',
			min= 0,
			max= 9,
			step= 1,
			marks= {i: '{}'.format(i) for i in range(10)},
			value= 3,
			className= 'wrx',
		),

#		html.Label('Near-Earth Object'),
		dcc.Markdown(
			"""
			&nbsp;

			&nbsp;

			-----

			#### Near-Earth Object
			"""
		),
		dcc.Checklist(
			id='nyanNeo',
			options=[
					{'label': ' Yes', 'value': 'Y'},
					{'label': 'No', 'value': 'N'},
					],
			#value= 'Y',
			labelStyle= {'margin-left': '12px'},
			style={'display': 'inline-block'},
			className= 'wrx',
		),

		dcc.Markdown(
			"""
			&nbsp;

			&nbsp;

			-----
			
			#### Class
			"""
		),

#		html.Label('Class'),
		dcc.RadioItems(
			id='nyanClass',
			options=[
				{'label': 'Main-Belt Asteroid', 'value': 'MBA'},
				{'label': 'Outer Main-Belt Asteroid', 'value': 'OMB'},
				{'label': 'Inner Main-Belt Asteroid', 'value': 'IMB'},
				{'label': 'Mars-Crossing Asteroid', 'value': 'MCA'},
				{'label': 'Apollo', 'value': 'APO'},
				{'label': 'Amor', 'value': 'AMO'},
				{'label': 'Jupiter Trojan', 'value': 'TJN'},
				{'label': 'TransNeptunian Object', 'value': 'TNO'},
				{'label': 'Aten', 'value': 'ATE'},
				{'label': 'Centaur', 'value': 'CEN'},
				{'label': 'Atira', 'value': 'IEO'},
				{'label': 'Asteroid (Other)', 'value': 'AST'},
				{'label': 'Hyperbolic Asteroid', 'value': 'HYA'},
				{'label': 'Parabolic Asteroid', 'value': 'PAA'},
					],
			value= 'MBA',
			labelStyle= {'margin': '5px'},
			style= {'display': 'inline-block', 'margin-left': '7px'},
			className= 'wrx',
		),
#		html.Label('Prediction'),
		dcc.Markdown(
			"""
			-----
			-----
			"""
		),


		html.H3( 'PHA Prediction', className= 'wrx'),
		html.Div( id= 'prediction-content', className= 'lead')


	],
)

column3 = dbc.Col(
	[
		dcc.Markdown(
			"""
			-----  
			An orbit condition code (or U-uncertainty parameter) is an integer between 0 and 9
			that indicates how well-known an asteroid's orbit is, with 0 being absolute certainty. 
			The closer to 9 this value is, the more potential danger an asteroid presents.
			
			-----
			
			An asteroid is classified as a Near-Earth Object if its closest distance to the Sun is, 
			at any point, less than 1.3 astronomical units (au).  
			*1au is equal to the mean distance between the Earth and the Sun.*
			
			-----
			
			An asteroid's class describes its orbit -- where it likes to hang out in the solar system. 
			Because of this, only certain classes are typically capable of becoming an NEO. More insight
			and class definitions will be able to be found on the Insights tab in the near future.
			""",
			className= 'wrx',
		),

	],
)



layout = dbc.Row( [column1, column2, column3])