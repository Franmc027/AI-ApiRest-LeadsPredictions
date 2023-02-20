import json
from flask import Flask, request
import pickle
import pandas as pd
import sklearn

app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def predict_post():
    model = load_model()
    json_to_predict = request.get_json()
    return predict(json_to_predict, model)


def load_model():
    file = open('./models/model_RF.plk', 'rb')
    model = pickle.load(file)
    file.close()
    return model


def predict(values_to_predict, model):
    df = pd.DataFrame(values_to_predict, index=[0])
    result = model.predict(df)
    print(json.dumps({'result': result.tolist()}))
    return json.dumps({'result': result.tolist()})


if __name__ == '__main__':
    app.run(debug=True, port=8001)
