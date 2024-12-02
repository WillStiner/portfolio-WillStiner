import requests

def main():
    response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
    result = response.json()
    print(result)
    data = result["results"]
    print(data)
    for q in data:
        print(q)

main()