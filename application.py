from flask import Flask, render_template, request
from post import Post
import smtplib 
from email.message import EmailMessage
import os
from dotenv import load_dotenv

#Get user info to send email
load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")
my_email= os.getenv("MY_EMAIL")
api_key_gmail = os.getenv("APP_PASSWORD_GMAIL")

#Create Flask application
application = Flask(__name__)

#Routing
@application.route('/')
def get_all_posts():
    post = Post()#create instance with API Link
    all_posts = post.get_all_post()
    return render_template("index.html", all_post_html=all_posts)

@application.route('/post/<int:post_id>')
def single_post(post_id):
    post = Post()
    single_post = post.get_single_post(post_id)
    return render_template("post.html", single_post_html=single_post)

@application.route('/about')
def about():
    return render_template("about.html")

##########1 route for GET / POST method + HTML template+EMAIL MODULE###########################
@application.route('/contact', methods=["GET","POST"])
def get_user_data():
    #Show form
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    #Get user data and show, which data are received
    else:
        form_name = request.form["name"]
        form_email = request.form["email"]
        form_phone = request.form["phone"]
        form_message = request.form["message"]
        send_email(form_name, form_email, form_phone, form_message)
        return render_template("contact.html", name_html=form_name, email_html=form_email, phone_html=form_phone, message_html=form_message, msg_sent=True)
        
# def send_email(name=form_name, email=form_email, phone=form_phone, message=form_message):
def send_email(name, email, phone, message):

    #Create email
    user_info = f"""
    Here are information from user: \n
    Name: {name}, \n
    Email: {email}, \n
    Phone: {phone}, \n
    Message: {message}.
    """
    msg = EmailMessage()
    msg.set_content(user_info)
    msg["Subject"] = "Arch Blog fan contact!"
    msg["From"] = my_email
    msg["To"] = my_email

    #Send email with form's information
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=api_key_gmail)
        connection.send_message(msg)

#Run application
if __name__ == "__main__":


# #############1 route for GET / POST method + HTML template##############################
# @application.route('/contact', methods=["GET","POST"])
# def get_user_data():
#     if request.method == "GET":
#         return render_template("contact.html", msg_sent=False)
#     else:
#         form_name = request.form["name"]
#         form_email = request.form["email"]
#         form_phone = request.form["phone"]
#         form_message = request.form["message"]
        
#         user_data = f"""
#         Here are information from user - page Arch Blog. \n
#         Name: {form_name}, \n
#         Email: {form_email}, \n
#         Phone: {form_phone}, \n
#         Message: {form_message}.
#         """
#         with smtplib.SMTP("smtp.gmail.com") as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=api_key_gmail)
#             connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: User contact\n\n {user_data}")
#         return render_template("contact.html", name_html=form_name, email_html=form_email, phone_html=form_phone, message_html=form_message, msg_sent=True)



# #######################1 route for GET / POST method######################################
# @application.route('/contact', methods=["GET","POST"])
# def get_user_data():
#     if request.method == "GET":
#         return render_template("contact.html")
#     else:
#         form_name = request.form["name"]
#         form_email = request.form["email"]
#         form_phone = request.form["phone"]
#         form_message = request.form["message"]
#         return render_template("success_send_form.html", name_html=form_name, email_html=form_email, phone_html=form_phone, message_html=form_message)


# #######################2 routes for GET / POST method#######################################
# @application.route('/contact')
# def contact_form():
#     return render_template("contact.html")

# @application.route('/send-form-info', methods=["POST"])
# def send_form_success():
#     form_name = request.form["name"]
#     form_email = request.form["email"]
#     form_phone = request.form["phone"]
#     form_message = request.form["message"]
#     return render_template("success_send_form.html", name_html=form_name, email_html=form_email, phone_html=form_phone, message_html=form_message)
    application.run(debug=True, host="localhost", port="5000")