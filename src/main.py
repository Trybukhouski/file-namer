import os

def list_files_in_folder():
    folder_path = input('Please enter the folder path: ').strip()
    
    if not os.path.isdir(folder_path):
        print('The specified path does not exist or is not a directory')
        return
    
    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("Folder is empty")
        return

    print("Files in folder:")
    for file in files:
        print(file)

list_files_in_folder()