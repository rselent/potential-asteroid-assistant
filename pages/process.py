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
			
			I want to preface this section by drawing attention to that word above: 
			**Process**. Very much like in art, a process is neither supposed to be quick 
			nor easy. So this will not be a short or digestible blog post, either. This 
			will be a declaration of *my process* with this project -- my thoughts, 
			concerns, results, how I dealt with those and various other related things, 
			and how I connected not just with the data, but ultimately, how I bring 
			that story to you as well. 
			
			That said, go get a snack, get some coffee, and I 
			hope you enjoy this peek behind the proverbial curtain.
			
			----- 
			
			-----
			"""
			
			"""
			&nbsp;
			
			#### Interest
			
			As an artist and someone who has studied art most of their life, 
			whenever I approach a project like this, I'm often inundated with 
			creative thoughts of "*Wouldn't it be cool if...*"
			
			"*Wouldn't it be cool if?*"
			
			Wouldn't it be cool if I could create something that could help 
			with literally **saving the planet**?
			
			I was attracted to doing this project specifically when I stumbled across 
			a dataset on Kaggle. Another user had done something similar, and the
			dataset seemed quite interesting (and quite new). Combining both domain knowledge
			I had already possessed and active, ongoing research, I spent a few days 
			investigating, exploring, and cleaning their dataset, which they had generated
			utilizing NASA Jet Propulsion Laboratory's *Small-Body Database Search Engine*.
			
			Through my exploration and investigation, I began to feel aspects of their dataset 
			were becoming inadequate, so I decided to try generating my own dataset directly from 
			NASA-JPL's Small Body Database. Through selecting the same features as the baseline 
			Kaggle set and adding the few more I was searching for, I had found success!
			
			And almost 100,000 more observations, too!
			
			In total, I had generated a dataset that contained almost 1,000,000 observations 
			across over 30 features -- quite the jump from the last project I had done, 
			which had an absolutely-massive-at-the-time *50,000* observations. 
			Coincidentally, that previous project had also been my *first* 
			actual data science project ever. Quite the jump, indeed.
			
			-----
			"""
			
			"""
			&nbsp;
			
			#### Incite
			
			After re-exploring my shiny, new, *hot-off-the-presses* dataset, direct 
			from the venerable JPL and packed with with new data like *1-sigma 
			uncertainty values*, I had unfortunately surmised that I'll still have 
			to drop about half of its features. *Womp womp*.
			
			To be fair, most of these features had massively incomplete data, on the 
			order of 80% NaN values. One feature even had just 8 (*eight*) real values 
			recorded. Out of almost 1 million observations. With the objective that I 
			had in mind and the more-complete domain knowledge I now possessed, I made 
			the judgment that perhaps it would be better or even acceptable for me 
			to drop these features entirely, instead of imputing or trying to fill in 
			such wholly incomplete data and potentially tainting the following process 
			or, worse, the results. 
			
			Little did I know, I would have to consider this decision again when 
			my *target*, the very feature I intend to predict, reminded me that it 
			still had almost 40,000 missing values. I felt like this was an even 
			larger moral quandary. The only **logical** (or *least amoral*?) solution was 
			to drop all 40,000 of those observations. But if I did that, that's 40,000 
			objects that could *potentially* harm someone on this planet.
			
			I compromised with my conscience by assigning those 40,000 observations to 
			a separate, tertiary subset, that I could make blind predictions on as 
			an ultimate stretch goal.
			
			Once I started getting down to the "real work," right off the bat, I got my 
			baseline. Accuracy. Alright fam, we got this.  
			...  
			0.23%. 1/4 of a percent. What?? This really threw me for a loop. Almost 
			900,000 observations -- 900,000 recorded asteroids -- and only ~2,000 of 
			them are actually classified as Potentially Hazardous?? I knew space was big 
			(*spaaaaaaaace*), but that still shocked me. For a brief moment, I reflected 
			on those 40,000 observations I set aside and thought, "*What if*." 
			Thankfully, my reflection quickly broke, lest I revisit that moral conundrum. 
			Clearly I'd need another way to evaluate my models, as it's just too heavily imbalanced.

			-----
			"""
			
			"""
			&nbsp;
			
			#### Inquire
			
			The project rubric required that I build / fit / train a linear model, 
			regardless of my lack of confidence in its ability to produce desirable 
			results with this dataset. Sure enough, the best accuracy 
			score I was able to produce with a linear Logistic Regression model was 
			approximately 99.76% -- close to being a perfect complement to my baseline. 
			Interesting, but unhelpful. I felt compelled to inspect the feature 
			weights or coefficients that the model was assigning, and much to my chagrin 
			they made little sense: orbital class was very positively weighted, which 
			was expected, but other features like an asteroid's perihelion (q), 
			Minimum Orbit Intersection Distance, absolute magnitude (H), or its orbital 
			condition code were weighted *negatively*. What?? Those latter features 
			should be far more important than that!

			Naturally, this evoked more curiosity and research, and following along 
			with the rubric, I constructed a pipeline to fit a Random Forest model -- it's 
			another model we were explicitly taught how to use after all, so there should 
			be no issues. Lo and behold, however, it produced a validation accuracy of 
			a whopping *99.994%*! If that isn't *beating the baseline*, I don't know what is.
			
			Clearly, something was going on here, though. Both a linear model *and* a 
			tree-based model are behaving like this? Something didn't feel right. 
			As I was bringing up my concerns about the results with both my Team and
			Section Leads, I was also in tandem building *another* pipeline. 
			The few methods we had been taught (with sound reason, I'll add) just 
			did not seem to be serving me well in this instance, so maybe I needed to 
			think (and eventually reach... and then climb) outside the proverbial box 
			a little. 

			-----
			"""
			
			"""
			&nbsp;
			
			#### Incept
			
			It started with research -- a *lot* of research. This was a horrible decision 
			with regards to time management, given that we are only allotted a week to build this project, 
			but I felt I had no other choice. I could've accepted my fate (or rather, 
			the fate of my predictive models thus far), but if that was truly to be 
			my fate with this project, I was going to make Fate work *damn hard* to 
			get her way. So, as a method to confirm the model behaviours that I've 
			been seeing so far, I chose *another* linear model: Perceptron. Up until now, 
			I haven't been altering or forcing parameters all that much -- outside of n_jobs 
			(for expedience), random_state (for reproducibility), and such -- because my 
			guiding principle for this project was "find a model that fits my needs first," 
			as every other dataset that I've worked with while here at Lambda School has 
			had relatively balanced prediction targets and has thus been, well, comparatively "easy." 
			
			Surprisingly, Perceptron produced the same sort of results that my previous 
			two attempts had thrown at me, except this model was perfectly, right on the money: 
			99.77% accuracy. By this point I'm thinking to myself, "*This is way too convenient; 
			this is a perfect complement to my baseline.*" 
			
			When my Team and Section Leads got back to me with their recommendations of 
			abandoning the accuracy score evaluation metric in favour of something 
			a bit more minority- or recall-friendly -- like Precision-Recall or 
			F-scores -- they also suggested I plot ~~to take over the world~~ 
			a confusion matrix, to see what's really going on beneath the surface; 
			to see what kind of predictions this and the rest of my models were truly making. 
			It's probably better to just *show* you the results.
			
			< Confusion matrix goes here, because words just can't describe >
			
			Just like Owen Wilson, "*Wow*," was my first reaction. I mean, It's not 
			making *any* 'yes' predictions. At all.	And in that moment I truly 
			understood the value of confusion matrices, which just a few weeks ago 
			were, well, *confusing me* to no end. 
			
			Additionally, while researching how to calculate a digestible precision-recall 
			score, I had learned about precision-recall curves and what they can tell 
			us about how a model reacts to a dataset. 
			
			< PRC goes here >
			
			In short, this curve, along with the confusion matrix from earlier, tells 
			me that this kind of model is just not a good *fit* for this kind of heavily 
			unbalanced prediction. 
			
			So, what kind of model *would* be a good fit, then?
			
			-----
			"""
			
#			INSIGHTS:  (split into 2 sections: 1) about question/space, 2) about data/process
#			
#			* 'Oumuamua's trajectory, when it was discovered 
#			* the asteroid that wiped out the dinosaurs was only 10km in diameter (e.g. the length of Manhattan)
#			* 
#			
#			* If you think about a confusion matrix like a top-down view, then a PRC is a side view 
#			* When a PRC is a flat line like this
#			* 
#			
#			
			
			"""
			
			#### Intuition
			
			I've been playing video games for a long time -- ever since I was an infant, 
			basically. And as a gamer, my interest in data science before joining 
			Lambda School has kind of been casual and perfunctory, as for a time, 
			machine learning and gaming had	kind of a big intersection. Through a 
			push from GPU manufacturers AMD (then ATI) and Nvidia towards 
			building what are called General-Purpose GPUs, 
			
			
			
			-----
			"""

		),

	],
)

layout = dbc.Row([column1])