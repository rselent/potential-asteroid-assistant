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
            
            In total, I had generated a dataset that contained almost 1,000,000 observations 
            across over 30 features -- quite the jump from the last project I had done, 
            which had an absolutely-massive-at-the-time *50,000* observations. 
            Coincidentally, that previous  project had also been my *first* 
            actual data science project ever. Quite the jump, indeed.

			-----
            
            #### Shock
            
            After re-exploring my shiny, new, *hot-off-the-presses* dataset, direct  
            from the venerable *JPL* and packed with with new data like *1-sigma 
            uncertainty values*, I had almost immediately surmised that I'll still 
            have to drop about half of its features. *Womp womp*.
            
            To be fair, most of these features had massively incomplete data, on the 
            order of 80% NaN values. One feature even had just 8 (*eight*) real values 
            recorded. Out of almost 922,000 observations. I made the judgment that 
            perhaps -- with the objective that I had in mind and the more-complete domain 
            knowledge I now possessed -- it would be better or even acceptable for me 
            to drop these features entirely, instead of imputing or trying to fill in 
            such wholly incomplete data and potentially tainting the following process 
            or, worse, the results. 
            
            Little did I know, I would have to consider this decision again when 
            my *target*, the very feature I intend to predict, reminded me that it 
            still had almost 40,000 missing values. I felt like this was an even 
            larger moral quandary. The only **logical** (or least amoral?) solution was 
            to drop all 40,000 of those observations. But if I did that, that's 40,000 
            objects that could *potentially* harm someone on this planet.
            
            I compromised with my conscience by assigning those 40,000 observations to 
            a separate, tertiary subset, that I could make blind predictions on as 
            an ultimate stretch goal.
            
            -----
            
            Once I started getting down to the "real work," right off the bat, I got my 
            baseline. Accuracy. Alright fam, we got this.  
            ...  
            0.23%. 1/4 of a percent. What?? This really threw me for a loop. Almost 
            900,000 observations -- 900,000 recorded asteroids -- and only ~2,000 of 
            them are actually classified as Potentially Hazardous?? I knew space was big 
            (*spaaaaaaaace*), but that still shocked me. For a brief moment, I reflected 
            on those 40,000 observations I set aside and thought, "*What if*." 
            My reflection broke quickly though, thankfully (lest I revisit that moral 
            conundrum). Clearly I'd need another way to evaluate my models, as it's 
            just too heavily imbalanced.
            
            -----
            
            The project's rubric required that I build / fit / train a linear model, 
            regardless of my confidence in how much it *wouldn't* produce desirable 
            results... with this dataset, I mean. Sure enough, the best accuracy 
            score I was able to produce with a Logistic Regression model was 
            approximately 99.76% -- almost a perfect (inverse) complement to my 
            'baseline'.
            
            
            
            


            """
        ),

    ],
)

layout = dbc.Row([column1])