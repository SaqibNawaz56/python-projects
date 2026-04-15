
import argparse
from  managing_file import analyze_folder
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    file_path = args.file_path
    total_folders,total_files,total_mb,max_mb,file_types=analyze_folder(file_path)
    print(f"--- Folder Report ---")
    print(f"Total Folders: {total_folders}")
    print(f"Total Files:   {total_files}")
    print(f"Total Size:    {total_mb} MB")
    print(f"Largest File:  {max_mb} MB")
    print(f"File Types:    {file_types}")
if __name__ == '__main__':
    main()