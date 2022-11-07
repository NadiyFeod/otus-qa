import os.path
import json
from csv import DictReader


def read_json(file_path):
    with open(file_path, "r") as fd:
        return json.loads(fd.read())


def write_json(file_path, data):
    with open(file_path, "w") as fd:
        fd.write(json.dumps(data, indent=4))


def read_csv(file_path):
    with open(file_path, "r") as fd:
        csv_data = DictReader(fd)
        return [row for row in csv_data]


def distribute_books_to_users(users, list_book):
    result = []
    for one_user in users:
        result.append(
            {
                "name": one_user["name"],
                "gender": one_user["gender"],
                "address": one_user["address"],
                "book": [],
            },
        )

    index_book = len(list_book)
    while True:
        for one_user in result:
            index_book -= 1
            if index_book < 0:
                return result
            one_user["book"].append(list_book[index_book])


def get_path(dir_path, filename: str):
    return os.path.join(dir_path, filename)


if __name__ == '__main__':
    files_dir = os.path.join(os.path.dirname(__file__), "files")

    books_csv_file_path = get_path(files_dir, filename="books-133064-871075.csv")
    users_json_file_path = get_path(files_dir, filename="users-39204-8e2f95.json")

    users = read_json(users_json_file_path)
    books = read_csv(books_csv_file_path)
    result = distribute_books_to_users(users, books)
    write_json("result.json", result)
