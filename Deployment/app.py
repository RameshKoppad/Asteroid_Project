import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
CBR = pickle.load(open('CBR.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Index_.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = CBR.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('Index_.html', prediction_text='result'.format(output))


#if __name__ == "__main__":
#    app.run(debug=True)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)