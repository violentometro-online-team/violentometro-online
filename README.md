# violentometro-online

`Violentómetro Online` is a web app that detects Spanish hate-speech against women online.

In case you want to use our model in your experiments, you can do so with the following code:

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("violentometro/violentometro-model")

model = AutoModel.from_pretrained("violentometro/violentometro-model")
```

To learn more about the project, see the article [Detecting gender-based hate speech in Spanish with Natural Language Processing](https://medium.com/@alejandra.pedroza/detecting-gender-based-hate-speech-in-spanish-with-natural-language-processing-cdbba6ec2f8b).

We would like to express our gratitute to the organizers of [MEX-A3T](https://sites.google.com/view/mex-a3t/) for sharing a labeled dataset for this work.

## Repo Structure

Our repo is structured in a way that enables the visitors explore how a Data Science project is often managed, starting from the Exploratory Data Analysis stage to deployment of a web app.

## Data

For this project, we used two datasets. One dataset contains comments from Facebook that was compiled by one of the team members. The second dataset was kindly provided by the research group who is organizing [MEX-A3T](https://sites.google.com/view/mex-a3t/). 

>Note: The results may not be reproducible because the dataset that was provided by the research group mentioned above cannot be shared publicly.

## Web App

Our app has its own README in its directory.
