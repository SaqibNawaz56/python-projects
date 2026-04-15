import os
def analyze_folder(folder_path):
    total_files = 0
    total_folders = 0
    total_size = 0
    max_file_size = 0
    file_types = {}
    for root, dirs, files in os.walk(folder_path):

        total_folders = total_folders + len(dirs)

        for file_name in files:
            total_files = total_files + 1

            full_path = os.path.join(root, file_name)
            file_size = os.path.getsize(full_path)
            total_size = total_size + file_size

            if file_size > max_file_size:
                max_file_size = file_size

            name_part, extension = os.path.splitext(file_name)
            extension = extension.lower()

            if extension == "":
                extension = "No Extension"

            if extension not in file_types:
                file_types[extension] = 1
            else:
                file_types[extension] = file_types[extension] + 1

    total_mb = round(total_size / (1024 * 1024), 2)
    max_mb = round(max_file_size / (1024 * 1024), 2)
    return total_folders,total_files,total_mb,max_mb,file_types
