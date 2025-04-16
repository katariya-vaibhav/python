import json

file_name = 'youtube_manager.txt'

def load_videos():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def halper_data_save(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")
        print(f"   Description: {video['description']}")
        print(f"   Thumbnail: {video['thumbnail']}")

def upload_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    description = input("Enter Video Description: ")
    thumbnail = input("Enter Thumbnail URL or File Path: ")
    videos.append({
        'name': name,
        'time': time,
        'description': description,
        'thumbnail': thumbnail
    })
    halper_data_save(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index number of video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        description = input("Enter new video description: ")
        thumbnail = input("Enter new thumbnail URL or file path: ")
        videos[index - 1] = {
            'name': name,
            'time': time,
            'description': description,
            'thumbnail': thumbnail
        }
        halper_data_save(videos)
    else:
        print("Invalid index. Please try again.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index number of video to delete: "))
    if 1 <= index <= len(videos):
        deleted_video = videos.pop(index - 1)
        halper_data_save(videos)
        print(f"{deleted_video['name']} video has been deleted.")
    else:
        print("Invalid index. Please try again.")

def main():
    videos = load_videos()
    while True:
        print("\n YouTube Manager | Choose Your Option \n")
        print("1. List All Videos")
        print("2. Upload Video")
        print("3. Update Video Details")
        print("4. Delete Video")
        print("5. Exit\n")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                print("Listing all videos...\n")
                list_all_videos(videos)
            case '2':
                print("Uploading video...\n")
                upload_video(videos)
            case '3':
                print("Updating video...\n")
                update_video(videos)
            case '4':
                print("Deleting video...\n")
                delete_video(videos)
            case '5':
                print("Exiting the app...\n")
                break
            case _:
                print("Please enter a valid choice.")

if __name__ == "__main__":
    main()
