# Fraud Detection Case Study

*Apologies if these notes seem terse... Consider this a first draft.*

This is a case study from the Galvanize Data Science Immersive program. I worked on this with two other students. My portion of the project was to build the predictive model, including a data preparation pipeline (see, "DataPrep.py") and pickling the model for future use in a web interface. My partners also pursued a few potential models, but ultimately they focused on building the web interface portion.

EDA showed the dataset labels were approximately 9% positive (1, or "Fraud"), and 91% negative (0, or "Not Fraud"). This formed our baseline for accuracy, as we'd expect a naive model of simply predicting "Not Fraud" for all cases to be ~91% accurate. This also means our models needed to account for the imbalanced classes.

The instructions indicated downsides to both false positives and false negatives. False positives incur investigative costs and erode the trust and good will of the client's customers. More obviously, false negatives allow fraud to go unstopped. The case study parameters did not offer any guidance one managing the trade-off between the two. Personally, I think minimizing false negatives should take priority. Honest and effective communication efforts can mitigate the effects on customer trust and good. Consequently, I focused on minimizing false negatives rather than overall model accuracy.

**Logistic Regressions**  
The results were .... meh. These models seemed reluctant to flag anything as fraud. 

**Random Forests**  
Much Better. A random forest model (200 trees, leaf size 1, entropy information again, decision rule: if predicted probability > 0.3 then 'Fraud') produced false positive predictions 1.7% of the time, and false negatives occurred at 1.12% frequency.
