# Violentómetro Online App

A [Streamlit](https://www.streamlit.io/) app was created to showcase our model's performance.

## How to run locally

Assuming you're in a `Python 3.6.x virtualenv`:

1. `pip install -r requirements.txt`
1. `streamlit run app.py`

## Deployment process from local machine

**Note**: We're deploying the app to [Heroku](https://www.heroku.com), so its required files (`requirements.txt` and `Procfile`) were already defined.

Assuming you already installed [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):

1. `heroku login`
1. `heroku create`
1. `heroku git:remote -a <NAME_OF_THE_APP>`
1. Stage & commit the files you want to upload.
1. `git subtree push --prefix app/ heroku master`
