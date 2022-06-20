from flask import Flask, render_template, url_for, request, redirect
import csv

# redirect is used to redirect us to some subpage after some condition is met
app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/works.html")
def works():
    return render_template("works.html")


@app.route("/work.html")
def work():
    return render_template("work.html")


@app.route("/work2.html")
def work2():
    return render_template("work2.html")


@app.route("/download.html")
def download():
    return render_template("download.html")


def write_to_file(data):
    with open('database.txt', mode='a+') as database:  # mode - append
        email = data["email"]  # data is defined in the function submit_form()
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')
        # file = database.write(f'\n{email},{subject},{message}')
        # print(file)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:  # mode - append
        email = data["email"]  # data is defined in the function submit_form()
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])



#    return 'form submitted hoooorayyyy!'

# Method Post - the browser wants us to save information to the server
# Method Get - the browser wants us to send information from the server
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            print(data)
            write_to_csv(data)
            # print("done")
            # print(data, data)
            # return 'form submitted'
            return redirect('/thankyou.html')
        except:
            raise
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

# @app.route("/blog")
# def blog():
#     return "<p>This is my first blog page. Nothing to say right now uaaaaah.</p>"
#
# @app.route("/2020/dogs")
# def blog2():
#     return "<p>this is my dog</p>"
#
# @app.route("/index_about")
# def html_index_file2():
#     return render_template("index_about.html")
#
# @app.route("/favicon")
# def favicon_f():
#     return "<p>this is my dog</p>"
