from flask import Flask, render_template, request, jsonify
import random  # Replace with actual data source

app = Flask(__name)

# Dummy data for testing (replace with actual data source)
def get_environment_data():
    return {
        "temperature": random.uniform(10, 30),
        "humidity": random.uniform(30, 80),
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/environment_data")
def get_environment_data_api():
    data = get_environment_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
