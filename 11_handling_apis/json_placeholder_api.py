import requests


def fetch_todo_user_ids():
    url = "https://jsonplaceholder.typicode.com/todos"
    res = requests.get(url)
    res.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
    data = res.json()

    if isinstance(data, list):
        user_ids = [todo["userId"] for todo in data]
        return user_ids
    else:
        raise Exception("Unexpected data format")


def main():
    try:
        user_ids = fetch_todo_user_ids()
        print("User IDs:", user_ids)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
