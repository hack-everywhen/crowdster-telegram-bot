from _weakref import ref


import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["Reports"]
myuser = mydb["User"]

def Insert(emergency,location1,location2,phone):
    myquery = {"properties.Reference_No": phone}
    original_id = ObjectId()
    mydoc = list(mycol.find(myquery))
    print(mydoc)
    if len(mydoc) == 0:
        user_id = ObjectId()
        New_User("Sumit Kothari",phone,user_id)
    else:
        myquery2 = {"phoneno": phone}
        mydoc2 = (myuser.find(mydb))
        user_id = mydoc2[2]



    mydict = {"_id": original_id,
              "type": "Feature",
              "geometry": {"type": "Point",
              "coordinates": [location2,location1]},
              "properties": {"type": emergency,
              "Reference_No": phone,
              "report_id": original_id},
              "user_id": user_id}



    x = mycol.insert_one(mydict)

def New_User(Name,phone,user_id):

    mydict2 = {"_id": user_id,
               "name": Name,
               "phoneno": phone}
    x = myuser.insert_one(mydict2)



Insert("Fire",19.21,72.13,9769356951)





