from pprint import pprint


def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        cats_info = []

        for line in lines:
            cat_id, name, age = line.strip().split(',')
            cat_info = {
                "id": cat_id,
                "name": name,
                "age": age
            }
            cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
        return []
    except ValueError as ve:
        print(f"Error: Incorrect file format. {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


cats_info = get_cats_info("02_cats.txt")
pprint(cats_info)
