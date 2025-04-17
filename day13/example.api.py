import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 🔹 GET - Fetch posts
def get_posts():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        for post in response.json()[:5]:  # Only show first 5 posts
            print(f"{post['id']}: {post['title']}")
    else:
        print("Failed to fetch posts")


# 🔹 POST - Create a new post
def create_post():
    data = {
        "title": "Learning Python APIs",
        "body": "Using the requests module is simple!",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=data)
    print("Post created:", response.json())

# 🔹 PUT - Update a post
def update_post(post_id):
    data = {
        "title": "Updated Title",
        "body": "Updated content.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=data)
    print("Post updated:", response.json())



if __name__ == "__main__":
    get_posts()
    create_post()
    update_post(1)

