import requests

def get_json(url):
	response = requests.get(url)
	return response.json()

def send_json(url, title, description, pic):
    params = {'title': title, 'description': description}
    upload = {'photo': open(pic, 'rb')}
    response = requests.post(url, data=params, files=upload)
    return response

def delete_json(url, id):
	response = requests.delete(f'{url}{id}')
	return response

url = "http://127.0.0.1:8000/api/todo/"
print(send_json(url, 'купить молоко2', 'в пяторочке', 'cat.png'))
#delete_json(url)
print(get_json(url))
