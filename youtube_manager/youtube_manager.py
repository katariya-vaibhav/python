import json

file_name = 'youtube_manager.txt'

def load_videos():
    try:
        with open(file_name , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def halper_data_save(videos):
    with open(file_name , 'w') as file:
        json.dump(videos , file)        

def list_all_videos(videos):
    for index , video in enumerate(videos , start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")

def upload_video(videos):
    name = input("Enter Video Name : ")
    time = input("Enter Video Time : ")
    videos.append({'name' : name , 'time' : time})
    halper_data_save(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index number of video : "))
    if 1 <= index <= len(videos):
        name = input("Enter video name : ")
        time = input("Enter video time : ")
        videos[index-1] = {'name':name , 'time':time}
        halper_data_save(videos)
    else:
        print("Invalid Index Selected Please Try Again....")
        
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index number of video : "))
    if 1 <= index <= len(videos):
        # del videos[index-1]
        deleted_video = videos.pop(index-1)
        halper_data_save(videos)
        print(f"{deleted_video['name']} video is deleted")
    else:
        print("Invalid Index Selected Please Try Again....")
    
def main():
    videos = load_videos()
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
                list_all_videos(videos)
            case '2':
                print("Uploading video...")
                upload_video(videos)
            case '3':
                print("Update video...")
                update_video(videos)
            case '4':
                print("Delete video...")
                delete_video(videos)
            case '5':
                print("Exitting the app....")
                break
            case _:
                print("Please Enter Valid Choice...")


if __name__ == "__main__":
    main()