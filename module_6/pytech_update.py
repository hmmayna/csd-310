"""
  Title: pytech_update.py
   Author: Heather Maynard
   Date: Jaunary 22, 2023
"""


from pymongo import MongoClient

#connection string 
url = "mongodb+srv://<admin>:<admin>@cluster0.lsky6wc.mongodb.net/?retryWrites=true&w=majority"

#connection to MongoDB cluster 
client = MongoClient(url)

#connection to pytech
db = client.pytech

#retrieving student collection
students = db.students

#finding students that are in the collection
student_list = students.find({})

#message that is to be displayed
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#find document
lilly = students.find_one({"student_id": "1007"})

#output
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + lilly["student_id"] + "\n  First Name: " + lilly["first_name"] + "\n  Last Name: " + lilly["last_name"] + "\n")
  
#update student 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Drake"}})

#updated student
lilly = students.find_one({"student_id": "1007"})

#message that is to be displayed
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + lilly["student_id"] + "\n  First Name: " + lilly["first_name"] + "\n  Last Name: " + lilly["last_name"] + "\n")

#end
input("\n\n  End of program, press any key to continue...")
