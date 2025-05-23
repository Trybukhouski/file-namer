import os

def get_folder_path():
    path = input('Please enter the folder path: ').strip()
    if not os.path.isdir(path):
        print('The specified path does not exist or is not a directory')
        return None
    return path

def list_files(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def generate_new_names(files, prefix):
    new_names = []
    for i, old_name in enumerate(files, start=1):
        _, ext = os.path.splitext(old_name)
        new_name = f"{prefix}_{i}{ext}"
        new_names.append((old_name, new_name))
    return new_names

def print_files(files):
    if not files:
        print("Folder is empty")
    else:
        print("Files in folder:")
        for file in files:
            print(file)

def main():
    folder_path = get_folder_path()
    if not folder_path:
        return

    files = list_files(folder_path)
    print_files(files)
    if not files:
        return

    prefix = input("Please enter a prefix for new filenames: ").strip()
    new_names = generate_new_names(files, prefix)
    print(new_names)

if __name__ == "__main__":
    main()
