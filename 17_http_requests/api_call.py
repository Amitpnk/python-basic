# api_call.py
# Demonstrates making HTTP requests using the 'requests' library

import requests

# 🌐 Public test API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"

# ✅ GET request
response = requests.get(url)

print("📡 Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("\n📦 JSON Response:")
    print(f"ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
else:
    print("❌ Failed to fetch data")

# ✅ POST request example
post_data = {
    "title": "Hello from Python",
    "body": "This is a test POST request",
    "userId": 1
}

post_url = "https://jsonplaceholder.typicode.com/posts"
post_response = requests.post(post_url, json=post_data)

print("\n📬 POST request result:")
print("Status Code:", post_response.status_code)
print("Response JSON:", post_response.json())
