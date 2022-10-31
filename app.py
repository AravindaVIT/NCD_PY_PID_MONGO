from flask import Flask, render_template, request
from pymongo import MongoClient 
from random import randint
# import pymongo


app = Flask(__name__, template_folder='templates')

firstname = " "
add = 0
res = " "
patient_id=" "

@app.route('/', methods=['GET',"POST"])
def reg():
    return render_template('resgister1.html')
    

@app.route('/register', methods=['GET',"POST"]) 
def register():
    global firstname
    lastname = " "
    gender = " "
    birthday = " "
    pincode = " "
    #patient_id=0
    patient_id = randint(10000000000000,99999999999999)
    print(patient_id)
    if request.method == "POST":
    
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        birthday = request.form['birthday']
        pincode = request.form["pin"]
        #patient_id=randompatient_id(14)
        
        Collection.insert_one(
            { "patient_id":patient_id,
                "firstname" : firstname,
        "lastname":lastname,
        "gender":gender,
        "birthday":birthday,
        "pincode":pincode,
       }
        )
    return render_template('araa1.html',id = patient_id)

    

@app.route('/araa1', methods=['GET',"POST"])
def home():
    
    if request.method == "POST":
        
        while True:
            age = request.form.get('first')
            smoke = request.form.get('second')
            alcohol = request.form.get('third')
            waist = request.form.get('fourth')
            activity = request.form.get('fifth')
            history = request.form.get('sixth')
            Collection.update_one(
                {"firstname":firstname},
            {"$set": {"first" :age,
            'second': smoke,
             "third":alcohol,
            "fourth":waist,
            "fifth":activity,
            "sixth":history}}
       
        )
            score = float(age) + float(smoke)+float(alcohol)+float(waist) + float(activity)+float(history)
            global add
            add=score  
            global res
            if score>4:
                res="screening needed"
                Collection.update_one(
                {"firstname":firstname},
                {"$set": {"total_count" :add}})
            else:
                res="no need to screen"
                Collection.update_one(
                {"firstname":firstname},{"$set": {"total_count" :add}})
            return render_template('result1.html', add1=add,res=res)
    return render_template('araa1.html')



@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('register1.html')


if __name__ == "__main__":
     try:
        client = MongoClient("mongodb://localhost:27017")
        db = client['PYTHON_MONGO_NCD_ID']
        Collection = db["PATIENT"]
        # client.server_info() #trigger exception if it cannot connect to database
        
     except Exception as e:
        print(e)
        print("Error - Cannot connect to database")
     app.run(debug=True)