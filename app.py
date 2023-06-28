from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
def recom(dep,mod,pay):
    df1=pd.read_csv('Database.csv')
    df=pd.DataFrame(df1.loc[df1.DEPT == dep])
    print(df)
    df2=pd.DataFrame(df.loc[df.MODE == mod])
    print(df2,mod,"@##@$@",df.MODE == mod)
    df3=pd.DataFrame(df2.loc[df2['PAID/UNPAID'] == pay])
    print(df3)
    return df3.values.tolist()
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def akhil():
    if request.method=="POST":
        dept=request.form.get("Department")
        mod=request.form.get("mode")
        pay=request.form.get("payment")
        result=recom(dept,mod,pay)
        return render_template(r"web4.html",results=result)
    return render_template(r"web4.html",results=[])
if __name__=='__main__':
    app.run(debug=True)
    
