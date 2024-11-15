from flask import Flask, render_template

app = Flask(__name__)

# Mock data for students in the "HPCAP" course
students = [
    {"name": "Alice Smith", "prn": "PRN12345"},
    {"name": "Bob Johnson", "prn": "PRN12346"},
    {"name": "Charlie Brown", "prn": "PRN12347"},
    {"name": "David Wilson", "prn": "PRN12348"},
    {"name": "Eva Adams", "prn": "PRN12349"}
]

@app.route('/')
def index():
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
