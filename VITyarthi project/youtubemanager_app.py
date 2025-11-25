import json
def data_load():
    try:
        with open('youtube.txt','r') as file:
            test =  json.load(file)
            return(test)
    except FileNotFoundError:
        return[]
    
def save_data(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

 
def all_videos(videos):
    print("\n")
    print("-"* 195)      
    for index, video in enumerate(videos, start = 1):           
        print(f"{index}.{video['name']}, Duration : {video['time']}")       
    print("\n")
    print("-"* 195)    

def add_video(videos):
    name = input("Enter video name :")
    time = input("Enter video time :")
    videos.append({'name': name , 'time': time})
    save_data(videos)

def Video_to_update(videos):
    if not videos:
        print("No video")
        return

    all_videos(videos)
    try:
        name = int(input("Enter a no. of video to be updated : "))
        if 1 <= name  <= len(videos):
            video = videos[name - 1]
            print(f" Video name: {video['name']}")
            print(f" Video Time : {video['time']} ")

            new_name = input("Enter new video name: ")
            new_duration = input("Enter new video time : ")

            if new_name.strip():
                video['name'] = new_name
            if new_duration.strip():
                video['time'] = new_duration

            save_data(videos)
            print("Video updated")
        else:
            print("choice not valid.")

    except ValueError:
        print("Please enter a valid no.")
     

def Video_to_delete(videos):
    if not videos:
        print("There is no video that you added ")
        return

    all_videos(videos)
    try:
        video = int(input("Enter the  no. of the video to delete: "))
        if 1 <= video <= len(videos):
            delete = videos.pop(video - 1)
            save_data(videos)
            print(f"Video deleted: {delete['name']}\n")
        else:
            print("invalid request.")
    except ValueError:
        print("enter a valid video no.")
     
    

def main():

    videos = data_load()
    while True:
        print("\n This is a simple Youtube Manager  app | choose an option ")
        print("1. Show all youtube videos list .")
        print("2. Add a youtube video.")
        print("3. Update a youtube video details.")
        print("4. Delete a youtube video.")
        print("5. Exit the app.")
        choice = input("Enter your choice : ")
        #print(videos)
    
        match choice:
            case '1':
                all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                Video_to_update(videos)
            case '4':
                Video_to_delete(videos)
            case '5':
                break
            case _:
                print("Choice not valid.")

if __name__ == "__main__":
    main()
