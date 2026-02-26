def read_logs_file(path):
    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
