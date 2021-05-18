from flask import Flask,render_template,url_for,flash,redirect
import joblib
from flask import request
import numpy as np
import requests
import pickle

app=Flask(__name__,template_folder='template')
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'



@app.route("/",methods=['GET'])
def homepage():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")
 
@app.route("/yoga")
def yoga():
    return render_template("yoga.html")

@app.route("/cancer")
def cancer():
    return render_template("cancer.html")

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/kidney")
def kidney():
    return render_template("kidney.html")

@app.route("/Pneumonia")
def Pneumonia():
    return render_template("pneumonia.html")

def ValuePredictor(to_predict_list, size):

    to_predict = np.array(to_predict_list).reshape(1,size)
   
    if(size==8):#Diabetes
        loaded_model = pickle.load(open('diabetes prediction.pkl','rb'))
        result = loaded_model.predict(to_predict)
    elif(size==30):#Cancer
        loaded_model = pickle.load(open('cancer prediction.pkl','rb'))
        result = loaded_model.predict(to_predict)
    elif(size==24):#Kidney
        loaded_model = pickle.load(open('kidney prediction.pkl','rb'))
        result = loaded_model.predict(to_predict)
    elif(size==13):#Heart
        loaded_model = pickle.load(open('heart prediction.pkl','rb'))
        result =loaded_model.predict(to_predict)
    return result[0]
@app.route('/result',methods = ["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==30):#Cancer
            result = ValuePredictor(to_predict_list,30)
        elif(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)
        elif(len(to_predict_list)==13):#Heart
            result = ValuePredictor(to_predict_list,13)
        elif(len(to_predict_list)==24):#Kidney
            result = ValuePredictor(to_predict_list,24)
    if(int(result)==1):
        prediction='Sorry ! Suffering,Please get a checkup done.'
    else:
        prediction='Congrats ! you are Healthy' 
    return (render_template("result.html", prediction=prediction))
    

if __name__ == '__main__':
    app.run(debug=True)
