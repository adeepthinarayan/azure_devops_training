from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {"id": 101, "name": "Alice", "department": "HR"},
    {"id": 102, "name": "Bob", "department": "IT"},
    {"id": 103, "name": "Charlie", "department": "Finance"},
]

@app.route("/")
def home():
    return render_template("index.html", employees=employees)

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)