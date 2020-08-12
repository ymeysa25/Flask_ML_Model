from flask import Flask,request, render_template
import joblib
from io import TextIOWrapper
import csv
import numpy as np

app = Flask(__name__, template_folder='templates')

# Load Model
model = joblib.load('Text_classificationfix.txt')

#declare label
labels = ['POSITIF', 'NEGATIF']

values = [ 56, 77]

colors = ["#F7464A", "#46BFBD"]

def count_element(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0)+1
    return hist


#Route home
@app.route("/")
def my_form():
    # template HTML
    return render_template("index.html")

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


@app.route('/upload',methods = ['POST'])
def upload_csv():
    data_test = []
    if request.method == 'POST':
        csv_file = request.files['fileupload']
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

    return render_template('bar_chart.html', title='SVM Predicted Result', max=max(bar_values) + 20, labels=bar_labels, values=bar_values)
#run app
if __name__ == "__main__":
    app.run(debug=True)