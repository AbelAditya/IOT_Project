from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel

client = MongoClient("mongodb+srv://abelphilipose:1234567890@cluster-0.fyleujw.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database("first")
contacts = db.contacts

class contact(BaseModel):
    name: str
    cont: list

app = FastAPI()

@app.get("/")
def home():
    return "This is home"

@app.post("/addContacts")
def putData(data:contact):
    l = contacts.find_one({"user":data.name},{"_id":0})
    if(l!=None):
        contacts.update_one({"user":data.name},{"$set":{"contacts":data.cont}})
    else:
        contacts.insert_one({"user":data.name,"contacts":data.cont})

    return {"status":True}


@app.get("/getContacts")
def getData(user: str):
    l = contacts.find_one({"user":user},{"_id":0})
    if l!=None:
        return {"contacts":l["contacts"]}
    
    return {"contacts":[]}

