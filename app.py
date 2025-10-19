import numpy as np
import pandas as pd
import joblib
from flask import Flask,request,jsonify

model = joblib.load("student_grade.pkl")

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def begin():
  return "hello, welcome"


@app.route("/predict",methods = ["POST"])
def predict():
  try:
    data = request.get_json()

    main_data = pd.DataFrame([data],columns =["hours_studied",	"attendance","previous_score","extra_classes","age","gender","parent_education_Bachelor","parent_education_College",	"parent_education_Highschool","parent_education_Masters"])

    predictions = model.predict(main_data)

    result = np.array(predictions).tolist()

    return jsonify (result[0])
  
  except Exception as e:
    return jsonify({"error":str(e)})


if __name__ =="__main__":
  app.run(debug=True)