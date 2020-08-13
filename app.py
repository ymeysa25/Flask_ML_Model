from flask import Flask,request, render_template
import pickle
import numpy as np
from io import TextIOWrapper
import csv


app = Flask(__name__)


#Deklarasi label
labels = ['NEGATIF', 'POSITIF']

#load model
with open(r"svm.pickle", "rb") as input_file:
    model = pickle.load(input_file)

@app.route("/")
def my_app():
    return render_template("index.html")

def count_element(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0)+1
    return hist


#Route home when submit form from html
@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        # get input text
        text = request.form['text']

        #Predict text
        predicted = model.predict([text])[0]

    
    #send predicted to HTML
    return render_template("index.html", data = labels[predicted])


@app.route('/upload', methods = ['GET', 'POST'])
def upload_csv():
    data_test = []
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data_test.append(row)
    
    results = []
    for val in data_test:
        result =  model.predict(val)[0]
        results.append(result)

    results = np.array(results)
    
    hasil = count_element(results)
    
    bar_values= list(hasil.values())
    bar_labels= labels

    # bar_values = [100,50]

    return render_template('bar_chart.html', title='SVM Predicted Result', max=max(bar_values) + 20, labels=bar_labels, values=bar_values)

if __name__ == "__main__":
    app.run(debug=True)