from flask import Flask, render_template
import requests
from post import Post

#get post from API
# blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
# response = requests.get(blog_url)
# all_posts2 = response.json()#list with posts

#single line version to get post from API
all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

#create list with post object
post_list_object = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_list_object.append(post_obj)

#create Flask app
app = Flask(__name__)

#Routing
@app.route('/')
def home():
    return render_template("index.html", all_posts_html=post_list_object)

@app.route('/post/<int:index>')
def show_post(index):
    single_post = None
    for blog_post in post_list_object:
        if blog_post.id == index:
            single_post= blog_post
    return render_template("post.html", post_html=single_post)

if __name__ == "__main__":
    app.run(debug=True)
