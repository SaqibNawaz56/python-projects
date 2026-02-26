def read_csv_file(path):
    try:
        with open(path, 'r') as file:
            table = [strline.strip().split(',') for strline in file.readlines()]
            headers = table[0]
            data_as_dict_list = [{headers[i]: elem for i, elem in enumerate(line)} for line in table[1:]]
            return data_as_dict_list
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []