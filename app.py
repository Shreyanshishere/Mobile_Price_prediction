from optparse import Values
from flask import Flask , render_template, request
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
   # values= [int(x) for x in request.form.values()]    this can be used but mobile size is not accepting float values so we used individual type
   # casting for all ram rom and stuff and flaot type casting fior mobile size then call all into values array
   ram=int(request.form.get("RAM"))
   rom=int(request.form.get('ROM'))
   ss=float(request.form.get("size"))
   pc=int(request.form.get('BACK'))
   bc=int(request.form.get('FRONT'))
   battery=int(request.form.get('BATTERY'))
   values=[ram,rom,ss,pc,bc,battery]
   final=np.array(values)
   prediction=model.predict(final.reshape(1,-1))
   output=prediction[0]
   return render_template('index.html',sent_value = f"Expected price of phone is {output}")
if __name__=="__main__":
   app.run(debug=True) 