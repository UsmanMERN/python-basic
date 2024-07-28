from pymongo import MongoClient
from bson import ObjectId  # Import if using ObjectId for _id


client = MongoClient(
    "mongodb+srv://competition:addpasswordhere@cluster0.g1vq5d2.mongodb.net/ytManager?retryWrites=true&w=majority",
    tlsAllowInvalidCertificates=True,
)

db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)


def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name : {video['name']}, and Time : {video['time']}")


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(video_id: str, name: str, time: str):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},  # Filter as a dictionary
        {"$set": {"name": name, "time": time}},
    )


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n youtube manager App | mongoDB")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a new video")
        print("4. Delete a new video")
        print("5. Exist the App")
        choice = input("Enter your Choice :\n")

        if choice == "1":
            list_video()
        elif choice == "2":
            name = input("Enter the video name: \n")
            time = input("Enter the video time: \n")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video video id to update: \n")
            name = input("Enter the updated video name: \n")
            time = input("Enter the updated video time: \n")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video video id to update: \n")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Enter the valid choice: \n")


if __name__ == "__main__":
    main()
