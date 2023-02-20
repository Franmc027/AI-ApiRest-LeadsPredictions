# Leads Predictions / IA-ApiRest

## ApiRest whit Flask and Python

We are going to make a model to predict if our client will be loyal or not. For this we are going to use the [LEADS](https://www.kaggle.com/datasets/ashydv/leads-dataset)  dataset from kaggle, we are also going to use Google Colab to create the model and finally we are going to use flask to make the ApiRest.

## Routemap

### Create the model

The creation of the model is in this [Collab](https://colab.research.google.com/drive/1_yDFN-MW9LRoZA9P_4jLSb6mbl-3Czso#scrollTo=qZwmK18AWdUR)

### Create the ApiRest

The code of this repository is the one needed to create the API 

### How to use?

To use the Api we can use the following command to pass a json.

```curl -H "Content-Type: application/json" -X POST -d '{"key":datos.json}' localhost:8001/predict```

One JSON file for this case is [example.json](https://github.com/Franmc027/AI-ApiRest-LeadsPredictions/blob/main/example.json).
