import sqlite3

conn = sqlite3.connect("youtube_manager.db")


conn.execute('''
                CREATE TABLE IF NOT EXISTS videos (
                    id integer primary key,
                    name text not null,
                    time text not null
                )
            ''')

def list_all_videos():
    try:
        videos = conn.execute("SELECT * FROM videos")
        
        if videos == None:
            print("No video found")
        
        for video in videos.fetchall():
            print(video)
    except Exception as e:
        print("Error while list videos " , e)

def upload_video(name , time):
    try:
        conn.execute("INSERT INTO videos (name , time) VALUES (? , ?)" , (name , time))
        conn.commit()        
    except Exception as e:
        print("Error while upload video " , e)


def update_video(video_id , name , time):
    try:
        conn.execute("UPDATE videos SET name = ? , time = ? where id = ? " , (name , time , video_id))
        conn.commit()        
    except Exception as e:
        print("Error while update video " , e)


def delete_video(video_id):
    try:
        conn.execute("DELETE FROM videos where id = ?" , (video_id,))
        conn.commit()        
    except Exception as e:
        print("Error while delete video " , e)


def main():
    while True:
        print("\n YouTube Manager | choose your option \n")
        print("1. List All Videos")
        print("2. Upload Video")
        print("3. Update Video Details")
        print("4. Delete Video")
        print("5. Exit \n")        
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                print("Listing all videos...")
                list_all_videos()
            case '2':
                print("Upload video...")
                name = input("Enter video name : ")
                time = input("Enter video time : ")
                upload_video(name , time)
            case '3':
                print("Update video...")
                list_all_videos()
                video_id = int(input("Enter video id : "))
                name = input("Enter video name : ")
                time = input("Enter video time : ")
                update_video(video_id , name , time)
            case '4':
                list_all_videos()
                print("Delete video...")
                video_id = int(input("Enter video id : "))
                delete_video(video_id)
            case '5':
                print("Exitting the app....")
                conn.close()
                break
            case _:
                print("Please Enter Valid Choice...")
    
    conn.close()                    

if __name__ == "__main__":
    main()