import os
from flask import Flask, render_template, request
from pickle import load

app = Flask(__name__)

# Cargar el modelo desde la misma carpeta que app.py
model = load(open("decision_tree_classifier_diabetes.sav", "rb"))

# Diccionario de clases
class_dict = {
    "0": "Negativo en diabetes",
    "1": "Positivo en diabetes"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Obtener valores del formulario
        val1 = int(request.form['val1'])
        val2 = int(request.form['val2'])
        val3 = int(request.form['val3'])
        val4 = int(request.form['val4'])
        val5 = int(request.form['val5'])
        val6 = float(request.form['val6'])
        val7 = float(request.form['val7'])
        val8 = int(request.form['val8'])

        # Realizar la predicción
        prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])[0])
        pred_class = class_dict[prediction]

        return render_template('resultado.html', resultado=pred_class)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)