import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    users = response.json()

    print("Total Users:", len(users))

    for user in users[:5]:
        print(user["name"], user["email"])

except requests.exceptions.RequestException as e:
    print("Error:", e)