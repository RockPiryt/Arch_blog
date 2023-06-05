from flask import Flask, render_template, request
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


#######################1 page for GET / POST method######################################
@app.route('/contact', methods=["GET","POST"])
def get_user_data():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        form_name = request.form["name"]
        form_email = request.form["email"]
        form_phone = request.form["phone"]
        form_message = request.form["message"]
        return render_template("success_send_form.html", name_html=form_name, email_html=form_email, phone_html=form_phone, message_html=form_message)


# #######################2 pages for GET / POST method#######################################
# @app.route('/contact')
# def contact_form():
#     return render_template("contact.html")

# @app.route('/send-form-info', methods=["POST"])
# def send_form_success():
#     form_name = request.form["name"]
#     form_email = request.form["email"]
#     form_phone = request.form["phone"]
#     form_message = request.form["message"]
#     return render_template("success_send_form.html", name_html=form_name, email_html=form_email, phone_html=form_phone, message_html=form_message)

#Run app
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")