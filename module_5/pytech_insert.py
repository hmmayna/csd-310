from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.lsky6wc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

lilly = {
    "student_id": "1007",
    "first_name": "Lilly",
    "last_name": "Potter",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "3.9",
            "start_date": "August 1, 2001",
            "end_date": "May 14, 2002",
            "courses": [
                {
                    "course_id": "CYBR428",
                    "description": "Audits",
                    "instructor": "Professor Addy K",
                    "grade": "B"
                },
                {
                    "course_id": "CYBR100",
                    "description": "Cyber Basics",
                    "instructor": "Professor Ron B",
                    "grade": "A+"
                }
            ]
        }
    ]

}

harry = {
    "student_id": "1008",
    "first_name": "Harry",
    "last_name": "Nelson",
    "enrollments": [
        {
            "term": "Session 5",
            "gpa": "4.0",
            "start_date": "August 1, 2007",
            "end_date": "May 1, 2008",
            "courses": [
                {
                    "course_id": "ART 101",
                    "description": "Intro to Art",
                    "instructor": "Professor Chelsea J",
                    "grade": "A"
                },
                {
                    "course_id": "ENG 101",
                    "description": "Intro to English",
                    "instructor": "Professor Billy G",
                    "grade": "A"
                }
            ]
        }
    ]
}

gregory = {
    "student_id": "1009",
    "first_name": "Gregory",
    "last_name": "Hillbanks",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "2.7",
            "start_date": "August 1, 2010",
            "end_date": "May 14, 2011",
            "courses": [
                {
                    "course_id": "HIST 101,
                    "description": "US History",
                    "instructor": "Professor Dylan S",
                    "grade": "F"
                },
                {
                    "course_id": "CYBR 294",
                    "description": "CYBER Defense",
                    "instructor": "Professor Karren T",
                    "grade": "C"
                }
            ]
        }
    ]
}

students = db.students

print("\n  -- INSERT STATEMENTS --")
lilly_student_id = students.insert_one(lilly).inserted_id
print("  Inserted student record Lilly Potter into the students collection with document_id " + str(lilly_student_id))

harry_student_id = students.insert_one(harry).inserted_id
print("  Inserted student record Harry Nelson into the students collection with document_id " + str(harry_student_id))

gregory_student_id = students.insert_one(gregory).inserted_id
print("  Inserted student record Gregory Hillbanks into the students collection with document_id " + str(gregory_student_id))
