from flask import Flask, render_template
from post import Post

#Create Flask app
app = Flask(__name__)

#Routing
@app.route('/')
def get_all_posts():
    post = Post()#create instance with API Link
    all_posts = post.get_all_post()
    return render_template("index.html", all_post_html=all_posts)

@app.route('/post/<int:post_id>')
def single_post(post_id):
    post = Post()
    single_post = post.get_single_post(post_id)
    return render_template("post.html", single_post_html=single_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


#Run app
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")