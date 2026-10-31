import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        users = response.json()

        print("Total Users:", len(users))

        for user in users[:5]:
            print("\nName:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            print("Company:", user["company"]["name"])

        cities = set(user["address"]["city"] for user in users)
        print("\nUnique Cities:", len(cities))
        print("Cities:", ", ".join(sorted(cities)))

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

    except (ValueError, KeyError, TypeError) as e:
        print("Error processing data:", e)

fetch_data()
