from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.lsky6wc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech
 
students = db.students

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

harry = students.find_one({"student_id": "1008"})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + harry["student_id"] + "\n  First Name: " + harry["first_name"] + "\n  Last Name: " + harry["last_name"] + "\n")

lilly = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + lilly["student_id"] + "\n  First Name: " + lilly["first_name"] + "\n  Last Name: " + lilly["last_name"] + "\n")

gregory = students.find_one({"student_id": "1009"})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + gregory["student_id"] + "\n  First Name: " + gregory["first_name"] + "\n  Last Name: " + gregory["last_name"] + "\n")
 
input("\n\n  End of program, press any key to continue...")
