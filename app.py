from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('knn_best.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_salary():
    ClumpThickness = int(request.form.get('Clump Thickness'))
    UniformityOfCellSize = int(request.form.get('Uniformity of Cell Size'))
    UniformityOfCellShape = int(request.form.get('Uniformity of Cell Shape'))
    MarginalAdhesion = int(request.form.get('Marginal Adhesion'))
    SingleEpithelialCellSize = int(request.form.get('Single Epithelial Cell Size'))
    BareNuclei = int(request.form.get('Bare Nuclei'))
    BlandChromatin = int(request.form.get('Bland Chromatin'))
    NormalNucleoli = int(request.form.get('Normal Nucleoli'))
    Mitosis = int(request.form.get('Mitosis'))


    # prediction

    result = model.predict(np.array([ClumpThickness, UniformityOfCellSize, UniformityOfCellShape,
                                     MarginalAdhesion, SingleEpithelialCellSize, BareNuclei, BlandChromatin,
                                     NormalNucleoli, Mitosis]).reshape(1, 9))

    if result[0] == 2:
        output="Benign"
    else:
        output="Malignant"



    return render_template('index.html', prediction_text=f'Cancer is {output}')


if __name__ == '__main__':
    app.run(debug=True)