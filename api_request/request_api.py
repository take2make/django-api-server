import requests

def get_json(url):
	response = requests.get(url)
	return response.json()

def send_json(url, title, description):
    params = {'title': title, 'description': description}
    response = requests.post(url, data=params)
    return response

def delete_json(url, id):
	response = requests.delete(f'{url}{id}')
	return response

url = "http://46.101.227.60:8000/api/todo/"
#send_json(url, 'купить молоко', 'в пяторочке')
#delete_json(url)
print(get_json(url))
