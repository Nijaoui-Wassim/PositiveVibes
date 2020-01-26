===================
PositiveVibes
===================


Quick Start
===================
pip install vaderSentiment,tensorflow==1.4.0
pip install vaderSentiment
Follow the documentation for GPT2: https://github.com/openai/gpt-2
Add the GPT2 Master folder to your Path
install all the requirements for GPT2
pip install python-facebook-api

And get a user Facebook Graph API Acess Toke :
https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999

And replace the existing token in the file facebook.py


Test:
python facebook.py


Inspiration
===================

We spent a good part of our day surfing through the internet. So why not make use of it? Our approach was to tackle mental health well-being in our society using activities on social media. In fact, our app downloads youtube, twitter and facebook posts & comments, scans it, determine its feeling using an AI and if that post or comment is have a sad or depressive value then we take that input and generate a customized comment to support that user. This text won’t be just any random text, but it would be a positive generated text through an AI. This app would be called PositveVibes. 
What it does
It essentially works with social media platforms. In fact, when you go online you can help someone! You can make someone’s day :D With your permission, our app would download the posts and comments using facebook, twitter and youtube APIs, check the post’s feeling using the AI  VaderSentiment, and if the AI determines that the post is sad, depressive or simply needs help, than it would use that as an input to generate a helping reply using AI GPT2 then.  This app could be an efficient and cheaper solution to cyberbullying since it doesn’t require monitoring. This app could also detect hate speech and reply to it in a proper way … In this demo it could even try to convince them to change their behavior!!  
It is a great app, with more work it could be a powerful tool to promote mental health well-being and fight cyberbullying. #PositveVibes

How we built it
===================
I decided to separate the job into 3 tasks.
First, getting the data from the platforms using facebook, twitter and youtube APIs. 
Second, run that data through the AI that detects feelings to determine whether that post’s owner needs help.( The API gives the post a score from -1 to 1)
Finally, get a proper reply using the AI than posting it as well as logistics like the overall appearance of the app, the logo, the presentation and everything that revolves around that. I used mostly Python to create the app.

 

Challenges we ran into
===================

-Youtube API is limited. 
-The open source AI GPT2 is very powerful tool to generate text. It kept surprising us with its unexpected outputs! This power made it hard to manipulate its behavior. Can you imagine that the power of an AI might be a challenge!!  
Then we have the obvious debugging problems. 
Accomplishments that I'm proud of
Collecting large amount of data using different APIs, using different AIs to detect feelings based on text and generating customized reply with a real powerful AI. An AI that you would think twice before admitting that an AI said it!
We're extremely proud of the amount of work delivered in such a short amount of time and we can't wait to continue developing this idea post hackathon.
What we learned
Using different APIs and various AI.
What's next for PositiveVibes
The next step for PositiveVibes is to continue optimizing our engine to produce more accurate results. 
Scale the results and use the same approuch using diffrents others APIs
From Facebook, youtube to Instagram, Reddit... we have to reach them and be There for them

