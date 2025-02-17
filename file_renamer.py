import os

def rename_files(directory, prefix):
    files = os.listdir(directory)
    for index, file in enumerate(files):
        ext = file.split(".")[-1]
        new_name = f"{prefix}_{index}.{ext}"
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
    print("Files renamed successfully!")

if __name__ == "__main__":
    dir_path = input("Enter directory path: ")
    prefix = input("Enter prefix for new file names: ")
    rename_files(dir_path, prefix)
