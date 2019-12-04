import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/meals')
def meals():
    data = []
    with open("data/menu_list.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("meals.html", page_title="meals", menu_list = data)

@app.route("/meals/<menu_name>")
def meals_menu(menu_name):
    menu = {}

    with open("data/menu_list.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == menu_name:
                menu = obj
    
    return render_template("menu.html", menu=menu)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/careers')
def careers():
    return render_template("careers.html")

@app.route('/baking')
def baking():
    return render_template("baking.html")

@app.route('/breakfast')
def breakfast():
    return render_template("breakfast.html")

@app.route('/dessert')
def dessert():
    return render_template("dessert.html")

@app.route('/dinner')
def dinner():
    return render_template("dinner.html")

@app.route('/lunch')
def lunch():
    return render_template("lunch.html")


@app.route('/snacks')
def snacks():
    return render_template("snacks.html")
# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/')
# def baking():
#     return render_template("baking.html")



# @app.route('/')
# def dessert():
#     return render_template("dessert.html")

# @app.route('/')
# def dinner():
#     return render_template("dinner.html")

# @app.route('/')
# def lunch():
#     return render_template("lunch.html")

# @app.route('/')
# def snacks():
#     return render_template("snacks.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
    