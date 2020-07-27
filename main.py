from flask import Flask,render_template,request,jsonify
import pickle
from wsgiref import simple_server
import sklearn
from flask_cors import CORS,cross_origin

app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return  render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method=='POST':
        try:
            Pregnancies=int(request.form['Pregnancies'])
            Glucose = int(request.form['Glucose'])
            BloodPressure=int(request.form['BloodPressure'])
            SkinThickness = int(request.form['SkinThickness'])
            Insulin = int(request.form['Insulin'])
            BMI = float(request.form['BMI'])
            DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
            Age = int(request.form['Age'])
            filename='model.pkl'
            loaded_model=pickle.load(open(filename,'rb'))
            prediction=loaded_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
            print('prediction is :',prediction)
            diabetic="You have Diabetes"
            non_diabetic="You don't have Diabetes"
            if prediction==0:
                return render_template('results.html', prediction=non_diabetic)
            else:
                return render_template('results.html', prediction=diabetic)
        except Exception as e:
            print('The exception message is :',e)
            return 'Something has gone Wrong'
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)