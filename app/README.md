# Violentómetro Online App

A [Streamlit](https://www.streamlit.io/) app was created to showcase our model's performance.

## Deployment process from local machine

**Note**: We're deploying the app to [Heroku](https://www.heroku.com), so its required files (`requirements.txt` and `Procfile`) were already defined.

1. `heroku login`
1. `heroku create`
1. `heroku git:remote -a <NAME_OF_THE_APP>`
1. Stage & commit the files you want to upload.
1. `git subtree push --prefix app/ heroku master`
