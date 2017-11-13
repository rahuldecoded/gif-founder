# GIF FOUNDER

## Installation
1. Install Python3
2. Create an virtual environment. `virtualenv -p python3 venv`
3. Activate the virtal environment. `source activate venv`
4. Install the required packages. `pip install -r requirements.txt`
5. Run the application. `python run.py`


#### Explanation for beginner/non-coder
Here, there are two main Python Scripts run.py and engine.py
1. run.py - this is the core part. I'm using Flask(web microframework), from here the invoked requests are get maintained.
2. engine.py - here I'm making the API calls and filttering the json response that we get from the API call and returning the required data to the run.py
