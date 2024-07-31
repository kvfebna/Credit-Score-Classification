from flask import Flask,request,render_template
import pickle
import numpy as np

with open('model.pkl','rb') as model_file:
    model=pickle.load(model_file)

app=Flask(__name__)
                      
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/Prediction',methods=['POST'])
def detect():
   Annual_Income=float(request.form['Annual Income'])
   Amount_invested_monthly=float(request.form['Amount Invested Monthly'])
   Total_EMI_per_month=float(request.form['Total EMI Per Month'])
   Outstanding_Debt=float(request.form['Outstanding Debt'])

   Interest_Rate=float(request.form['Interest Rate'])
   if Interest_Rate<5:
      Interest_Rate_Group=0
   elif 5<=Interest_Rate<=13:
      Interest_Rate_Group=1
   elif 14<=Interest_Rate<=20:
      Interest_Rate_Group=2
   else:
      Interest_Rate_Group=3

   Num_Credit_Card=float(request.form['Number of Credit Cards'])
   if Num_Credit_Card<3:
      Num_Credit_Card_Group=0
   elif 3<=Num_Credit_Card<=4:
      Num_Credit_Card_Group=1
   elif 5<=Num_Credit_Card<=7:
      Num_Credit_Card_Group=2
   else:
      Num_Credit_Card_Group=3

   Num_Credit_Inquiries=float(request.form['Number of Credit Inquiries'])
   if Num_Credit_Inquiries<6:
      Num_Credit_Inquiries_Group=0
   elif 6<=Num_Credit_Inquiries<=8:
      Num_Credit_Inquiries_Group=1
   else:
      Num_Credit_Inquiries_Group=2

   Credit_Mix=request.form['Credit Mix']
   if Credit_Mix=='Good':
      Credit_Mix_Good=1
   else:
      Credit_Mix_Good=0

   feature=np.array([[Annual_Income,Outstanding_Debt,Total_EMI_per_month,Amount_invested_monthly,
                      Num_Credit_Card_Group,Num_Credit_Inquiries_Group,Interest_Rate_Group,Credit_Mix_Good]])
   prediction=model.predict(feature)
   return render_template('result.html',pred_res=prediction[0])

if __name__=='__main__':
  app.run(debug=True)