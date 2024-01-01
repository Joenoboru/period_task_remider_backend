import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.period

student_collection = database.get_collection("students_collection")
task_collection = database.get_collection("task")


# helpers


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }


# crud operations


# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True
    



def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "task": task["task"],
        "reminder_cycle": task["reminder_cycle"],
        "dayCount": task["dayCount"],
    }


# crud operations


# Retrieve all students present in the database
async def retrieve_tasks():
    tasks = []
    async for task in task_collection.find():
        tasks.append(task_helper(task))
    return tasks


# Add a new student into to the database
async def add_task(task_data: dict) -> dict:
    task = await task_collection.insert_one(task_data)
    task = await task_collection.find_one({"_id": task.inserted_id})
    return task_helper(task)


# Retrieve a student with a matching ID
async def retrieve_task(id: str) -> dict:
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        return task_helper(task)


# Update a student with a matching ID
async def update_task(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        updated_task = await task_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_task:
            return True
        return False


# Delete a student from the database
async def delete_task(id: str):
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        await task_collection.delete_one({"_id": ObjectId(id)})
        return True
