import os
import motor.motor_asyncio

MONGO_URL = os.environ.get("MONGODB_PROD_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.agenda

homeworks_data = database.get_collection("homeworks")

# Retriev all homeworks
async def retrieve_homeworks():
    homeworks_retrieved = []
    async for homework in homeworks_data.find():
        homeworks_retrieved.append(homework)
    return homeworks_retrieved

# Retrieve a ufo with a matching ID
async def retrieve_homework(homework_id: str):
    homework = await homeworks_data.find_one({"_id": homework_id})
    if homework:
        return homework

# Add a new ufo into to the database
async def insert_homework(homework_data):
    homework = await homeworks_data.insert_one(homework_data)
    new_homework = await homeworks_data.find_one({"_id": homework.inserted_id})
    return new_homework


# Update a ufo with a matching ID
async def update_homework(homework_id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    homework = await homeworks_data.find_one({"_id": homework_id})
    print(f'le homework trouvé {homework}')
    if homework:
        updated_homework = await homeworks_data.update_one(
            {"_id": homework_id}, {"$set": data}
        )
        print(f'le homework updaté {updated_homework}')
        if updated_homework:
            return True
        return False


# Delete a ufo from the database
async def remove_homework(homework_id: str):
    homework = await homeworks_data.find_one({"_id": homework_id})
    if homework:
        await homeworks_data.delete_one({"_id": id})
        return True
