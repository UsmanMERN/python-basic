import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS VIDEO(
#                id INTEGER PRIMARY KEY
#                name TEXT NOT NULL,
#                time TEXT NOT NULL,
#     )
# """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
""")


def list_videos():
    cursor.execute("SELECT * FROM videos")

    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name, time))
    con.commit()


def update_video(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\n youtube manager with DB| choice an option")
        print("\n 1. List all youtube videos")
        print("\n 2. Add a youtube videos")
        print("\n 3. Update youtube videos details")
        print("\n 4. Delete youtube videos")
        print("\n 5. Exit the app")

        choice = input("Enter your choice:  ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name\n")
            time = input("Enter the video duration\n")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to Update\n")
            name = input("Enter the video name ")
            time = input("Enter the video duration\n")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to Delete\n")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice : \n")

    con.close()


if __name__ == "__main__":
    main()
