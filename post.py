import requests

class Post():
    def __init__(self):
        self.post_url = "https://api.npoint.io/6c4f0f978204ff0ae340"

    def get_all_post(self):
        all_post = requests.get(url=self.post_url).json()
        return all_post
    
    def get_single_post(self, post_id):
        all_post = requests.get(url=self.post_url).json()
        single_post = [post for post in all_post if int(post["id"]) == int(post_id)]
        print(single_post)
        return single_post[0]