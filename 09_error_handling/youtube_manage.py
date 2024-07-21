import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            if not file:
                return []
            else:
                return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    if not videos:
        print("No videos found.")
    else:
        print("\n")
        print("*" * 70)
        for index, video in enumerate(videos, 1):
            print(f"{index}. {video['name']} - {video['time']} \n")
        print("*" * 70)


def add_video(videos):
    name = input("Enter video name: \n")
    time = input("Enter video time: \n")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    update_index = int(input("Enter the index you wants to update \n"))
    if 1 <= update_index <= len(videos):
        name = input("Enter the video name\n")
        time = input("Enter the video time\n")

        videos[update_index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Entered Invalid Index")


def delete_video(videos):
    list_all_videos(videos)
    del_index = int(input("Enter the index you wants to deleted \n"))
    if 1 <= del_index <= len(videos):
        del videos[del_index - 1]
        save_data_helper(videos)
    else:
        print("Entered Invalid Index")


def main():
    videos = load_data()

    # video=[]
    while True:
        print("\n youtube manager | choice an option")
        print("\n 1. List all youtube videos")
        print("\n 2. Add a youtube videos")
        print("\n 3. Update youtube videos details")
        print("\n 4. Delete youtube videos")
        print("\n 5. Exit the app")

        choice = input("Enter your choice:  ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
