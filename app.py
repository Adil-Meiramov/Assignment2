from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store user preferences and recipes
user_data = {"name": "", "preferences": {}, "recipes": []}

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/preferences", methods=["POST"])
def preferences():
    user_data["name"] = request.form.get("name")
    return render_template("preferences.html")

@app.route("/save_preferences", methods=["POST"])
def save_preferences():
    user_data["preferences"] = {
        "diet": request.form.get("diet"),
        "cuisine": request.form.get("cuisine"),
        "meals_per_week": request.form.get("meals_per_week"),
    }
    return redirect(url_for("recipe_input"))

@app.route("/recipe_input", methods=["GET", "POST"])
def recipe_input():
    if request.method == "POST":
        recipe = {
            "name": request.form.get("recipe_name"),
            "ingredients": request.form.get("ingredients"),
        }
        user_data["recipes"].append(recipe)
        return redirect(url_for("recipe_plan"))

    return render_template("recipe_input.html")

@app.route("/recipe_plan", methods=["GET"])
def recipe_plan():
    return render_template("recipe_plan.html", data=user_data)

if __name__ == "__main__":
    app.run(debug=True)
