# Physical-Development-Tracker
The Physical Development Tracker uses the theory that muscles grow in a sigmoid curve to allow for safe physical development (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3177954/, more in depth analysis below). It takes in a goal and the estimated time to reach that goal and personalizes an exercise plan (including daily goals) for the user using a sigmoid regression. As the user continues through the program, she can input data points which the plan will refit to the curve. The program is currently being alpha tested on nursing home residents, middle aged adults, and the track team at my school to promote successful outcomes across demographics.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This program, the Physical Development Tracker, is a way to track someone's 
physical development and to set reasonable goals for them based on the 
sigmoidal curve of development. There is some research that has shown that
safe physical development happens in the shape of a sigmoidal curve. This 
program takes that sigmoidal curve and fits it to the user's data, as well as 
the expected data taken from the archetypal sigmoidal curve of development,
so as to keep a steady rate of progress going which is tailored to the user
while mitigating risk of injury from too rapid a rate of attempted development. 

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3177954/

This paper describes that the "dose-response curve in gene induction obeys a 
sigmoidal curve," and it says that the correlation between potency and maximum 
activity describe "the expression of the regulated gene in response to ligand 
concentration." This correlation manifests itself in a sigmoid curve. Since 
many developmental activities take place due to ligand-protein interactions, we 
can infer that these developmental activities will follow the same sigmoidal 
curve. However, these curves can vary. So, this curve-fitting algorithm 
(sigmoidal/logistic regression implementation) will serve to account for these 
sigmoid inconsistencies and correct them as data comes in. 
