"""
  Title: pytech_delete.py
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
    
#test document
test_doc = {
    "student_id": "2001",
    "first_name": "Kinder",
    "last_name": "Sue"
}

#inserting test document
test_doc_id = students.insert_one(test_doc).inserted_id

#inserting statements 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

#find_one() method with student 2001
student_test_doc = students.find_one({"student_id": "2001"})

#output results
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

#delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "2001"})

#find students
new_student_list = students.find({})

#message that is to be displayed
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#output results
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#end
input("\n\n  End of program, press any key to continue...")
