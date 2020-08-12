from flask import Flask, Markup, render_template

app = Flask(__name__)

labels = [
    'POSITIF', 'NEGATIF'
]

values = [56, 77]

colors = [
    "#F7464A", "#46BFBD"]

@app.route('/')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='SVM Predicted Result', max=100, labels=bar_labels, values=bar_values)

if __name__ == '__main__':
    app.run(debug=True)
