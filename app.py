from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load pipeline model (preprocessor + classifier together)
model = pickle.load(open("artifacts/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # list of columns in correct order
    columns = ['age','sex','cp','trestbps','chol','fbs','restecg',
               'thalach','exang','oldpeak','slope','ca','thal']

    # get all values from form
    data = [[
        float(request.form["age"]),
        float(request.form["sex"]),
        float(request.form["cp"]),
        float(request.form["trestbps"]),
        float(request.form["chol"]),
        float(request.form["fbs"]),
        float(request.form["restecg"]),
        float(request.form["thalach"]),
        float(request.form["exang"]),
        float(request.form["oldpeak"]),
        float(request.form["slope"]),
        float(request.form["ca"]),
        float(request.form["thal"])
    ]]

    # MAKE DATAFRAME (must do this)
    df = pd.DataFrame(data, columns=columns)

    # Predict directly → pipeline handles preprocessing
    prediction = model.predict(df)[0]

    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
