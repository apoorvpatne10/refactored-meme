import requests

payload = {"some": "data"}
r = requests.post("http://127.0.0.1:5000/file_upload", json=payload)
print(r.json())
